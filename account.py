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

    def save_account(self):
        """
        A method saves account objects into account_list
        """  
        Account.account_list.append(self)  

    def delete_account(self):
        """
        A method that deletes saved accounts from the account list
        """
        
        Account.account_list.remove(self) 
        
    @classmethod
    def find_by_name(cls,name):
        for account in cls.account_list:
            if account.account_name == name:
                return account  

    @classmethod
    def account_exist(cls,name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.password == name:
                    return account  

        return False
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list        


    
    