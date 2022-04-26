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
    print('*******************************************************************')
    print('*                                                                 *')
    print('*                    Welcome Administrator                        *')
    print('*                                                                 *')
    print('*******************************************************************')

    # Welcome Message
    print(f'{"Please select your input":^45}')

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
                for member in accounts.values():
                    pin = member['pin']
                    first = member['first']
                    last = member['last']
                    dob = member['dob']
                    debit = member['debit']
                    savings = member['saving']
                    credit = member['credit']
                    credit_used = member['credit_used']
                    address = member['address']
                    state = member['state']

                    # Print user info from account_holders
                    print(f'\nPin : {pin}\nName : {first} {last}\nDob : {dob}\nDebit : {debit}\nSavings : {savings}\nCredit : {credit}\n'
                    f'Credit Used : {credit_used}\nAddress : {address}\nState : {state}\n')
                    # Restart admin program
                    run_admin_program(accounts)

            # Added the beginning of the "add user" function
            # FIXME I attempted to used precoded values to try and test the functionality. Error message reads "ValueError: dictionary update sequence element #0 has length 1; 2 is required"
            if user_input == '1' or user_input == "Add User":
                print(f"{' Please enter user info':20s} {date:>25}")
                print('-' * 50)
                for member in accounts:
                    name = "Billy Bob" #str(input())
                    accounts[name] = {}
                    pin = 4444 #int(input())
                    accounts[name]['pin'] =  pin
                    first = "Billy" #str(input())
                    accounts[name]['first'] = first
                    last = "Bob" #str(input())
                    accounts[name]['last'] = last
                    dob = "00/00/00" #str(input())
                    accounts[name]['dob'] = dob
                    debit = "1234" #int(input())
                    accounts[name]['debit'] = debit
                    saving = "1234" #int(input())
                    accounts[name]['saving'] = saving
                    credit = "1234" #int(input())
                    accounts[name]['credit'] = credit
                    credit_used = "4321" #int(input())
                    accounts[name]['credit_used'] = credit_used
                    address = "123 Rainbow Road" #str(input())
                    accounts[name]['address'] = address
                    state = "Alabama" #str(input())
                    accounts[name]['state'] = state
                    debit_transactions = []
                    accounts[name]["debit_transaction"] = debit_transactions
                    savings_transactions = []
                    accounts[name]["savings_transactions"] = savings_transactions
                    accounts.update(member)
                    # Restart admin program
                    run_admin_program(accounts)

            # Added the beginning of the "updated user" function
            # FIXME Same as before, inputting 2 triggers the system information menu as well as the print statement
            if user_input == '2' or user_input == "Updated Users":
                print(f"{' Please select User':20s} {date:>25}")
                print('-' * 50)
                # Restart admin program
                run_admin_program(accounts)


            # FIXME Command will iterate through the accounts dictionary, but requires three inputs from user, The program is looking through all of the users in the accounts dictionary and outputs the print statement for each one.
            if user_input == '3' or user_input == "Search Users":
                # Display the names of the users and their info  in the accounts dictionary
                # Used the template from account holders to create this, prints specified user information.
                print(f"{'Search user menu':20s} {date:>25}")
                print(f"{'Please type users first name':20s}")
                print('-' * 50)
                # Iterate through the accounts dictionary
                for member in accounts.values():
                    pin = member['pin']
                    first = member['first']
                    last = member['last']
                    dob = member['dob']
                    debit = member['debit']
                    savings = member['saving']
                    credit = member['credit']
                    credit_used = member['credit_used']
                    address = member['address']
                    state = member['state']
                    user = input().strip()
                    # Check input to see if it matches the "first" key in account.holders
                    if first == user:
                        # Print the all the information in the user dictionary of the user, using String Formatting.
                        print(
                            f'\nPin : {pin}\nName : {first} {last}\nDob : {dob}\nDebit : {debit}\nSavings : {savings}\nCredit : {credit}\n'
                            f'Credit Used : {credit_used}\nAddress : {address}\nState : {state}\n')
                        # Restart admin program
                        run_admin_program(accounts)

                # Display Divider
                print('-' * 50)
                date = str(datetime.date.today())
                print(f'{date:>80}')
            # Added the beginning of the "delete user" function
            if user_input == '4' or user_input == "Delete User":
                print(f"{' Please enter Users name and the Admin code':20s} {date:>25}")
                print('-' * 50)
                for member in accounts.values():
                    pin = member['pin']
                    first = member['first']
                    last = member['last']
                    dob = member['dob']
                    debit = member['debit']
                    savings = member['saving']
                    credit = member['credit']
                    credit_used = member['credit_used']
                    address = member['address']
                    state = member['state']
                    if input().strip() == member:
                        del member
                        # Restart admin program
                        run_admin_program(accounts)

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
            print(f'{"4 : Minimum":20s} {"5 : Return to Main Menu":20s}\n')

            # Ask Admin for Next Command
            user_input = input('Enter your selection:\n')
            if user_input == '0' or user_input == 'View All':
                print(f"\n\n{' Admin':20s} {date:>25}")
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
                    # print(f"{account['first']:60} {account['last']:20}")
                    print(f"{account['first']:^10}{account['last']:<50}")
                    print()
                    print('User Savings Transactions')
                    print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
                    print('-' * 80)
                    for transaction_ in account['savings_transactions']:
                        print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
                                  f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
                        print()
                for account in accounts.values():
                    print()
                        # print(f"{account['first']:60} {account['last']:20}")
                    print(f"{account['first']:^10}{account['last']:<50}")
                    print()
                    print('User Debit Transactions')
                    print(f"{'Date':^10} {'Debit/Credit':^16} {'Expense':^21} {'Amount':^20} {'Balance':^8}")
                    print('-' * 80)
                    for transaction_ in account['debit_transactions']:
                        print(f"{transaction_['date']:15} {transaction_['deb_cred']:15} {transaction_['expense']:15} "
                                  f"{transaction_['amt']:15}" f"{transaction_['remaining']:15}")
                        print()


                # Display Divider
                print('-' * 50)
            if user_input == '1' or user_input == 'View Last':
                print(f"\n\n{' Admin':20s} {date:>25}")

                # Display Divider
                print('-' * 50)
            if user_input == '2' or user_input == 'Average Balance':
                print(f"\n\n{' Admin':20s} {date:>25}")

                # Display Divider
                print('-' * 50)
            if user_input == '3' or user_input == 'Maximum':
                print(f"\n\n{' Admin':20s} {date:>25}")

                # Display Divider
                print('-' * 50)
            if user_input == '4' or user_input == 'Minimum':
                print(f"\n\n{' Admin':20s} {date:>25}")

                # Display Divider
                print('-' * 50)



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
