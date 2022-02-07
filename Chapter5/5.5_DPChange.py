'''
5.5 Dynamic Programing Change Problem 
input - an integer money and an array Coins = (coin1,..., coind)
output - the minimum numer of coins with demonimations Coins that changes money

Psudocode:
DPChange(money, Coins):
    MinNumCoins(0) ← 0
    for m ← 1 to money
        MinNumCoins(m) ← ∞
            for i ← 0 to |Coins| - 1
                if m ≥ coini
                    if MinNumCoins(m - coini) + 1 < MinNumCoins(m)
                        MinNumCoins(m) ← MinNumCoins(m - coini) + 1
    output MinNumCoins(money)


if you are are Coins[m-1], we can take as many instances of that coin i.e. count(Coins, m, money-Coins[m-1])
then you moce to Coins[m-2]. After moving to Coins[m-2], we can't move back and can't make choices for Coins[m-1] i.e. Count(Coins, m-1, money)
Finally have to find the total number of ways, so you ass these two possible choices i.e. count(Coins, m, money-Coins[m-1]) + count(Coins, m-1, money)


'./testcases/01_Coins/inputs/test4.txt '
'''


def ReadFile():
    with open('./datasets/dataset_609141_10.txt ', 'r') as f:
        data = f. readlines()
        money = int(data[0])
        values = data[1].strip()
        values = values.split(',')
        Coins= []
        for coin in values :
            coin = int(coin)
            Coins.append(coin)
    print (money, Coins)
    return (money, Coins)

def DPChange(money, Coins):
    minCoins = (money+1) *[0]
    for m in range (1,money+1):
        minCoins[m] = m+1
        for coin in Coins:
            if m >= coin:
                if minCoins[m-coin]+1 < minCoins[m]:
                    minCoins[m] = minCoins[m-coin]+1
    return minCoins[money]

inputs = ReadFile()
money = inputs[0]
Coins = inputs[1]


print(DPChange(money, Coins))