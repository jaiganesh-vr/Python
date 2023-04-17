intervals = [(4, 5), (0, 2), (2, 7), (1, 3), (0, 4)]
intervals.sort(key=lambda x: x[1])

count = 0
end = 0
answer = []

for interval in intervals:
    if (end <= interval[0]):
        end = interval[1]
        count += 1
        answer.append(interval)

print("The maximum events a person can attend is : ", count)
print("List of intervals in which person will attend events : ", answer)