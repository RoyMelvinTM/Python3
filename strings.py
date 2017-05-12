#los String
my_string = "Hola mundo 'roy'"
my_string = '''Este es un salto de linea\ncomo este\ny como este jejej xD'''

course = "Python3"
alumno = "Roy"

#unir Strings 1ra forma
final_message = "este es el curso"+course+"por"+alumno
# 2da forma
final_message = "nuevo curso de %s por %s" % (course, alumno)
#3ra forma
final_message = "new curso {} por {}".format(course, alumno)
#print (my_string)
print (final_message)
