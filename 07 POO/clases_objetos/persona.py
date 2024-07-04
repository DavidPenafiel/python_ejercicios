class Persona:
    __nombre = None
    __edad = None
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad = edad    
    #def mostrar_datos(self):
    #    print('Nombre:', self.nombre)
    #    print('Edad:', self.edad)
    def __metodo_privado(self):
        print('este es un método privado')
    
    def detalle_persona(self):
        print(self.__str__())

    def __str__(self):
        return f'Nombre: {self.__nombre}\nEdad: {self.__edad}'
    
    def llamar_medoto(self):
        #print("Nombre: ",self.nombre)
        self.__metodo_privado()

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad

class Cliente(Persona):
    pass

class Empleado(Persona):
    #__sueldo = 0
    def __init__(self, nombre, edad, sueldo):
        #super().__init__(nombre, edad)
        Persona.__init__(self, nombre, edad)
        self.__sueldo = sueldo
    
    def __str__(self):
        #return super().__str__() + f'\nSueldo: {self.__sueldo  }'
        return Persona.__str__(self) + f'\nSueldo: {self.__sueldo  }'

    def detalle_empleado(self):
        Persona.detalle_persona(self)    