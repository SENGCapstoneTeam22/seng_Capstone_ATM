# Accounts Dictionary
import datetime
# Added import random to support withdraw code @ the bottom.
import random 

accounts = {
    'Mutulu Shakur': {
        'pin': 1111,
        'first': 'Mutulu',
        'last': 'Shakur',
        'dob': '00/00/00',
        'debit': 7430,
        'saving': 247,
        'credit': 900,
        'credit_used': 113,
        'address': '1884 ECU Blvd.',
        'state': '1884 ECU Blvd.',
        'debit_transactions': [
            # date, deb_cred, expense, amt, remaining,
            {'date': '04/12/2022', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -312.21,
             'remaining': 1926.62},
            {'date': '04/10/2022', 'deb_cred': 'credit', 'expense': 'random expense', 'amt': 1450.00,
             'remaining': 2237.69},
            {'date': '04/04/2022', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -234.83,
             'remaining': 787.69},
            {'date': '04/04/2022', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -45.32,
             'remaining': 1022.52},
            {'date': '04/01/2022', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -87.16,
             'remaining': 155.04},
        ],
        'savings_transactions': [
            {'date': '04/10/2022', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 4633.19},
            {'date': '03/21/2022', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 4233.19},
            {'date': '03/07/2022', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3833.19},
            {'date': '02/21/2022', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3433.19},
            {'date': '02/07/2022', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3033.19},
        ],
    },
    'Jacques Kallis': {
        'pin': 2222,
        'first': 'Jacques',
        'last': 'Kallis',
        'dob': '00/00/00',
        'debit': 200,
        'saving': 247,
        'credit': 900,
        'credit_used': 113,
        'address': '1884 ECU Blvd.',
        'state': '1884 ECU Blvd.',
        'debit_transactions': [
            # date, deb_cred, expense, amt, remaining,
            {'date': '04/12/2021', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -311.21,
             'remaining': 1926.62},
            {'date': '04/10/2021', 'deb_cred': 'credit', 'expense': 'random expense', 'amt': 1450.00,
             'remaining': 2237.69},
            {'date': '04/04/2021', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -234.83,
             'remaining': 787.69},
            {'date': '04/04/2021', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -45.32,
             'remaining': 1022.52},
            {'date': '04/01/2021', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -87.16, 'remaining': 155.04}
        ],
        'savings_transactions': [
            {'date': '04/10/2021', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 4633.19},
            {'date': '03/21/2021', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 4233.00},
            {'date': '03/07/2021', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3833.19},
            {'date': '02/21/2021', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3433.19},
            {'date': '02/07/2021', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3033.19},
        ],
    },
    'Ricky Bobby': {
        'pin': 3333,
        'first': 'Ricky',
        'last': 'Bobby',
        'dob': '00/00/00',
        'debit': 3000,
        'saving': 247,
        'credit': 900,
        'credit_used': 113,
        'address': '1884 ECU Blvd.',
        'state': 'NC',
        'debit_transactions': [
            # date, deb_cred, expense, amt, remaining,
            {'date': '04/12/2020', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -311.21,
             'remaining': 1926.62},
            {'date': '04/10/2020', 'deb_cred': 'credit', 'expense': 'random expense', 'amt': 1450.00,
             'remaining': 2237.69},
            {'date': '04/04/2020', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -234.83,
             'remaining': 787.69},
            {'date': '04/04/2020', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -45.32,
             'remaining': 1022.52},
            {'date': '04/01/2020', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -87.16, 'remaining': 155.04}
        ],
        'savings_transactions': [
            {'date': '04/10/2020', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 4633.19},
            {'date': '03/21/2020', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 4233.00},
            {'date': '03/07/2020', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3833.19},
            {'date': '02/21/2020', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3433.19},
            {'date': '02/07/2020', 'deb_cred': 'credit', 'expense': 'DIRECT DEPOSIT - JOB', 'amt': 400,
             'remaining': 3033.19},
        ],
    },
}

# transaction = ['date', 'debit or credit', 'random expense', 'amount debited/credited', 'remaining amount']

# # Creation of User (to be used later w/ create-user view in admin)
# accounts['User_1'] = {
#     'pin': 0000,
#     'first': 'Matulu',
#     'last': 'Shakur',
#     'dob': '00/00/00',
#     'debit': 3218,
#     'saving': 247,
#     'credit': 900,
#     'credit_used': 113,
#     'address': '1884 ECU Blvd.',
#     'state': '1884 ECU Blvd.',
#     'debit_transactions': [],
#     'savings_transactions': [],
#     'credit_transactions': []
# }


# Admin Functions/Loops
"""
A For-Loop that prints members name and all debit transactions.
Combine For-Loops to print multiple values, debit + saving = all transactions.


                                                                      2022-04-16
  Matulu  Shakur                                            

   Date      Debit/Credit          Expense               Amount        Balance 
--------------------------------------------------------------------------------
04/12/2022      debit           random expense          -311.21        1926.62
04/10/2022      credit          random expense           1450.0        2237.69
04/04/2022      debit           random expense          -234.83         787.69


 Jacques  Kallis                                            

   Date      Debit/Credit          Expense               Amount        Balance 
--------------------------------------------------------------------------------
04/12/2021      debit           random expense          -311.21        1926.62
04/10/2021      credit          random expense           1450.0        2237.69
04/04/2021      debit           random expense          -234.83         787.69


  Ricky   Bobby                                             

   Date      Debit/Credit          Expense               Amount        Balance 
--------------------------------------------------------------------------------
04/12/2020      debit           random expense          -311.21        1926.62
04/10/2020      credit          random expense           1450.0        2237.69
04/04/2020      debit           random expense          -234.83         787.69

******  UN-COMMENT INDIVIDUALLY CODE SNIPPETS BELOW FOR TESTING & BEFORE copy/paste  ******

    - RUN THE PROGRAM AFTER UN-COMMENTING A SNIPPET BELOW TO VIEW IT'S ACTION...

REMEMBER TO RE-APPLY COMMENT NOTATION BEFORE RUNNING PROGRAM FOR PRODUCTION.
"""
# # PRINT ALL USERS DEBIT TRANSACTIONS (^^EXAMPLE ABOVE^^)
# date = str(datetime.date.today())
# print(f'{date:>80}')
# for account in accounts.values():
#     print()
#     # print({f"{account['first']:60} {account['last']:20"})
#     print(f"{account['first']:^10}{account['last']:<50}")
#     print()
#     print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
#     print('-' * 80)
#     for transaction_ in account['debit_transactions']:
#         # print(transaction_)
#         print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
#               f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
#     print()


# # PRINT ALL USERS SAVING TRANSACTIONS
# date = str(datetime.date.today())
# print(f'{date:>80}')
# remaining_balance_list = []
# for account in accounts.values():
#     print()
#     # print({f"{account['first']:60} {account['last']:20"})
#     print(f"{account['first']:^10}{account['last']:<50}")
#     print()
#     print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
#     print('-' * 80)
#     for transaction_ in account['savings_transactions']:
#         # print(transaction_)
#         print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
#               f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
#
#     print()


# # PRINT ALL USERS DEBIT & SAVING TRANSACTIONS (SEPERATED)
# # Create variable that store the current date as a String
# date = str(datetime.date.today())
# # Print the current date at the top-far-right of the UI
# print(f'{date:>80}')
#
# # Iterate through accounts.values() to access inner dictionaries.
# for account in accounts.values():
#     print()
#     # Print Users first and last name
#     print(f"{account['first']:^10}{account['last']:<50}")
#     print()
#
#     # Print labels above transactions
#     print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
#     print('-' * 80)
#     for transaction_ in account['debit_transactions']:
#         # Print each debit transaction
#         print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
#               f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
#     print()
#
#     # Print 'Debit' label above transactions
#     print(f"{'Savings':^10}")
#
#     for transaction_ in account['savings_transactions']:
#         print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
#               f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
#     print()


# # Print ALL USERS DEBIT & SAVING TRANSACTIONS (COMBINED)
# # Create variable that store the current date as a String
# date = str(datetime.date.today())
# # Print the current date at the top-far-right of the UI
# print(f'{date:>80}')
#
# # Iterate through accounts.values() to access inner dictionaries.
# for account in accounts.values():
#     # Create variable to hold both debit and savings transactions as two dictionaries in one list.
#     joint_transaction = account['debit_transactions'] + account['savings_transactions']  # <-- Type: LIST
#
#     print()
#
#     # Print Users first and last
#     print(f"{account['first']:^10}{account['last']:<50}")
#     print()
#
#     # Print labels above transactions
#     print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
#     # Print border-line
#     print('-' * 80)
#
#     # Print 'Debit' label above transactions
#     print(f"{'Debit':^10}")
#
#     # Iterate through the joint_transaction list (debit/savings transactions)
#     for transaction_ in joint_transaction:
#         # print(transaction_)
#         print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
#               f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
#     print()


# CODE BELOW GRABS INDIVIDUAL USER DATA, W/ OPTION TO SEARCH FOR ADMIN
# Iterate through accounts, print User-name if in accounts
#for user in accounts:
    #if 'mutulu' in user.lower(): # TODO: 'mutulu' should be replaced with input().strip() for searching the dictionary
        #print(f'  {user}')

# Iterate through accounts.values() to access inner dictionaries.
#for member in accounts.values():
    ## Create variables to hold query references.
    #pin = member['pin']
    #first = member['first']
    #last = member['last']
    #dob = member['dob']
    #debit = member['debit']
    #savings = member['saving']
    #credit = member['credit']
    #credit_used = member['credit_used']
    #address = member['address']
    #state = member['state']
    #debit_transactions = member['debit_transactions']
    #savings_transactions = member['savings_transactions']

    # date = member['pin']
    # deb_cred = member['deb_cred'] # error
    # expense = member['expense']
    # amt = member['amt']
    # remaining = member['remaining']

    # TODO: Grab last 'remaining' amt (debit/savings) and link to variables below
    # For ***USER-TEAM***, use variables below to show current money in the bank.
    # Reading the from the last transaction, the remaining amount.
    #current_debit = None
    #current_savings = None

    ## Check if the 'first-name' is equal to the users input
    #if first.lower() == 'mutulu':  # TODO: 'mutulu' should be replaced with input().strip() for searching the dictionary

        ## Print the all the information in the user dictionary of the user, using String Formatting.
        #print(f'\nPin : {pin}\nFirst : {first}\nDOB : {dob}\nDebit : {debit}\nSavings : {savings}\nCredit : {credit}\n'
              #f'Credit Used : {credit_used}\nAddress : {address}\nState : {state}\n')

        ## Print 'Debit Transactions:' before printing/displaying all debit-transactions
        #print('   Debit Transactions:\n')
        # For every debit-transaction, print transaction
        # TODO: Use String Formatting as above, to display in a more neatly/professional looking manner.
        #  Reference variables are already listed above in comments.
        #for transaction in debit_transactions:
            #print(transaction)
        ## Blank line for separation
       # print()

        ## Print 'Savings Transactions:' before printing/displaying all savings-transactions
        #print('   Savings Transactions:\n')
        #for transaction in savings_transactions:
            #print(transaction)
       ## Blank line for separation
        #print()
        
        
        
              
def innum(mess):                                          
     while True:                                          
         try:                                             
             num = float(input(mess))                     
         except ValueError:                               
             print('ERROR: Enter a number\n')             
             continue                                     
         else:                                            
             if num < 0:                                  
                 print('Negative Balance prohibited!\n')  
                 continue                                 
                                                          
             else:                                        
                 return num                               
                 break                                    
                                                          
while True:                                               
     bal = random.randint(10, 10000)                      
                                                          
while True:                                               
     draw = innum('Enter a Withdraw Amount: $')           
     if draw > bal:                                       
         print('Error: Insufficient Funds!\n')            
         continue                                         
     else:                                                
         for transaction_ in user['debit_transactions']:  
             print(f"{transaction_['deb_credit']}'") - bal
         print('Success!')                                        
        
