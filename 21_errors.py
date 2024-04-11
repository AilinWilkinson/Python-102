# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) == 4 #solo continua si este condicional da verdadero

print('Hola 2')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')
#es una forma de parar el programa dada una excepción y enviar un mensaje al usuario
print('Hola 2')