file = open('./text.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close()
#en el siguiente no hay que preocuparse por cerrar el archivo
with open('./text.txt') as file:
  for line in file:
    print(line)