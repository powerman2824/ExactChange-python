num = 266

dollars = num / 100
dollars = int(dollars)

change = num % 100

quaters = change / 25
quaters = int(quaters)

change = num % 25

dimes = change / 10
dimes = int(dimes)

change = num % 10

nickels = change / 5
nickels = int(nickels)

change = num % 5

pennies = change / 1
pennies = int(pennies)

change = num % 1

if dollars > 0:
    if dollars == 1:
        print(f'{dollars} Dollar')
    else:
        print(f'{dollars} Dollars')
if quaters > 0:
    if quaters == 1:
        print(f'{quaters} Quater')
    else:
        print(f'{quaters} Quaters')
if dimes > 0:
    if dimes == 1:
        print(f'{dimes} Dime')
    else:
        print(f'{dimes} DImes')
if nickels > 0:
    if nickels == 1:
        print(f'{nickels} Nickel')
    else:
        print(f'{nickels} Nickels')
if pennies > 0:
    if pennies == 1:
        print(f'{pennies} Penny')
    else:
        print(f'{pennies} Pennies')
# print(f'{dollars}:{quaters}:{dimes}:{nickels}:{pennies}')
