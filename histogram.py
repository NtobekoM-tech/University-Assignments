"""
Program that takes in a list of marks (separated by spaces), 
and outputs a histogram representation of the marks according to the mark categories at a UCT:
1 : 75+, 2+: 70-75, 2-: 60-70, 3: 50-60, F: <50

Ntobeko Mhlongo
19 April 2024
"""
marks_input = input("Enter a space-separated list of marks:\n")
marks = [int(mark) for mark in marks_input.split()]
    
counters = [0, 0, 0, 0, 0]
    
for mark in marks:
    if mark < 50:
        counters[4] += 1
    elif 50 <= mark < 60:
        counters[3] += 1
    elif 60 <= mark < 70:
        counters[2] += 1
    elif 70 <= mark < 75:
        counters[1] += 1
    else:
        counters[0] += 1


categories = ["1 ", "2+", "2-",  "3 ", "F "]
for i in range(len(categories)):
    category = categories[i]
    count = counters[i]
    print(category+'|'+('X' * count))
