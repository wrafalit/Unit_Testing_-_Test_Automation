import unittest

from phonebook.phonebook import Phonebook


class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add('BOB', '12345')
        number = phonebook.lookup('Bob')
        self.assertEqual('12345', number)