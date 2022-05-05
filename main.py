# Generates bids in three different distributions


import numpy as np


### Find max: Basically a Max function to find highest bids.
def findMax(bids):
    maxBid = max(bids)
    print("Max is " + str(maxBid))

    return maxBid


### FindPrice1 will be my program to find the best bids.
def findPrice1(bids):
    print("In findprice")
    print("Bids: " + str(bids))

    ### Assuming
    ### Slot 1: 500 Clicks, \
    # Slot 2: 300 Clicks,
    # Slot 3:100 Clicks.

    ### Trackers: bidsX for Max 3, BidsY to calculate VCG, and p0 to calculate first price for VCGs.
    bidsX = bids.tolist()  # Copy of Bids as a list For processing Top 3 bids:
    bidsY = bids.tolist()  # Copy of Bids as a list For processing VCG payments.
    p0 = findPrice2(bidsY)  ### Original Price (VCG)

    ### 1: FirstBid
    topBid = findMax(bidsX)  # Bidder 1 / highest bid
    bidsX.remove(topBid)  # Removes Highest bid to find 2nd

    bidsY = bids.tolist()  # Copy of Bids as a list For processing VCG payments.
    bidsY.remove(topBid)  # Removes Highest bid to find 2nd
    p1 = p0 - findPrice2(bidsY)  ### 1st Price (VCG)

    ### 2: SecondBid
    secondBid = findMax(bidsX)  # Bidder 2 / Second highest bid
    bidsX.remove(secondBid)  # Removes Highest bid to find 2nd

    bidsY = bids.tolist()  # Copy of Bids as a list For processing VCG payments.
    bidsY.remove(secondBid)  # (BidsY copy)
    p2 = p0 - findPrice2(bidsY)  ### 2nd Price (VCG)

    ### 3: ThirdBid
    thirdBid = findMax(bidsX)  # Bidder 2 / Second highest bid
    bidsX.remove(thirdBid)  # Removes Highest bid to find 2nd

    bidsY = bids.tolist()  # Copy of Bids as a list For processing VCG payments.
    bidsY.remove(thirdBid)  # Removes Highest bid to find 2nd
    p3 = p0 - findPrice2(bidsY)  ### 1st Price (VCG)

    print("\n FINAL RESULTS: p0: " + str(p0) + ", p1: " + str(p1) + ", p2: " + str(p2) + ", p3: " + str(p3))
    print(p0)


### FindPrice2: just a inner function to handle the prices for VCG
### S1, S2, and S3 Represent the amount of Slots expected, as 500, 300, and 100 clicks respectively.
def findPrice2(bids, S1=500, S2=300, S3=100):
    print("\nIn findprice2")
    print("Bids: " + str(bids))

    ### Assuming
    ### Slot 1: 500 Clicks, \
    # Slot 2: 300 Clicks,
    # Slot 3:100 Clicks.

    bidsX = bids  # Copy of Bids. (Already made a list since of the wrapper function, so we can use remove without worry. )

    # findPrice2(bidsX)
    topBid = findMax(bidsX)  # Bidder 1 / highest bid
    bidsX.remove(topBid)  # Removes Highest bid to find 2nd

    secondBid = findMax(bidsX)  # Bidder 2 / Second highest bid
    bidsX.remove(secondBid)  # Removes Highest bid to find 2nd

    thirdBid = findMax(bidsX)  # Bidder 2 / Second highest bid

    price = S1 * topBid + S2 * secondBid + S3 * thirdBid
    print("Finalprice: " + str(price))
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
    print("\nMy Code Begins")
    findPrice1(normalBids)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
