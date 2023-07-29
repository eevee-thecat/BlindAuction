def find_highest_bidder(bidding_record):
    highestBid = 0
    highestBidder = []
    for bidder in bidding_record:
        if bidding_record[bidder] > highestBid:
            highestBidder = [bidder]
            highestBid = bidding_record[bidder]
        elif bidding_record[bidder] == highestBid:
            highestBidder.append(bidder)

    return highestBidder

def getBids():
    bidding_records = {}
    other_bidders = "yes"
    while other_bidders == "yes":
        name = input("What is your name? ")
        bid = int(input("What's your bid? $"))
        invalid_bid = True

        #repeats request for bidding price if offer is less than 0
        while invalid_bid:
            if bid < 0:
                print("You cannot enter a negative bid. Try again.")
            else:
                invalid_bid = False

        bidding_records[name] = bid
        invalid_answer = True
        while invalid_answer:
            other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
            if other_bidders == "yes" or other_bidders == "no":
                invalid_answer = False
            else:
                print("That is not a valid input.")

    return bidding_records

def breakTie(tied_bidders):
    bidding_records = {}
    for bidder in tied_bidders:
        bid = int(input(f"{bidder}, what is your new bid? $"))
        bidding_records[bidder] = bid

    return bidding_records

def main():
    bidding_records = getBids()
    winningBidder = find_highest_bidder(bidding_records)
    tied = False

    if len(winningBidder) > 1:
        tied = True

    while tied:
        print("There was a tie. Bidding will continue until the tie is broken.")
        bidding_records = breakTie(winningBidder)
        winningBidder = find_highest_bidder(bidding_records)
        if len(winningBidder) == 1:
            tied = False

    highestBid = bidding_records[winningBidder[0]]
    print(f"The winner is {winningBidder[0]} with a bid of ${highestBid}.")

print("Welcome to the secret auction program.")
main()
