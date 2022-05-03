'''
This program shows how you might read a file containing columns of data
separated by commas.
'''
 # File containing lines of the form "name,shares,price"


filename = 'tuples/portfolio.csv'

portfolio = []
with open(filename) as file:
    for line in file:
        row = line.split(',')
        name = row[0]
        shares = int(row[1])
        price = float(row[2])
        holding = (name, shares, price)
        portfolio.append(holding)


print(portfolio[0])
print(portfolio[1])
print(portfolio[1][1])
print(portfolio[1][2])

total = sum([shares * price for _, shares, price in portfolio])
print(total)