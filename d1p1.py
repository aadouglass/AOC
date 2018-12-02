#   load list of integers to sum in for loop
frequencies = open("C:\\Users\\AndrewDesktop\\Advent\\freq.txt").read().split()

#   loop through elements of frequencies array and sum together for answer to the advent calendar.
i = 0
for x in range(len(frequencies)): 
    freq = frequencies[x]
    i = i + int(freq)
print(i)
