count = int(input("How many day's Temperature: "))
temp = []
for i in range(count):
    day = int(input(f"Day {i+1}'s high Temperature: "))
    temp.append(day)

print(temp, "is the list of temperature")
avg = sum(temp) / len(temp)
print(avg, "is the average temperature")

abv_avg = []
for j in range(len(temp)):
    if temp[j] > avg:
        abv_avg.append(temp[j])
print(abv_avg, "is the list of temperature above average")