#리스트 Shuffle하기 : 기본

import random
import math

card = [1,2,3,4,5]
tmp = []

for x in card:
    tmp = tmp + [[random.random(), x]]

tmp.sort()

shuffleCard = []
for y in tmp:
    shuffleCard = shuffleCard + [y[1]]

print(shuffleCard)