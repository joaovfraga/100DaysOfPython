from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidders = {}
other_bidders = True

while other_bidders:

    name = input("What is your name? ")
    your_bid = int(input("What is your bid? $"))
    bidders[name] = your_bid

    more_bidders = input("Are there any other bidders? type 'yes' or 'no'\n")

    if more_bidders == "yes":
        bidders[name] = your_bid
    else:
        bidders[name] = your_bid
        highest_bidder = max(bidders.values())
        highest_bidder_name = ""
        for i in bidders:
            if bidders[i] == highest_bidder:
                highest_bidder_name = i
        print(f"The winner is {highest_bidder_name} with a bid of ${highest_bidder}.")
        other_bidders = False
