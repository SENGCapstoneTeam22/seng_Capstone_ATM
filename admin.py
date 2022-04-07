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
            # help('Need to figure out how to take information from the accounts dictionary to display here')
            if user_input == '0' or user_input == "view users":
                # Display user-name & date
                print(f"{' Users':20s} {date:>25}")

                # Display Divider
                print('-' * 50)
                print(' Mutulu Shakur\n','Jacques Kallis\n','Ricky Bobby\n','Total accounts = 3\n')

            # If the user chooses the 'EXIT' command, restart/re-run the program.
            if user_input == '5' or user_input == 'exit':
                # Restart/re-run the program to get back to Main Menu
                run_admin_program(accounts)

        if user_input == '1' or user_input == 'transactions':
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

    print('\n\nThank you for using XYZ Bank. Have a great day!')