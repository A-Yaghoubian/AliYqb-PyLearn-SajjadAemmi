
n = int(input("How many students in programming class? "))
score_list = []

for i in range(n):
    score = float(input("Score: "))
    score_list.append(score)
    
print('AVG:', sum(score_list) / n)
print('MAX:', max(score_list))
print('MIN:', min(score_list))
