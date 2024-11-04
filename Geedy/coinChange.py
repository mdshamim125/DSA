"""এই সমস্যায় একটি নির্দিষ্ট পরিমাণ অর্থ তৈরি করতে কতগুলি কয়েন লাগবে তার সর্বনিম্ন সংখ্যা বের করতে হয়।
"""


def minCoins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if(amount>=coin):
            count += amount // coin
            amount %= coin
    if(amount == 0):
        return count
    else:
        return -1

coins = [1, 5, 10, 25]
amount = 63
result = minCoins(coins, amount)
if(result != -1):
    print("number of coins: ", result)
else:
    print("It is not possible to make this money.")