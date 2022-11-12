import random
import time

for i in range(1, 51):
    time.sleep(0.1)
    numbe = "bid_" + str(i) + ": " + str(random.uniform(0, (i*10)))
    print(numbe)