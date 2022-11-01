print("¡Bienvenido a la isla Tu misión sera encontrar el tesoro!")
opcion= int(input("Digita \n1. Derecha  \n2. Izquierda  \n3. abajo  \n"))
if(opcion==1):
    print("Caiste por un tunel \n")
    print("Estas en la playa \n")
    opcion= int(input("1. Selva  \n2. Barco Pequeño \n"))
    if(opcion==1):
        print("Tienes Hambre \n")
        opcion= int(input("1. Pescar  \n2. Seguir Caminando \n"))
        if(opcion==1):
            print("Eres atacado por un cocodrilo \n GAME OVER")
        elif(opcion==2):
            opcion= int(input("Sigue la secuencia \n U \n A \n G \n M \n ¿1. R - 2. T ? \n"))
            if(opcion==2):
                print("\n GAME OVER")
            elif(opcion==1):
                opcion= int(input("Sigue la secuencia \n H \n F \n D \n B \nZ  \nX  \n ¿ 1. U - 2. V? \n"))
                if(opcion==1):
                    print("GAME OVER")
                elif(opcion==2):
                    print("Encontraste el tesoro \n GANASTE!!")
                else:
                    print("Opcion incorrecta Vuelve a empezar")
    elif(opcion==2):
        print("Tromenta Electrica \n")
        print("GAME OVER!!")
    else:
        print("Opcion incorrecta Vuelve a empezar")
elif(opcion==2):
    opcion= int(input("1. Casa  \n2. Cueva \n"))
    if(opcion==1):
        print("Te ataca un animal salvaje\n  GAME OVER!")
    elif(opcion==2):
        print("Encuentras provisiones \n")
        opcion= int(input("1. Explorar la cueva  \n2. quedarte en la entrada \n"))
        if(opcion==1):
            print("Caminas por 20 minutos \n")
            opcion= int(input("1. Nadar  \n2. Descender por una montaña \n"))
            if(opcion==1):
                print("llegas a una casa echa de troncos \n Encuentras un cofre \n")
                opcion= int(input(" Sigue la secuencia para abrirlo  U\nD\nT\nC\nC\nS\nS\nO\nN\n ¿1.T - 2. D \n"))
                if(opcion==1):
                    print("GAME OVER!!")
                elif(opcion==2):
                    print("Encuentras una llave  y un mapa \n Llegas a la ubicación  \n")
                    opcion= int(input(" Cuanto es la mitad de 2 + 2= \n Digita\n ¿1. 4 ó  2. 2 \n"))
                else:
                    print("Opcion incorrecta vuelve a empezar")
                    if(opcion==1):
                        print("GAME OVER!!")
                    elif(opcion==2):
                        print("GANASTE!!")
                    else:
                        print("Opcion incorrecta vuelve a empezar")
            elif(opcion==2):
                print("Al final encuencuentras un cofre brillate\n")
                opcion= int(input(" 54 * 2 = Digita\n ¿1. 110 ó  2. 108 \n"))
                if(opcion==1):
                    print("GAME OVER!!")
                elif(opcion==2):
                    opcion= int(input(" Digita \n ¿1. Puerta ó  2. Puente \n"))
                    if(opcion==1):
                        print("Encuentras 3 puertas: \n Puerta azul : conduce a un infierno \n Puerta verde : te lleva a un asesino mortal \n Puerta roja te conduce a un león que no ha comido en tres meses ")
                        opcion= int(input(" Digita \n ¿1. Puerta azul  \n 2. Puerta verde \n 3. Puerta Roja \n"))
                        if(opcion==1 or opcion==2):
                            print("GAME OVER!")
                        elif(opcion==3):
                            print("Ganaste!!!!!")
                        else:
                            print("Opcion no existe, Vuelve a empezar")
                    elif(opcion==2):
                        print("GAME OVER!")
                    else:
                        print("La opcion digitada no existe")
        elif(opcion==2):
            print("Durante la noche llega un oso")
            opcion= int(input(" Digita \n ¿1. Corres  \n 2. Lo enfrentas \n "))
            if(opcion==1):
                print("Logras escapar del oso \n De tanto correr te deshidratas \n llegas a una casa echa de troncos \n Encuentras un cofre \n")
                opcion= int(input(" Sigue la secuencia para abrirlo  \nU\nD\nT\nC\nC\nS\nS\nO\nN\n ¿1.T - 2. D \n"))
                if(opcion==1):
                    print("GAME OVER!!")
                elif(opcion==2):
                    print("Encuentras una llave  y un mapa \n Llegas a la ubicación  \n")
                    opcion= int(input(" Cuanto es la mitad de 2 + 2 ¿1. 4 ó  2. 2 ?\n"))
                else:
                    print("Opcion incorrecta vuelve a empezar")
                    if(opcion==1):
                        print("GAME OVER!!")
                    elif(opcion==2):
                        print("GANASTE!!")
                    else:
                        print("Opcion incorrecta vuelve a empezar")



    