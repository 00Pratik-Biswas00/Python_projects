import os

dic = {}
finish_bid = False
winner = ""


def highest_bidder(record_bid):
    high_bid = 0
    for bidder in record_bid:
        bid_amount = record_bid[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"{winner} is placed the highest bid: {high_bid}")
    print(dic)


while not finish_bid:
    name = input("Name of the bidder: ")
    bid = int(input("Enter your bid: Rs. "))
    dic[name] = bid
    others = input("Is there any other bidder present? 'yes' or 'no'? -> ").lower()
    os.system('cls')
    if others == "no":
        finish_bid = True
        highest_bidder(dic)
