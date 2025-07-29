row1 = ["x", "x", "x"]
row2 = ["x", "x", "x"]
row3 = ["x", "x", "x"]
map = [row1,row2,row3]
pos = input("where do you want to put the treasure? ")
horizontal = int(pos[0])
vertical = int(pos[1])
selected_row = map[vertical - 1]
selected_row[horizontal -1] = "T"
print(f"{row1}\n{row2}\n{row3}")
