from persona import Persona
from persona import Empleado

#programador = Persona()
#programador.nombre  ='Freddy'
#programador.edad    =18
#programador.mostrar_datos()

programador = Persona('Freddy', 18)
técnico = Persona('David', 39)

#programador.mostrar_datos()
#print('-- ' * 8)
#técnico.mostrar_datos()

print(programador.__str__())
programador.set_edad(19)
print(programador.get_edad())
print('-- ' * 8)
print(técnico.__str__())

print('-- ' * 8)

empleado = Empleado('Peñafiel', 38, 2000)

print(empleado.__str__())

print('-- ' * 8)

empleado.detalle_empleado()
