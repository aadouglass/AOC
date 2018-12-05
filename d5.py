input = list(open("C:\\Users\\andrewd\\Source\\Repos\\adoc\\d5.txt").read())

print("Initial length of input:", len(input))

set_deleted = 0
del_count = 0

while set_deleted < 1:
    del_check = 0
    for x in range(len(input)-1):
        if abs(ord(input[x]) - ord(input[x+1])) == 32:
            input.remove(input[x])
            input.remove(input[x])
            del_check = 1
            del_count = del_count + 2
            break
    if del_check == 0:
        set_deleted = 1
        
print("Number of characters deleted:", del_count)
print("Characters remaining:", input)
print("Number of characters remaining:", len(input))
