coins = [1,5,10,100]
price = 239
coins.reverse()
amount = 0

for i in range(len(coins)):
    if price>=coins[i]:
        while price>=coins[i]:
            price -= coins[i]
            amount += 1


print(amount)
