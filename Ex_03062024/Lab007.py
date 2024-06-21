#unpacking of tuple
a , b, c =(12,24,36)

t = (1,24,36)
#t.append # not possible as tuples are immutable
new_t = t + (4,)
print(new_t) # create new tuple