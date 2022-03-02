# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# print(f'{"Player Name":16s} {"Goals":8s}')
# print('-' * 24)
#
# print(f'{"Maria":16s} {"22":8s}')
# print(f'{"Edward":16s} {"21":8s}')
help('FORMATTING')
user_1 = {
    'first': 'Matulu',
    'last': 'Shakur',
    'dob': '00/00/00',
    'debit': 1386,
    'saving': 247,
    'credit': 900,
    'credit_used': 113,
    'address': '1884 ECU Blvd.',
    'state': '1884 ECU Blvd.'
}


print(f"{user_1['last']:8s}{user_1['first']:8s} {'Current Date':8s}")
print('-' * 29)

print(f'{"0 : Check Balance":20} {"1 : Deposit":16s}')
print(f'{"2 : Make Withdraw":20s} {"3 : Option 4":16s}')
print(f'{"4 : Edit Profile":20s} {"5 : Exit":16s}')