from random import random
from xml.dom import INDEX_SIZE_ERR


import random

omikuji = ["大吉", "吉", "中吉","凶"]

index = random.randint(0, len(omikuji) - 1)

result = omikuji[index]

print(f"今日の運勢は...{result}")
