def increment(x):
  return x + 1


increment_v2 = lambda x: x + 1

result = increment(10)
print(11)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
#esa f minuscula es importante para que se genere correctamente la concatenacion
text = full_name('nicolas', 'perez casas')
print(text)