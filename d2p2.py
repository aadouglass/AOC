box_codes = open("AoCd2").read().split()
box_a = []
box_b = []
full_match_len = 0
sim_match_len = 0
found = 0

# create the outer most loop to look at each box individually
for x in range(len(box_codes)):
# break the loops if we found our match
    if found == 1:
        break
    else:
	    full_match_len = len(box_codes[x])
	    sim_match_len = len(box_codes[x]) - 1
	    box_a = list(box_codes[x])
# loop through the same list to compare each element to each other
	    for y in range(len(box_codes)):
# break the loops if we found our match
	        if found == 1:
	            break
	        else:
	    	    box_b = list(box_codes[y])
	    	    box_mismatch_count = 0
	    	    box_match = ''
# compare each position in the box code to each other
	    	    for z in range(len(box_a)):
	    	        if x != y:
	    	            if box_a[z] == box_b[z]:
	    	    	    	box_match = box_match + box_a[z]
	    	    	    else:
	    	    	    	box_mismatch_count = box_mismatch_count + 1
	    	    	    	if box_mismatch_count > 1:
	    	    	    		break
# we have found our match, look no further!
	    	    	if len(box_match) == sim_match_len:
	    	    	    print(box_match)
	    	    	    found = 1
