from ascii_art import art

logo = art.gavel

print(logo, '\n')
print("\nWelcome to the Secret Bidding Auction!\n")

auction = {}

def find_highest_bid(bidding_dict): 
    highest_bid = 0
    winner = ""
    for bidder in bidding_dict: 
        bid_amount = bidding_dict[bidder]
        if highest_bid < bid_amount: 
            highest_bid = bid_amount
            winner = bidder
    
    return(winner, highest_bid)


while True:
    name = input("Name: ")
    bid = int(input("Bid: "))
    auction[name] = bid
    choice = input("Any other bidders? Type 'yes' or 'no'").lower()

    if choice == "no": 
        print("\n" * 100)
        winner, highest_bid = find_highest_bid(auction)
        print(f"Winner is {winner}, with bid of {highest_bid}")
        break
    elif choice == "yes": 
        print("\n" * 100)
    else: 
        print("Invalid Input! Type 'yes' or 'no'")