s_height = input("input a list of student heights: ").split()
for n in range(0,len(s_height)):
     s_height[n] = int(s_height[n])
# print(s_height)
# sum = 0
# i = 0

# for height in s_height:
#     sum += height
#     i += 1
# print(f"sum of heights is {sum}.")
# print(f"number of students is {i}.")

# average = round(sum / i)
# print(average) 
max = 0
for height in s_height:
     if height >= max:
          max = height
print(f"the highest score is :{max}.")
     
