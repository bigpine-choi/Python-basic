import random

n = random.randint(1, 50)

while True:
    x = input("맞혀 볼까요?")
    g = int(x)
    if g == n:
        print("정답!")
        break
    if g < n:
        print("업!")
    if g > n:
        print("다운!")