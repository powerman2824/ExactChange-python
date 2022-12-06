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

print(f'{dollars}:{quaters}:{dimes}:{nickels}:{pennies}')
