class Account:
    """
    A class that generates new users 
    """
    account_list = []

    def __init__(self,user_name,account_name,password,email):
        self.user_name = user_name
        self.account_name = account_name
        self.password = password
        self.email = email
