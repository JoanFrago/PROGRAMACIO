string = input()
string = list(string)
diccionario = {}

for elem in string:
        diccionario[elem] = 0
        for i in string:
            if elem == i:
                diccionario[elem] += 1

print(diccionario)