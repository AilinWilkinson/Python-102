def message_creator(text):
   # Escribe tu solución 👇
  respuesta= ''
  if text == 'computadora':
    respuesta = 'Con mi computadora puedo programar usando Python'

  elif text == 'celular':
    respuesta = 'En mi celular puedo aprender usando la app de Platzi'

  elif text == 'cable':
    respuesta = '¡Hay un cable en mi bota!'  
  
  else:
    respuesta = 'Artículo no encontrado'
  
  return respuesta

text = 'computadora'
response = message_creator(text)
print(response)