#    set - set is a collection of item he is store unique element . it is a unorder collection of element 

#  set operation -
#    - union
#    - intersection
#    - different 

set1 = {1,3,4,8,6,10}
set2 = {2,3,5,8,9,6}

#  union of set is

mark_union = set1.union(set2)

print("union of element" , mark_union)

mark_intersection = set1.intersection(set2)

print("intersection of element is " , mark_intersection)

mark_different = set1.difference(set2)

print("different between two set" , mark_different)


# add a new value in set

set1.add(25)

print(set1)

# remove element from set

set1.remove(25)

print(set1)

# clear all set value

set1.clear()

print(set1)