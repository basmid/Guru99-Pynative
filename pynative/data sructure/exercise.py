#mijn versie
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

sett = list(set(first_set) & set(second_set))
print(sett)

for x in sett:
    if x in first_set:
        first_set.remove(x)

print(first_set)

# site versie
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element ", first_set)

