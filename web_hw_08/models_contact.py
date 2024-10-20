from mongoengine import connect, Document, StringField, BooleanField

connect(
    db="HW_08",
    host="mongodb+srv://Helya:OLHnah69*@helya.hl5fw.mongodb.net/?retryWrites=true&w=majority&appName=Helya",
)


class Contact(Document):
    full_name = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    message_sent = BooleanField(default=False)
    phone = StringField()
    preferred_contact_method = StringField(choices=["email", "sms"], default="email")