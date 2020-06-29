import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("status","clinton","454545","st@g.com")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """  
        Credentials.credentials_list = [] 

    def test_init(self):
        """
        To test if the objects are initialized properly
        """  
        self.assertEqual(self.new_credentials.credentials_name,"status")
        self.assertEqual(self.new_credentials.name,"clinton")
        self.assertEqual(self.new_credentials.password,"454545")
        self.assertEqual(self.new_credentials.email, "st@g.com")

    def test_save_credentials(self):
        """
        A method to save user credentials
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    

    def test_save_multiple_credentials(self):
        """
        To test if multiple credentials can be saved
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("status","clinton","454545","st@g.com")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        """
        To test if we can remove credentials from the list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("status","clinton","454545","st@g.com")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_credentials_name(self):
        """
        test to check if we can find a credential by credentials_name and display information
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("status","clinton","454545","st@g.com")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_name("status")
        self.assertEqual(found_credentials.email,test_credentials.email)









if __name__ == "__main__":
    unittest.main()          