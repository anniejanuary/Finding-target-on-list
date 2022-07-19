list = [1,3,7,11,13,17,23]
target = 17

count = 0
for i in list:
    if i == target:
        print("Found the target at index: ", count)
        break
    else: 
        if count == len(list):
            print("Didn't find the target")
    count+=1
