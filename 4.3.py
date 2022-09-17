from collections import Counter
your_data = [2, 7, 11, 13, 15, 17]
target = 9
data_counter = Counter(your_data)
for i in data_counter:
    if target - i in data_counter and (i != target - i or data_counter[target - i] > 1):
        print (i, target - i)
        break