import datetime

# help('FORMATTING')

# Accounts Dictionary
accounts = {
    'Mutulu Shakur': {
        'pin': 1111,
        'first': 'Matulu',
        'last': 'Shakur',
        'dob': '00/00/00',
        'debit': 3218,
        'saving': 247,
        'credit': 900,
        'credit_used': 113,
        'address': '1884 ECU Blvd.',
        'state': '1884 ECU Blvd.',
        'debit_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-45.00',
            'amount_remaining': '1155.00'
        },
        'savings_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-45.00',
            'amount_remaining': '1155.00'
        },
        'credit_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-45.00',
            'amount_remaining': '1155.00'
        }
    },
    'Jacques Kallis': {
        'pin': 2222,
        'first': 'Jacques',
        'last': 'Kallis',
        'dob': '00/00/00',
        'debit': 3218,
        'saving': 247,
        'credit': 900,
        'credit_used': 113,
        'address': '1884 ECU Blvd.',
        'state': '1884 ECU Blvd.',
        'debit_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-50.00',
            'amount_remaining': '1150.00'
        },
        'savings_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-20.00',
            'amount_remaining': '1180.00'
        },
        'credit_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-145.00',
            'amount_remaining': '1055.00'
        }
    },
    'Ricky Bobby': {
        'pin': 3333,
        'first': 'Ricky',
        'last': 'Bobby',
        'dob': '00/00/00',
        'debit': 3218,
        'saving': 247,
        'credit': 900,
        'credit_used': 113,
        'address': '1884 ECU Blvd.',
        'state': 'NC',
        'debit_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-45.00',
            'amount_remaining': '1155.00'
        },
        'savings_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-45.00',
            'amount_remaining': '1155.00'
        },
        'credit_transactions': {
            'date': '00/00/00',
            'debit_credit': 'debit',
            'expense': 'random expense',
            'amount_debited_credited': '-45.00',
            'amount_remaining': '1155.00'
        }
    },
}

# transaction = ['date', 'debit or credit', 'random expense', 'amount debited/credited', 'remaining amount']


# # Creation of User (to be used later w/ create-user view)
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

user_1 = {
    'pin': 0000,
    'first': 'Matulu',
    'last': 'Shakur',
    'dob': '00/00/00',
    'cash': 1386,
    'debit': 3218,
    'saving': 247,
    'credit': 900,
    'credit_used': 113,
    'address': '1884 ECU Blvd.',
    'state': '1884 ECU Blvd.',
    'debit_transactions': [],
    'savings_transactions': [],
    'credit_transactions': []
}

date = str(datetime.date.today())
# Display user-name & date
print(f"\n\n{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
# Display Divider
print('-' * 35)

print(f'{"0 : Accounts":20} {"1 : Deposit":16s}')
print(f'{"2 : Transfer":20s} {"3 : Settings":16s}')
print(f'{"4 : Products":20s} {"5 : Exit":16s}\n')

user_input = input('Enter your selection:\n').strip().lower()
print('\n\n\n\n\n')

if user_input != 'exit':
    if user_input == '0' or user_input == 'checking':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        print(f'{"Current Balance":<15} : {user_1["debit"]:<10} {"1 : Deposit":16s}')
        print(f'{"1 : View Transactions":25s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
        user_input = input('Enter your selection:\n')

    if user_input == '1' or user_input == 'deposit':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
        print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
        user_input = input('Enter your selection:\n')

    if user_input == '2' or user_input == 'saving':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
        print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
        user_input = input('Enter your selection:\n')

    if user_input == '3' or user_input == 'credit':
        # Display user-name & date
        print(f"{user_1['last']:8s}{user_1['first']:14s} {date:8s}")
        # Display Divider
        print('-' * 35)

        print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
        print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
        print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
        user_input = input('Enter your selection:\n')

print('\n\nThank you for using XYZ Bank. Have a great day!')
"""
print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
print(f'{"2 : Make Withdraw":20s} {"3 : Option 4":16s}')
print(f'{"4 : Edit Profile":20s} {"5 : Exit":16s}')
"""