import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
result = []

for i in range(8):
    b = random.choice(boys)
    g = random.choice(girls)
    boys.remove(b)
    girls.remove(g)
    
    result.append((b, g))
    
for family in result:
    print(family)