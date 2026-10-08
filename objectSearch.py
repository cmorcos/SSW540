objects = ["apple", "banana", "apple", "orange", "grape", "banana"] # test list including duplicates

unique_objects = [] # list to store uniques

for item in objects:    # loop through objects in list
    if objects.count(item) == 1:    # check if object only shows up once
        unique_objects.append(item) # if yes then = unique

print("Unique objects:", unique_objects)    # print unique objects

# github link: 