box_codes = open("AoCd2").read().split()
box_a = []
box_b = []
match_length = 0
for x in range(len(box_codes)):
  match_length = len(box_codes[x]) - 1
  box_a = list(box_codes[x])
  for y in range(len(box_codes)):
    box_b = list(box_codes[y])
    box_mismatch_count = 0
    box_match = ''
    for z in range(len(box_a)):
      if box_a[z] == box_b[z]:
        box_match = box_match + box_a[z]
      elif ord(box_a[z]) - ord(box_b[z]) == 1 or ord(box_a[z]) - ord(box_b[z]) == -1:
        box_mismatch_count = box_mismatch_count + 1
        if box_mismatch_count > 1:
          break
      print(box_match)
      if match_length == len(box_match):
        print(box_match)
