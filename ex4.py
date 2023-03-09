l1 = [1,2,4,4,5,6,4,3,424,46,5654,9]
a = []
def sth(aba):
    for i in range(len(l1)):
        a.append(l1[i]**aba)

sth(3)
print(a)


#-------------------------------------------------------------------------

def cub(nombres):
    llista=[]
    for i in nombres:
        llista.append(i**3)
    return llista

print(cub([1,5,3,5,6,75,645,657,65,9990]))