import datetime
from admin import run_admin_program
from account_holders import accounts


# help('FORMATTING')


def run_user_program(user):
    """
    THIS FUNCTION IS THE USER PROGRAM.
    After the PIN is verified, this program will run.
    The User Object/Dictionary is passed into this function to be used for CRUD.
    Updated
    """
    date = str(datetime.date.today())
    # Display user-name & date
    print(f"\n\n{user['last']:8s}{user['first']:14s} {date:8s}")
    # Display Divider
    print('-' * 35)

    # User Commands
    print(f'{"0 : Accounts":20} {"1 : Deposit":16s}')
    print(f'{"2 : Withdraw":20s} {"4 : Products":16s}') # Changed "Transfer" to "Withdraw"
    print(f'{"5 : Exit":20s}\n')

    # Ask User for a Command
    user_input = input('Enter your selection:\n').strip().lower()
    print('\n\n\n\n\n')

    if user_input != 'exit':

        if user_input == '0' or user_input.lower() == 'accounts':
            # Display user-name & date
            print(f'{user["last"]:8s}, {user["first"]:14s} {date:8s}')
            # Display Divider
            print('-' * 35)

            # User Commands
            print(f'{"Current Balance":<15} : {user["debit"]:>10}\n')
            # print(f'{"1 : View Transactions":25s} {"3 : Credit":16s}') # REMOVE
            print(f'{"1 : Checking":25s} {"2 : Saving":16s}')
            print(f'{"3 : Profile":25s} {"4 : Exit":16s}\n')

            # Ask User for Next Command
            user_input = input('Enter your selection:\n')
            # If the User chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '1' or user_input.lower() == 'checking':

                # Print USER DEBIT TRANSACTIONS
                print(f"{user['first']:^10}{user['last']:<50}")
                print(f"{'Checking':^80}\n")
                print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
                print('-' * 80)
                for transaction_ in user['debit_transactions']:
                    # print(transaction_)
                    print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
                          f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
                print()

            if user_input == '2' or user_input == 'saving':

                # Print USER SAVING TRANSACTIONS
                print(f"{user['first']:^10}{user['last']:<50}")
                print(f"{'Savings':^80}\n")
                print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
                print('-' * 80)
                for transaction_ in user['savings_transactions']:
                    # print(transaction_)
                    print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
                          f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
                print()

                # If the User chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '3' or user_input == 'profile':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(user)

            # If the User chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '4' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                print("****************************************************************************")
                print("*                                                                          *")
                print("*                   Thank you for using College Bank ATM!                  *")
                print("*                                                                          *")
                print("****************************************************************************")
                quit()

        if user_input == '1' or user_input == 'deposit':
            # Display user-name & date
            print(f"{user['last']:8s}, {user['first']:14s} {date:8s}")
            # Display Divider
            print('-' * 35)

            # User Commands
            print(f'{"0 : Checking":20} {"1 : Saving":16s}')
            print(f'{"2 : Back":20} {"3 : Exit":16s}\n')

            # Ask User for Next Command
            user_input = input('Enter your selection:\n')
            if user_input == '0' or user_input == 'checking':
                #deposit to checking INCOMPLETE
                print(f'{"How much would you like to deposit?":10} {"Enter amount:":16s}')
                deposit_amount = float(input())
                deposit_answer=input(('Are you done? y/n\n'))
                if deposit_answer == 'y':
                    #quit
                    print("Current Balance:",deposit_amount)
                    quit()
                if deposit_answer == 'n':
                    #return to profile
                    print("Current Balnce:", deposit_amount)
                    print('Returning to profile')
                    run_user_program(user)
                else:
                    #invalid answer quit
                    print("Invalid Answer... Forcing Exit...\n\n")
                    print("****************************************************************************")
                    print("*                                                                          *")
                    print("*                   Thank you for using College Bank ATM!                  *")
                    print("*                                                                          *")
                    print("****************************************************************************")
                    quit()
            if user_input == '1' or user_input == 'saving':
                #deposit to saving INCOMPLETE
                print(f'{"How much would you like to deposit?":10} {"Enter amount:":16s}')
                deposit_amount1 = float(input())
                deposit_answer1 = input(('Are you done? y/n\n'))
                if deposit_answer1 == 'y':
                    print("Current Balance:", deposit_amount1)
                    quit()
                if deposit_answer1 == 'n':
                    #return to profile
                    print('Returning to profile')
                    run_user_program(user)
                else:
                    #Force exit due to invalid answer
                    print("Invalid Answer... Forcing Exit...\n\n")
                    print("****************************************************************************")
                    print("*                                                                          *")
                    print("*                   Thank you for using College Bank ATM!                  *")
                    print("*                                                                          *")
                    print("****************************************************************************")
                    quit()
            # restart/re-run the program.
            if user_input == '2' or user_input == 'back':
                run_user_program(user)

            # If the User chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '3' or user_input == 'exit':
                # Exit program
                print("****************************************************************************")
                print("*                                                                          *")
                print("*                   Thank you for using College Bank ATM!                  *")
                print("*                                                                          *")
                print("****************************************************************************")
                quit()

        if user_input == '2' or user_input == 'Withdraw': # Replaced "Transfer" with "Withdraw"
            # Removed print functions that was implemented before.
            print(f"Which account would you like to withdraw funds from?\n")

            # User Commands | Removed Deposit, Credit and Profile selections.
            print(f'{"1 : Checking":20} {"2 : Saving":16s}')
            print(f'{"3 : Exit":16s}\n')

            # Start of the withdrawal process UNFINISHED STILL WORKING ON IT.
            user_input = input('Enter your selection:\n')
            if user_input == '1' or user_input == 'Checking':
                user_input = input('Enter a Withdraw Amount: $')

            # If the User chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_user_program(user)

        if user_input == '3' or user_input == 'settings':
            # Display user-name & date
            print(f"{user['last']:8s}, {user['first']:14s} {date:8s}")
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
                run_user_program(user)

        if user_input == '4' or user_input == 'products':
            # Display Divider
            print('-' * 35)

            print(f'{"Checking Interest :":<20} {"0.25% APY":>20}')
            print(f'{"Savings Interest :":<20} {"0.050% APY":>20}')
            print(f'{"Business Loan :":<20} {"3.89% APR":>20}')

            print(f'{"Mortgage :":<20} {"3.500% APR":>20}')
            print(f'{"Credit Card :":<20} {"9.99% APR":>20}')
            print(f'{"Personal Loan :":<20} {"3.16% APR":>20}')
            print(f'{"CD Interest :":<20} {"2.96% APR":>20}')

            print(f'{"Auto Loan :":<20} {"4.093% APR":>20}')
            print(f'{"Private Student Loan :":<20} {"3.16% APR":>18}\n')

            # Return Command
            print(f'{"0 : Return to Main Menu":20}\n')

            # Ask User for Next Command
            user_input = input('Enter your selection:\n')

            # If the User  chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '0' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                print('\n\n\n\n\n')
                # start_atm()
                run_user_program(user)
        #quit for user
        if user_input == '5' or user_input == 'exit':
            print("****************************************************************************")
            print("*                                                                          *")
            print("*                   Thank you for using College Bank ATM!                  *")
            print("*                                                                          *")
            print("****************************************************************************")
            quit()
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
        elif int(entered_pin) != 0000 or int(entered_pin) != int(pin_ref):
            #invalid pin for user/try again
            print("****************************************************************************")
            print("*                                                                          *")
            print("*                   Sorry invalid PIN :(                                   *")
            print("*               Do you want to try again? y/n                              *")
            print("*                                                                          *")
            print("****************************************************************************")
            person_answer = input('y/n    ')
            if person_answer =='y':
                print("****************************************************************************")
                print("*                                                                          *")
                print("*                   Welcome to College Bank ATM!                           *")
                print("*                                                                          *")
                print("****************************************************************************")
                entered_pin = (input('Please Enter Your PIN Below to Get Started: \n')).strip()
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
            if person_answer == 'n':
                #quit invalid answer attempts
                print("****************************************************************************")
                print("*                                                                          *")
                print("*                   Thank you for using College Bank ATM!                  *")
                print("*                                                                          *")
                print("****************************************************************************")
                break
            else:
                #break loop for invalid answer
                print("Invalid Answer... Forcing Exit...\n\n")
                print("****************************************************************************")
                print("*                                                                          *")
                print("*                   Thank you for using College Bank ATM!                  *")
                print("*                                                                          *")
                print("****************************************************************************")
                break

            # TODO: COME UP W/ A WAY TO CLOSE PROGRAM ON COMMAND (EXIT FUNCTION)

            # if int(entered_pin) == pin:
            #     run_user_program(account)
            # elif entered_pin == 0000:
            #     print('admin pin entered')
            # else:
            #     print('Sorry Invalid PIN, Try Again...')


start_atm()
