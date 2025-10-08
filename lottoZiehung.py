import random


statistik = {};
for i in range(1, 46):
    statistik[i] = 0;


def ziehung():
    for i in range(1,46):
        zahlen.append(i);

    for i in range(0,6):
        randomNumber = random.randrange(0,len(zahlen)-i);
        element = zahlen.pop(randomNumber);
        zahlen.append(element);
        statistik[element] = statistik[element]+1;


for i in range(1000):
    zahlen = [];
    ziehung()


print(statistik)
