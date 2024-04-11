import sys
print(sys.path)#lugar exacto de donde se esta ejecutando

import re#tiene que ver con expresiones regulares
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)
#que encuentre coincidencias

import time
timestamp = time.time()#hora actual para la computadora
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter) #saber la frecuencia de los numeros

#los modulos tambien se pueden crear