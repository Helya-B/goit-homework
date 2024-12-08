from fastapi import APIRouter, Depends, HTTPException, status, Security, BackgroundTasks, Request

from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session


from src.database.db import get_db
from src.database.models import User
from src.schemas import UserModel
from src.helpers.auth import create_access_token, get_email_from_token, create_refresh_token, hash_handler

from src.services.email import send_email

from src.repository import users as user_repository


security = HTTPBearer()

router = APIRouter(prefix='/auth', tags=["authorization"])


@router.post("/signup")
async def signup(body: UserModel, background_tasks: BackgroundTasks, request: Request, db: Session = Depends(get_db)):
    """
    Sign up a new user

    :param body:
    :type body: UserModel
    """
    exist_user = await user_repository.get_user_by_email(body.email, db)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    body.password = hash_handler.get_password_hash(body.password)
    new_user = User(email=body.email, password=hash_handler.get_password_hash(body.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    background_tasks.add_task(send_email, new_user.email, new_user.email, request.base_url)
    return {"user": new_user, "detail": "User successfully created. Check your email for confirmation."}


@router.post("/login")
async def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await user_repository.get_user_by_email(body.username, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not user.confirmed:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not confirmed")
    if not hash_handler.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    # Generate JWT
    access_token = await create_access_token(data={"sub": user.email})
    refresh_token = await create_refresh_token(data={"sub": user.email})
    await user_repository.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.get('/refresh_token')
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    email = await get_email_from_token(token)
    user = db.query(User).filter(User.email == email).first()
    if user.refresh_token != token:
        user.refresh_token = None
        db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    access_token = await create_access_token(data={"sub": email})
    refresh_token = await create_refresh_token(data={"sub": email})
    user.refresh_token = refresh_token
    db.commit()
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.get('/confirmed_email/{token}')
async def confirmed_email(token: str, db: Session = Depends(get_db)):
    email = await get_email_from_token(token)
    user = await user_repository.get_user_by_email(email, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    await user_repository.confirmed_email(email, db)
    return {"message": "Email confirmed"}
