#for loop
scores = [40.0, 75.0, 100.0, 80.0]
total = 0
for score in scores:
    total += score

print(total)


#while loop
total = 0
i = 0
while i < len(scores):
    total += scores[i]
    i += 1
print(total)