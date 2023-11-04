#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

class Bidder:
    def __init__(self, name, valuation):
        self.name = name
        self.valuation = valuation
        self.bids = []  # Store bids for each round

    def submit_bid(self, auction_type):
        if auction_type == 'first_price':
            self.bids.append(random.randint(1, self.valuation))
        elif auction_type == 'second_price':
            self.bids.append(random.randint(1, self.valuation))
        else:
            print("Invalid auction type")

class Auction:
    def __init__(self, bidders, auction_type):
        self.bidders = bidders
        self.auction_type = auction_type
        self.rounds = []
        self.num_rounds = 1

    def run(self):
        for round_num in range(self.num_rounds):
            self.run_single_round()
            self.rounds.append(self.bidders.copy())

    def run_single_round(self):
        for bidder in self.bidders:
            bidder.submit_bid(self.auction_type)

        self.determine_winner()

    def determine_winner(self):
        for bidder in self.bidders:
            if bidder.bids:
                if self.auction_type == 'first_price':
                    bidder.winner = max(bidder.bids)
                elif self.auction_type == 'second_price':
                    bids = bidder.bids.copy()
                    bids.remove(max(bids))
                    if bids:
                        bidder.second_highest_bid = max(bids)
                    else:
                        bidder.second_highest_bid = 0  # No second bid
                    bidder.winner = max(bidder.bids)
            else:
                bidder.second_highest_bid = 0
                bidder.winner = 0



    def announce_winner(self, round_num):
        print(f"Round {round_num} Results:")
        for bidder in self.bidders:
            print(f"{bidder.name}: Winning bid: {bidder.winner}")
            if self.auction_type == 'second_price':
                print(f"{bidder.name}: Second highest bid: {bidder.second_highest_bid}")

if __name__ == "__main__":
    num_bidders = 3
    bidders = [Bidder(f"Bidder {i+1}", random.randint(80, 150)) for i in range(num_bidders)]
    auction_type = 'second_price'  # Change to 'first_price' for a first-price auction
    num_rounds = 3

    auction = Auction(bidders, auction_type)
    auction.num_rounds = num_rounds

    for round_num in range(num_rounds):
        print(f"Running Round {round_num + 1}")
        auction.run_single_round()
        auction.announce_winner(round_num + 1)

    print("Auction Completed")


# In[ ]:




