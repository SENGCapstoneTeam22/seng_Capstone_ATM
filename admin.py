import datetime


# help('FORMATTING')
def run_admin_program(accounts):
    """
    THIS FUNCTION IS THE USER PROGRAM.
    After the PIN is verified, this program will run.
    The User Object/Dictionary is passed into this function to be used for CRUD.
    """

    # help('FORMATTING')

    date = str(datetime.date.today())

    # Welcome Message
    print(f'{"Welcome Admin":^48}')

    # Display user-name & date
    print(f"{' Admin':20s} {date:>25}")

    # Display Divider
    print('-' * 50)

    # Admin Commands
    print(f'{"0 : Users":20} {"1 : Transactions":16s}')
    print(f'{"2 : System Info":20s} {"3 : Exit":16s}\n')

    # Ask Admin for Next Command
    user_input = input('Enter your selection:\n').strip().lower()
    print('\n\n\n\n\n')

    if user_input != 'exit':
        if user_input == '0' or user_input == 'users':
            # Display user-name & date
            print(f"\n\n{' Admin':20s} {date:>25}")

            # Display Divider
            print('-' * 50)

            # Admin Commands
            print(f'{"0 : View Users":20s} {"1 : Add User":16s}')
            print(f'{"2 : Updated Users":20s} {"3 : Search Users":16s}')
            print(f'{"4 : Delete User":20s} {"5 : Exit":16s}\n')
            # Display User Accounts






            # Ask Admin for Next Command
            user_input = input('Enter your selection:\n')
            # Display users and total number of users
            # Command now displays the users and their transaction history
            if user_input == '0' or user_input == "view users":
                # Display user-name & date
                print(f"{' Users':20s} {date:>25}")

                # Display Divider
                print('-' * 50)
                # Display the names of the users and their info  in the accounts dictionary
                # Used the template from account holders to create this, prints all users and their debit transactions

                date = str(datetime.date.today())
                print(f'{date:>80}')
                for account in accounts.values():
                    print()
                    #print(f"{account['first']:60} {account['last']:20}")
                    print(f"{account['first']:^10}{account['last']:<50}")
                    print()
                    print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
                    print('-' * 80)
                    for transaction_ in account['debit_transactions']:
                        print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
                        f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
                        print()


            # Added the beginning of the "add user" function
            # FIXME Error message reads "dictionary changed size during iteration"
            if user_input == '1' or user_input == "Add User":
                print(f"{' Please enter user info':20s} {date:>25}")
                print('-' * 50)
                for user in accounts:
                    name = str(input())
                    accounts[name] = {}
                    pin = int(input())
                    accounts[name]['pin'] = pin
                    first = str(input())
                    accounts[name]['first'] = first
                    last = str(input())
                    accounts[name]['last'] = last
                    dob = str(input())
                    accounts[name]['dob'] = dob
                    debit = int(input())
                    accounts[name]['debit'] = debit
                    saving = int(input())
                    accounts[name]['saving'] = saving
                    credit = int(input())
                    accounts[name]['credit'] = credit
                    credit_used = int(input())
                    accounts[name]['credit_used'] = credit_used
                    address = str(input())
                    accounts[name]['address'] = address
                    state = str(input())
                    accounts[name]['state'] = state
                    debit_transaction = []
                    savings_transactions = []


                    # Added the beginning of the "updated user" function
            # FIXME Same as before, inputting 2 triggers the system information menu as well as the print statement
            if user_input == '2' or user_input == "Updated Users":
                print(f"{' Please select User':20s} {date:>25}")
                print('-' * 50)


            # FIXME I can't seem to directly pull one users info from the dictionary.

            if user_input == '3' or user_input == "Search Users":
                # Display the names of the users and their info  in the accounts dictionary
                # Used the template from account holders to create this, prints all users and their debit transactions
                print(f"{' Users':20s} {date:>25}")
                print('-' * 50)
                account = input("Please enter user's name\n").strip()
                if account in accounts:
                    print(f'  {account}')
                    print()
                    print()


                    # Print Users first and last name
                    # Fixme Error Message states that "line 135, in run_admin_program print(f"{accounts['first']:^10}{accounts['last']:<50}")KeyError: 'first'"
                    
                    print(f"{accounts['first']:^10}{accounts['last']:<50}")
                    print()

                     # Print labels above transactions
                    print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
                    print('-' * 80)
                    for transaction_ in accounts['debit_transactions']:
                        # Print each debit transaction
                        print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
                                f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
                    print()




                # Display the names of the users and their info  in the accounts dictionary
                # Used the template from account holders to create this, prints all users and their debit transactions





            # Added the beginning of the "delete user" function
            if user_input == '4' or user_input == "Delete User":
                print(f"{' Please enter Users name and the Admin code':20s} {date:>25}")
                print('-' * 50)











            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_admin_program(accounts)

        if user_input == '1' or user_input.lower() == 'transactions':
            # Display user-name & date
            print(f"\n\n{' Admin':20s} {date:>25}")

            # Display Divider
            print('-' * 50)

            # Admin Commands
            print(f'{"0 : View All":20} {"1 : View Last":16s}')
            print(f'{"2 : Average Balance":20s} {"3 : Maximum":16s}')
            print(f'{"4 : Minimum":20s} {"5 : Flagged":16s}')
            print(f'{"6 : Return to Main Menu":20s}\n')

            # Ask Admin for Next Command
            user_input = input('Enter your selection:\n')
            print()


            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '6' or user_input == 'exit':
                    # Restart/re-run the program to get back to Main Menu
                    run_admin_program(accounts)

        if user_input == '2' or user_input == 'system info':
            # Display user-name & date
            print(f"\n\n{' Admin':20s} {date:>25}")
            # Display Divider
            print('-' * 50)

            user_balances = 0
            # Loop through account balances
            for account in accounts.values():
                # print(account['debit'])
                # Add each balance/amount to user_balances
                user_balances += int(account['debit'])

            # Display (Dummy) ATM Software Information
            print(f'{"Amount Dispensed :":30} {"?????":>16s}')
            print(f'{"Amount On Hand :":30} {user_balances:>16}')
            print(f'{"OS Version :":30} {"19.2":>16s}')
            print(f'{"Model :":30} {"R927":>16s}')
            print(f'{"Serial Number :":30} {"08DN385":>16s}')
            print(f'{"Data Storage Capacity :":30} {"64GB":>16s}')
            print(f'{"Wi-Fi Address :":29} {"A0:F3:C1:3B:6F:90":>16s}')
            print(f'{"Modem Firmware :":30} {"9.0.33":>16s}')
            print(f'{"Network :":30} {"Verizon":>16s}\n')

            # Return Command
            print(f'{"0 : Return to Main Menu":20}\n')
            # Ask Admin for Next Command
            user_input = input('Enter your selection:\n')
            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '6' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_admin_program(accounts)

        if user_input == '3' or user_input == 'exit':
            # Display user-name & date
            print(f"\n\n{' Admin':20s} {date:>25}")

            # Display Divider
            print('-' * 50)

            # Admin Commands
            print(f'{"0 : Checking":20} {"1 : Deposit":16s}')
            print(f'{"2 : Saving":20s} {"3 : Credit":16s}')
            print(f'{"4 : Profile":20s} {"5 : Exit":16s}\n')

            # Ask Admin for Next Command
            user_input = input('Enter your selection:\n')

    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   Thank you for using College Bank ATM!                  *")
    print("*                                                                          *")
    print("****************************************************************************")
