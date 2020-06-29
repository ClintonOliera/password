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

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """  
        Account.account_list = []  

    def test_save_multiple_account(self):
        """
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        """
        self.new_account.save_account()
        test_account =Account("clin","twiter","565656","tw@g.com")
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
        """
        test_delete_account to test if we can remove an account from our account list
        """
        self.new_account.save_account()
        test_account = Account("clin","twiter","565656","tw@g.com")
        test_account.save_account()

        self.new_account.delete_account()# deleting the account object
        self.assertEqual(len(Account.account_list),1)







if __name__ == "__main__":
    unittest.main()