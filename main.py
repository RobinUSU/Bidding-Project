# Generates bids in three different distributions


import numpy as np


### Find max: Basically a Max function to find highest bids.
def findMax(bids):
    maxBid = max(bids)
    # print("Max is " + str(maxBid))

    return maxBid


### FindPrice1 will be my program to find the best bids.
def findPrice1(bids, C1=500, C2=300, C3=100):
    # print("In findprice")
    # print("Bids: " + str(bids))

    ### Assuming
    ### Slot 1: 500 Clicks, \
    # Slot 2: 300 Clicks,
    # Slot 3:100 Clicks.

    ### Trackers: bidsX for Max 3, BidsY to calculate VCG, and p0 to calculate first price for VCGs.
    bidsX = bids.tolist()  # Copy of Bids as a list For processing Top 3 bids:
    bidsY = bids.tolist()  # Copy of Bids as a list For processing VCG payments.
    maxPrice = findPrice2(bidsY,C1, C2, C3)  ### Original Price (VCG)

    ### 1: FirstBid
    firstBid = findMax(bidsX)  # Bidder 1 / highest bid
    bidsX.remove(firstBid)  # Removes Highest bid to find 2nd

    # bidsY = bids.tolist()  # Copy of Bids as a list For processing VCG payments.
    # bidsY.remove(topBid)  # Removes Highest bid to find 2nd
    # p1 = p0 - findPrice2(bidsY)  ### 1st Price (VCG)

    ### 2: SecondBid
    secondBid = findMax(bidsX)  # Bidder 2 / Second highest bid
    bidsX.remove(secondBid)  # Removes Highest bid to find 2nd

    # bidsY = bids.tolist()  # Copy of Bids as a list For processing VCG payments.
    # bidsY.remove(secondBid)  # (BidsY copy)
    # p2 = p0 - findPrice2(bidsY)  ### 2nd Price (VCG)

    ### 3: ThirdBid
    thirdBid = findMax(bidsX)  # Bidder 2 / Second highest bid
    bidsX.remove(thirdBid)  # Removes Highest bid to find 2nd

    ### 4: FourthBid. For VCG
    fourthBid = findMax(bidsX)  # Bidder 2 / Second highest bid

    p1 = firstBid
    p2 = secondBid
    p3 = thirdBid
    p4 = fourthBid

    ### A1 pays P2 * (C1 - C2) + P3 * (C2 - C3) + P4 * (C3 - 0)
    a1Pays = p2 * (C1 - C2) + p3 * (C2 - C3) + p4 * (C3 - 0)
    ri1 = (a1Pays) / C1

    ### A2 pays P3 * (C2 - C3) + P4 * (C3 - 0)
    a2Pays = p3 * (C2 - C3) + p4 * (C3 - 0)
    ri2 = (a2Pays) / C2

    ### A3 pays P4 * (C3 - 0)
    a3Pays = p4 * (C3 - 0)
    ri3 = (a3Pays) / C3

    ### Conclusions:
    print("\n___ Price Results ___")
    print("A1 pays: $" + str(a1Pays) + ", wi = " + str(p1) + " at: " + str(ri1))
    print("A2 pays: $" + str(a2Pays) + ", wi = " + str(p2) + " at: " + str(ri2))
    print("A3 pays: $" + str(a3Pays) + ", wi = " + str(p3) + " at: " + str(ri3))
    print("(The original amount all agents were willing to pay could have been $" + str(maxPrice) + ")")

    print("\n___ Social Welfare ___")
    sw1 = C1 * (p1 - ri1)  # Social welfare 1-3
    sw2 = C2 * (p2 - ri2)
    sw3 = C3 * (p3 - ri3)
    print("| Ci  |  Wi  |  Ri  | Ci(Wi-Ri)  |")
    print("|" + str(C1) + "  | " + str(p1) + "  | " + str(round(ri1, 2)) + " | " + str(round(sw1, 2)) + "       |")
    print("|" + str(C2) + "  | " + str(p2) + "  | " + str(round(ri2, 2)) + " | " + str(round(sw2, 2)) + "       |")
    print("|" + str(C3) + "  | " + str(p3) + "  | " + str(round(ri3, 2)) + " | " + str(round(sw3, 2)) + "       |")
    print("Total Social welfare: " + str(sw1 + sw2 + sw3))

    # bidsY = bids.tolist()  # Copy of Bids as a list For processing VCG payments.
    # bidsY.remove(thirdBid)  # Removes Highest bid to find 2nd
    # p3 = p0 - findPrice2(bidsY)  ### 1st Price (VCG)
    #
    # print("\n FINAL RESULTS: p0: " + str(p0) + ", p1: " + str(p1) + ", p2: " + str(p2) + ", p3: " + str(p3))
    # print(p0)


### FindPrice2: just a inner function to handle the prices for VCG
### S1, S2, and S3 Represent the amount of Slots expected, as 500, 300, and 100 clicks respectively.
def findPrice2(bids, C1=500, C2=300, C3=100):
    # print("\nIn findprice2")
    # print("Bids: " + str(bids))

    ### Assuming
    ### Slot 1: 500 Clicks, \
    # Slot 2: 300 Clicks,
    # Slot 3:100 Clicks.

    bidsX = bids.copy()  # Copy of Bids. (Already made a list since of the wrapper function, so we can use remove without worry. )

    # findPrice2(bidsX)
    topBid = findMax(bidsX)  # Bidder 1 / highest bid
    bidsX.remove(topBid)  # Removes Highest bid to find 2nd

    secondBid = findMax(bidsX)  # Bidder 2 / Second highest bid
    bidsX.remove(secondBid)  # Removes Highest bid to find 2nd

    thirdBid = findMax(bidsX)  # Bidder 2 / Second highest bid

    price = C1 * topBid + C2 * secondBid + C3 * thirdBid
    #print("Finalprice: " + str(price))
    return (price)
    # bidsX.remove(thirdBid)  # Removes Highest bid to find 2nd


def random_snorm(n, mean=0, sd=1, xi=1.5):
    def random_snorm_aux(n, xi):
        weight = xi / (xi + 1 / xi)
        z = np.random.uniform(-weight, 1 - weight, n)
        xi_ = xi ** np.sign(z)
        random = -np.absolute(np.random.normal(0, 1, n)) / xi_ * np.sign(z)
        m1 = 2 / np.sqrt(2 * np.pi)
        mu = m1 * (xi - 1 / xi)
        sigma = np.sqrt((1 - m1 ** 2) * (xi ** 2 + 1 / xi ** 2) + 2 * m1 ** 2 - 1)
        return (random - mu) / sigma

    return random_snorm_aux(n, xi) * sd + mean


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    normalBids = np.round(np.random.normal(50, 5, 10), 1)
    normalBids.sort()
    print("Normal bids ", normalBids)
    skewedBids = np.round(random_snorm(10, 50, 10, 1.5), 1)
    skewedBids.sort()
    print("Skewed bids ", skewedBids)
    uniformBids = np.round(np.random.uniform(0.0, 100.0, 10), 1)
    uniformBids.sort()
    print("Uniform bids ", uniformBids)

    ### My code sections: begin
    print("\n{Code Begins}")
    # findPrice1(normalBids)

    findPrice1(
        np.array([0.50, 0.40, 0.30, 0.20, 0.10, 0.09, 0.09, 0.08, 0.08]))  # Debugging Test case with word lecture Data

    '''
    Part 1: 
    Consider controlling the following parameters:
    a.	Number of bidders and the value per click for each bidder.
    b.	Closeness of bids (or pattern of bids).  For example, (.5,.4,.3, .2, .1) or (.5, .45, .2, .1, .1)
    c.	Number of clicks expected for each slot (in decreasing order)
    d.	Number of advertising slots
    
    Come up with an interesting parameter combination.  
    
    '''

    ### For this, i wanted to try a test case for buyer's remorse to see some of the extreme gaps
    ### That VCG could have solving Buyer's remorse, where a buyer bids their true evaluation
    ### But the others value it much lower, while the highest slots could be a very costly mistake! I Thought this one was very interesting! 
    overBids = [2.50, 0.10, 0.09, 0.09, 0.08, 0.08]
    overBids.sort()
    print("Over bids ", normalBids)

    findPrice1(
        np.array(overBids), 50000, 3000, 100)  # Debugging Test case with word lecture Data
