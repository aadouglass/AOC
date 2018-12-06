import re
original_input = open("C:\\Users\\AndrewDesktop\\Advent\\d4.txt").read()
set_deleted = 0
del_count = 0
input = []
poly_counts = []
alpha = [['a','A'], ['b','B'], ['c','C'], ['d','D'], ['e','E'], ['f','F'], ['g','G'], ['h','H'], ['i','I'], ['j','J'], ['k','K'], ['l','L'], ['m','M'], ['n','N'], ['o','O'], ['p','P'], ['q','Q'], ['r','R'], ['s','S'], ['t','T'], ['u','U'], ['v','V'], ['w','W'], ['x','X'], ['y','Y'], ['z','Z']]
polyalph = []
for a in range(len(alpha)):
    temp = []
    polyalph.append(re.sub(alpha[a][0], '', original_input))
    polyalph[a] = list(re.sub(alpha[a][1], '', polyalph[a]))
    print(polyalph[a])

for z in range(len(polyalph)):
    set_deleted = 0
    print("Processing data without", alpha[z])
    input = polyalph[z]
    while set_deleted < 1:
        del_check = 0
        for x in range(len(input)-1):
            if abs(ord(input[x]) - ord(input[x+1])) == 32:
                del(input[x])
                del(input[x])
                del_check = 1
                del_count = del_count + 2
                break
        if del_check == 0:
            set_deleted = 1
    poly_counts.append(len(input))

smallest_poly = min(poly_counts)
print(smallest_poly)
print(poly_counts)
