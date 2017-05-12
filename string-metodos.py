course = 'Curso'
my_string = 'Código Facilito'

'''METdOS DE FORMATOS --> cambiar el orden'''
result = '{a} de {b}'.format(a=course, b=my_string)
# minusculas
result = result.lower()
#mayusculas curso de codigo facilito
#result = result.upper()
#formato titulo
#result = result.title()

'''METDOS DE BUSQUEDA'''
pos = result.find('código')
count = result.count('c')

#new_string = result.replace('c', 'o')
new_string = result.split(' ')
print (pos)
print (count)
print (result[9])
print(new_string)
