'''
we are going learn Set methods.
'''

S = {1, 2, 3, 4, 5}

print(type(S)) # output: <class 'set'>

S.add(6)

print(S) # output: {1, 2, 3, 4, 5, 6}

S.pop() # this will remove one random value.

print(S) 

Set1 = {1,2, 3, 4, 5}
Set2 = {4, 5, 6, 7}

print("Set1 : ", Set1)
print("Set2 : ", Set2)

unionResult = Set1.union(Set2)

print("Union of Set1 & Set2 result ",unionResult)

intersectionResult = Set1.intersection(Set2)

print("Intersection of Set1 & Set2 result ",intersectionResult)