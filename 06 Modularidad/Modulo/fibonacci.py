# Módulo de números de Fibonacci
def fibo(n):
    a, b = 0, 1
    while a < n: 
        print(a, end=' ')
            # end lo que reemplaza es el cierre 
            # de print que ya no será un salto 
            # de línea sino un espacio
        a, b = b, a + b  
    print()
    # se hace un print vacío con salto de línea

def fibo2(n):
    resultado = []
    a, b = 0, 1
    while a < n: 
        resultado.append(a)
        a, b = b, a + b 
    return resultado

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        fibo(int(sys.argv[1]))
        
#se puede llamar de las siguientes formas
#python "C:\Users\david\Documents\Python Scripts\06 Modularidad\Modulo\fibonacci.py"(9)
#python "C:\Users\david\Documents\Python Scripts\06 Modularidad\Modulo\fibonacci.py"9
#python "C:\Users\david\Documents\Python Scripts\06 Modularidad\Modulo\fibonacci.py",9
#python "C:\Users\david\Documents\Python Scripts\06 Modularidad\Modulo\fibonacci.py" "9"
#python "C:\Users\david\Documents\Python Scripts\06 Modularidad\Modulo\fibonacci.py" '9'