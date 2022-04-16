# Accounts Dictionary
import datetime

accounts = {
    'Mutulu Shakur': {
        'pin': 1111,
        'first': 'Matulu',
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
            {'date': '04/12/2022', 'deb_cred': 'debit', 'expense': 'random expense', 'amt': -311.21,
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
             'remaining': 4233.00},
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

Un-comment code below before copy/paste, REMEMBER TO RE-APPLY COMMENT NOTATION BEFORE RUNNING PROGRAM
"""
# # Print ALL USERS DEBIT TRANSACTIONS
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


# # Print ALL USERS SAVING TRANSACTIONS
# date = str(datetime.date.today())
# print(f'{date:>80}')
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
#     print()


# # Print ALL USERS DEBIT & SAVING TRANSACTIONS (SEPERATED)
# date = str(datetime.date.today())
# print(f'{date:>80}')
# for account in accounts.values():
#     print()
#     # print({f"{account['first']:60} {account['last']:20"})
#     print(f"{account['first']:^10}{account['last']:<50}")
#     print()
#     print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
#     print('-' * 80)
#     print(f"{'Debit':^10}")
#     for transaction_ in account['debit_transactions']:
#         # print(transaction_)
#         print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
#               f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
#     print()
#     print(f"{'Savings':^10}")
#     for transaction_ in account['savings_transactions']:
#         print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
#               f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")

# # Print ALL USERS DEBIT & SAVING TRANSACTIONS (COMBINED)
# date = str(datetime.date.today())
# print(f'{date:>80}')
# for account in accounts.values():
#     joint_transaction = account['debit_transactions'] + account['savings_transactions']
#
#     print()
#     print(f"{account['first']:^10}{account['last']:<50}")
#     print()
#     print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
#     print('-' * 80)
#
#     print(f"{'Debit':^10}")
#     for transaction_ in joint_transaction:
#         # print(transaction_)
#         print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
#               f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
#     print()
