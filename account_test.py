import unittest # importing the unittest module
from account import Account # importing the class account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = Account("clinton","Facebook","232323","clin@g.com") #created account object

    def test_init(self):
        """
        test_init is to test if the objects are initialized properly
        """ 
        self.assertEqual(self.new_account.user_name,"clinton")
        self.assertEqual(self.new_account.account_name,"Facebook")
        self.assertEqual(self.new_account.password,"232323")
        self.assertEqual(self.new_account.email,"clin@g.com")

    def test_save_account(self):
        """
        """
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),1)
