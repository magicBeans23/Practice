import os

def fun(c):
    if c == 1:
        return 1
    elif c == 0:
        return 0
    else:
        return c+fun(c-1)

def arrangeCoins(coins):
    dict={}
    ctr = 1
    for c in coins:
        counter=0
        found=False
        while dict.get(counter) is not None:
            if c>dict.get(counter) and c<=dict.get(counter+1):
                print(counter)
                found=True
                break
            else: counter += 1
        if not found:
            #f = fun(counter)
            while fun(ctr) <= c:
                dict[ctr] = fun(ctr)
                ctr += 1
            print(ctr-1)




# Write your code here

if __name__ == '__main__':
    coins_count = int(input().strip())

    coins = []

    for _ in range(coins_count):
        coins_item = int(input().strip())
        coins.append(coins_item)

    arrangeCoins(coins)
