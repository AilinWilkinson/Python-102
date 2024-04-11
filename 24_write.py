with open('./texs.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')

# el permiso de r+ es leer y escribir agregando en cambio el de w+ sobre escribe el archivo