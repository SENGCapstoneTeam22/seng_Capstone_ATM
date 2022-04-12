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
    date = str(datetime.date.today())
    # Display user-name & date
    print(f"\n\n{user['last']:8s}{user['first']:14s} {date:8s}")
    # Display Divider
    print('-' * 35)

    # User Commands
    print(f'{"0 : Accounts":20} {"1 : Deposit":16s}')
    print(f'{"2 : Transfer":20s} {"3 : Settings":16s}')
    print(f'{"4 : Products":20s} {"5 : Exit":16s}\n')

    # Ask User for a Command
    user_input = input('Enter your selection:\n').strip().lower()
    print('\n\n\n\n\n')

    if user_input != 'exit':
        if user_input == '0' or user_input == 'accounts':
            # Display user-name & date
            print(f'{user["last"]:8s} {user["first"]:14s} {date:8s}')
            # Display Divider
            print('-' * 35)

            # User Commands
            print(f'{"Current Balance":<15} : {user["debit"]:>10}\n')
            print(f'{"1 : View Transactions":25s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":25s} {"5 : Exit":16s}\n')

            # Ask User for Next Command
            user_input = input('Enter your selection:\n')

            # If the User chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(accounts)

        if user_input == '1' or user_input == 'deposit':
            # Display user-name & date
            print(f"{user['last']:8s}{user['first']:14s} {date:8s}")
            # Display Divider
            print('-' * 35)

            # User Commands
            print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
            print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')

            # Ask User for Next Command
            user_input = input('Enter your selection:\n')

            # If the User chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(accounts)

        if user_input == '2' or user_input == 'transfer':
            # Display user-name & date
            print(f"{user['last']:8s}{user['first']:14s} {date:8s}")
            # Display Divider
            print('-' * 35)

            # User Commands
            print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
            print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')

            # Ask User for Next Command
            user_input = input('Enter your selection:\n')

            # If the User chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(accounts)

        if user_input == '3' or user_input == 'settings':
            # Display user-name & date
            print(f"{user['last']:8s}{user['first']:14s} {date:8s}")
            # Display Divider
            print('-' * 35)

            # User Commands
            print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
            print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')

            # Ask User for Next Command
            user_input = input('Enter your selection:\n')

            # If the User chooses the 'EXIT' command, restart/re-run the program.
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

            # Ask User for Next Command
            user_input = input('Enter your selection:\n')

            # If the User  chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '0' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                print('\n\n\n\n\n')
                # start_atm()
                run_user_program(accounts)
    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   Thank you for using College Bank ATM!                  *")
    print("*                                                                          *")
    print("****************************************************************************")


def start_atm():
    # WELCOME MESSAGE (START OF PROGRAM)
    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   Welcome to College Bank ATM!                           *")
    print("*                                                                          *")
    print("****************************************************************************")

    # Request User-Account PIN
    entered_pin = (input('Please Enter Your PIN Below to Get Started: \n')).strip()

    # Check entered PIN against all Account-PIN's by looping
    for account in accounts.values():
        # print(account['pin'])
        pin_ref = account['pin']

        # If PIN's match, run User_Program(). Passing the individual account data of matching PIN.
        if int(pin_ref) == int(entered_pin):
            # print(account)
            # Run user program/function
            run_user_program(account)
        elif int(entered_pin) == 0000:
            # Run admin program/function
            run_admin_program(accounts)

            # TODO: COME UP W/ A WAY TO CLOSE PROGRAM ON COMMAND (EXIT FUNCTION)

            # if int(entered_pin) == pin:
            #     run_user_program(account)
            # elif entered_pin == 0000:
            #     print('admin pin entered')
            # else:
            #     print('Sorry Invalid PIN, Try Again...')


start_atm()
