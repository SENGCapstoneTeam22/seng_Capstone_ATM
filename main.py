
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
=======
import datetime
from admin import run_admin_program
from account_holders import accounts

# help('FORMATTING')


def run_user_program(user):
    """
    THIS FUNCTION IS THE USER PROGRAM.
    After the PIN is verified, this program will run.
    The User Object/Dictionary is passed into this function to be used for CRUD.
    """
    print(user['pin'])
    print(user)
    print(user['pin'])
    date = str(datetime.date.today())
    # Display user-name & date
    print(f"\n\n{user['last']:8s}{user['first']:14s} {date:8s}")
    # Display Divider
    print('-' * 35)

    print(f'{"0 : Accounts":20} {"1 : Deposit":16s}')
    print(f'{"2 : Transfer":20s} {"3 : Settings":16s}')
    print(f'{"4 : Products":20s} {"5 : Exit":16s}\n')

    user_input = input('Enter your selection:\n').strip().lower()
    print('\n\n\n\n\n')

    if user_input != 'exit':
        if user_input == '0' or user_input == 'accounts':
            # Display user-name & date
            print(f'{user["last"]:8s} {user["first"]:14s} {date:8s}')
            # Display Divider
            print('-' * 35)

            print(f'{"Current Balance":<15} : {user["debit"]:>10}\n')
            print(f'{"1 : View Transactions":25s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":25s} {"5 : Exit":16s}\n')
            user_input = input('Enter your selection:\n')

            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(accounts)

        if user_input == '1' or user_input == 'deposit':
            # Display user-name & date
            print(f"{user['last']:8s}{user['first']:14s} {date:8s}")
            # Display Divider
            print('-' * 35)

            print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
            print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
            user_input = input('Enter your selection:\n')

            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(accounts)

        if user_input == '2' or user_input == 'transfer':
            # Display user-name & date
            print(f"{user['last']:8s}{user['first']:14s} {date:8s}")
            # Display Divider
            print('-' * 35)

            print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
            print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
            user_input = input('Enter your selection:\n')

            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(accounts)

        if user_input == '3' or user_input == 'settings':
            # Display user-name & date
            print(f"{user['last']:8s}{user['first']:14s} {date:8s}")
            # Display Divider
            print('-' * 35)

            print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
            print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')
            user_input = input('Enter your selection:\n')

            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(accounts)

        if user_input == '4' or user_input == 'products':
            # Display Divider
            print('-' * 35)

            print(f'{"Savings Interest :"}')
            print(f'{"CD Interest :"}')
            print(f'{"Business Loan Rates :"}\n')

            # Return Command
            print(f'{"0 : Return to Main Menu":20}\n')
            # Ask Admin for Next Command
            user_input = input('Enter your selection:\n')

            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '0' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                print('\n\n\n\n\n')
                # start_atm()
                run_admin_program(accounts)
    print('Thank you for using XYZ Bank. Have a great day!')


def start_atm():
    # WELCOME MESSAGE (START OF PROGRAM)
    print(f'{"Welcome to College Bank":^50s}\n\n')

    # Request User-Account PIN
    entered_pin = (input('Enter Your PIN: ')).strip()

    # Check entered PIN against all Account-PIN's by looping
    for account in accounts.values():
        # print(account['pin'])
        pin_ref = account['pin']

        # If PIN's match, run User_Program(). Passing the individual account data of matching PIN.
        if int(pin_ref) == int(entered_pin):
            # print(account)
            # Run user program/function
            run_user_program(account)

            # TODO: COME UP W/ A WAY TO CLOSE PROGRAM ON COMMAND (EXIT FUNCTION)

            # if int(entered_pin) == pin:
            #     run_user_program(account)
            # elif entered_pin == 0000:
            #     print('admin pin entered')
            # else:
            #     print('Sorry Invalid PIN, Try Again...')


start_atm()
