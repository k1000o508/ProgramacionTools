#Validaciones de todo tipo de variables 
class ValidacionesUniversales():
    #Validamos que el input sea un valor numerico
    def numval(x):
        
        it = False 
        while it == False:
            
            try:
                x = int(input( "▶ " ))
                it = True 
                return x 
            except (ValueError):
                print("Este valor solo puede ser numerico")
                it = False

    #El val_range funciona unicamente con variables tipo int
    def val_range(maxim,minin):

        while True:
            x = int(input(" ▶ "))

            if x >= maxim and x <= minin:            
                return x

            else:
                print("Su valor tiene que estar entre",minin ,"y",maxim ,sep = " ")


        # a = 19
        # print(a)
        # ranker(a,0,20)

    #Validamos que el input sea una cadena de texto explicitamente 
    def srtval(x):
        
        while True :
            print(x)
            x = input(" ▶ ")

            if x.isdigit() == False:
                for i in range(len(x)):
                    if x[i].isdigit() == True:

                        x=x[:i]+" "+x[i+1:]
                        print(x) 


                return x
                break
                
            else:

                print("No se pueden ingresar numeros")

            print(x)	

    #La funcion valida que los nombres esten cargados
    def val_strlist(x):
        
        while True:
            
            x = input(" ▶ ")

            if x.lower() in ap:
                return x
                break
                
            else:
                print("El apellido que ingreso no esta cargado\n Los nombres cargados son: \n ", ap, "\n Reingrese el apellido")			

    #Funcion para validar un si o un no
    def sn(z):
        
        while True:
            z = str(input( """Opciones:
                -Si
                -No 
                ▶ """ ))
            
            if z.upper() == "SI" or z.upper() == "NO" or z.upper() == "S" or z.upper() == "N":
                zup = z.upper()
                return zup[:1]
                break 
            else:
                print("Ingrese por respuesta un si o no")

    # Validamos que ningun valor se repita 
    def nrep(var):

        for i in range(len(var)-1):
            if var[i] == var[-1]:
                print("El valor ",var[-1], ",ya fue cargado")
                var.pop(-1)
                var.append(numval(var))
                print(var)
                nrep(var)

        # a = [2,4,5,6,7,8,2]

        # nrep(a)

    # Validamos que ningun valor se repita comparando 2 valores
    def nrep2(var,var2):

        print(var)
        print(var2)
        for i in range(len(var)-1):
            if var[i] == var[-1] and var2[i] == var2[-1]:
                var.pop(-1)
                var2.pop(-1)
                print("Ya fue cargado, en el indice, " ,i)
                var.append(input(numval(var)))
                var2.append(input(numval(var2)))
        return var, var2

        # a = [1,1,12,2,3,4,3]
        # b = [2,2,3,42,3,5,3]


        # nrep2(a,b)

    # Validamos que ningun valor se repita comparando 2 valores por lote y propietario
    def nrep2_lotxprop(var,var2,var_p,var2_p):

        print(var)
        print(var2)
        for i in range(len(var)-1):
            if var_p[i] == var[-1] and var2_p[i] == var2[-1]:
                var.pop(-1)
                var2.pop(-1)
                print("Ya fue cargado, en el indice, " ,i)
                var.append(input(numval(var)))
                var2.append(input(numval(var2)))
        return var, var2


    def ValidacionFecha():
        
        while True:
            try:
                print("Ingresa una fecha en el formato MM(mes): ")
                #Arreglar val_range 
                fechaM = val_range(12,1)
                datetime.strptime(fechaM,'%m')
                print("Fecha válida")
                break
            except ValueError:
                print("Fecha inválida")
            else:
                print("Fecha inválida")
        while True:
            try:
                fechaD = input("Ingresa una fecha en el formato DD(dia): ")
                datetime.strptime(fechaD,'%d')
                print("Fecha válida")
                break
            except ValueError:
                print("Fecha inválida")
        while True:
            try:
                #fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
                print("Ingresa una fecha en el formato YYYY(año): ")
                fechaY = val_range(2022,1900)
                #datetime.strptime(fecha, '%Y-%m-%d')
                datetime.strptime(fechaY, '%Y')
                print("Fecha válida")
                break
            except ValueError:
                print("Fecha inválida")

        fecha = fechaY + "-" + fechaM + "-" + fechaD
        fecha_val = reversed(fechaY) + "-" + reversed(fechaM) + "-" + reversed(fechaD)
        fecha_hoy = reversed(datetime.strptime(fechaY, '%Y') )+ reversed(datetime.strptime(fechaM,'%m')) + reversed(datetime.strptime(fechaD,'%d'))
        print(fecha_val +"\n" + fecha_hoy)

        reversed()

        print(fecha)
        return fecha
