from report import *
from time import sleep


# This file starts the strategy report,
# which will be repeated in a circle

n = 0
# The number of repetitions
n_max = 500

while n < n_max:
    n += 1

    strategy_report()

    print('#'*100)
    print()
    sleep(30)
