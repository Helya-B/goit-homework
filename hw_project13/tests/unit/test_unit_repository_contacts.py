import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.repository import contacts as contacts_repository
from src.database.models import Contact
from src.schemas import ContactModel


class ContactsRepositoryTestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)

    async def test_get_contacts(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter().offset().limit().all.return_value = contacts
        result = await contacts_repository.get_contacts(1,
                                                        skip=0,
                                                        limit=10,
                                                        search=None,
                                                        with_close_bithdate=False,
                                                        db=self.session)
        self.assertEqual(result, contacts)


if __name__ == '__main__':
    unittest.main()
