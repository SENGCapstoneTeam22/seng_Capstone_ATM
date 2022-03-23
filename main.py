# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# print(f'{"Player Name":16s} {"Goals":8s}')
# print('-' * 24)
#
# print(f'{"Maria":16s} {"22":8s}')
# print(f'{"Edward":16s} {"21":8s}')
import datetime

# help('FORMATTING')
user_1 = {
    'pin' : 0000,
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

print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')

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