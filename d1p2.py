#   load list of integers to sum in for loop
freq_change = open("C:\\Users\\AndrewDesktop\\Advent\\freq.txt").read().split()

#   loop through elements of freq_change array and sum together then store each iteration as frequency history to find the first repeat.
i = 0
n = 0
freq_history = []
while n < 1:
    for x in range(len(freq_change)): 
        i = i + int(freq_change[x])
        freq_history.append(i)
        if freq_history.count(i) == 2:
            n = n + 1
            print(i)
            break
