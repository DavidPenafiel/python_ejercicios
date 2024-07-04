## 'MANERAS DE IMPORTAR UN MÓDULO'

#importar el módulo con funciones por especificar:
#import fibonacci

#*importar solo ciertas funciones para usarlas directamente:
#from fibonacci import fibo, fibo2  

#lo mismo que en la primera con functiones directas, excepto las que inician con '_' :
#from fibonacci import *

import fibonacci as fiby

fiby.fibo(20)

print(fiby.fibo2(20))

from fibonacci import fibo as operacion

operacion(22)

#fibonacci.py 
print("información del módulo fibonacci")
print(dir(fiby))

#resultado
# información del módulo fibonacci
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fibo', 'fibo2']