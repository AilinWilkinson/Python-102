set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar', 'ecua', 'pe'}) #union de conjuntos
print(set_countries)

# remove

set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
set_countries.discard('arg')# por si el elemento no este para que no lance error
print(set_countries)
set_countries.add('arg')
print(set_countries)
set_countries.clear() #vacia el conjunto
print(set_countries)
print(len(set_countries))