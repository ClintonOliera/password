import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("status","clinton","454545","st@g.com")


    def test_init(self):
        """
        To test if the objects are initialized properly
        """  
        self.assertEqual(self.new_credentials.credentials_name,"status")
        self.assertEqual(self.new_credentials.name,"clinton")
        self.assertEqual(self.new_credentials.password,"454545")
        self.assertEqual(self.new_credentials.email, "st@g.com")

if __name__ == "__main__":
    unittest.main()          