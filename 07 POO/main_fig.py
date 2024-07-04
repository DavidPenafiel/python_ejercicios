from tarea_figura import Rectangulo, Circulo, probar_figura

def main():
    while True:
        menu = """
        OBTENER ÁREA Y PERÍMETRO DE FIGURAS GEOMÉTRICAS
        
        1 - Rectángulo
        2 - Círculo
        3 - Salir
        Ingrese una opción: """
        opcion = input(menu)
        
        if opcion == '1':
            base = float(input('Ingrese base: '))
            altura = float(input('Ingrese altura: '))
            r = Rectangulo(base, altura)
            probar_figura(r)
        elif opcion == '2':
            radio = float(input('Radio: '))
            c = Circulo(radio)
            probar_figura(c)
        elif opcion == '3':
            print('Sistema finalizado')
            break
        else:
            print('Elija una opción correcta')
    

if __name__ == '__main__':
    main()