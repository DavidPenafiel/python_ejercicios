from sys import argv

if len(argv) > 3 :
    Alumno = argv[1]
    Edad = int(argv[2])
    Estatura = float(argv[3])
    # 3 maneras de presentar datos con formato
    #print('Alumno: {} \nEdad: {} \nFunción: {}'.format(Alumno, Edad,Estatura))
    #print('Alumno: {a} \nEdad: {c} \nEstatura: {b} + {d}'.format(a = Alumno, b = Estatura, c = Edad, d = 1))
    print('Alumno: %s \nEdad: %i \nEstatura: %f'%(Alumno, Edad, Estatura))
else:
    print("no hay argumentos para devolver")

#si ejecuto:
# python ('C:\\Users\\david\\Documents\\Python Scripts\\06 Modularidad\\mod_sys_03.py', 'david', '39', '1.80')
#devuelve:
# david