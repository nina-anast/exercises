# ask for the input
cost = int(input('Provide me with the cost of the product: '))
# initialize the tax percentage
tax = 0.24
# calculate the initial cost of the product
initial_cost = cost/(1+tax)
# print the result
print('Its initial value was: ',initial_cost)