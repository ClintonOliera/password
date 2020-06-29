#!/usr/bin/env python3.8
from account import Account
from credentials import Credentials

def create_account(account_name,user_name,password,email):
    '''
    Function to create a new account
    '''
    new_account = Account(account_name,user_name,password,email)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()    

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()  

def find_account(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Account.find_by_name(name) 

def check_existing_accounts(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Account.account_exist(name) 

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()  



def create_credentials(credentials_name,name,password,email):
    '''
    Function to create a new account
    '''
    new_credentials = Credentials(credentials_name,name,password,email)
    return new_credentials 

def save_credentials(credentials):
    '''
    Function to save account
    '''
    credentials.save_credentials()  

def del_credentials(credentials):
    '''
    Function to delete a account
    '''
    credentials.delete_credentials()    

def find_credentials(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Credentials.find_by_name(name)  

def check_existing_credentials(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name) 

def display_credentials():  
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_credentials() 


def main():
    print("Hello Welcome to your Pass Word Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to password locker to create an account")
    print('\n')

    while True:
     print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n EX ->exit Pass Word Locker.")   
     short_code = input().lower()

     if short_code == 'su':
            print("Create a PassWord Locker Account")
            print("_"*100)
            account_name = input('Account name:')
            print ('\n')
            u_name = input('User name:')
            print ('\n')
            pwd = input('Password : ')
            print ('\n')
            e_address = input('Email address:')
            save_accounts(create_account(account_name,u_name,pwd,e_address)) 
            print ('\n')
            print(f"A New {account_name} Account with the user name  {u_name} has been created.")
            print(f"You can now login to your {account_name} account using your password.")
            print ('\n')

     elif short_code == 'da':
             if display_accounts():
                 print("Here is your account and your details")
                 print('\n')
                 for account in display_accounts():
                     print(f"Account name:{account.account_name}  User name: {account.user_name} Password:{account.password}")
                     print('\n')
             else:
                 print('\n')
                 print("You dont seem to have created an account.Sign up to create a new account.")
                 print('\n')



if __name__ == "__main__":
    main()             