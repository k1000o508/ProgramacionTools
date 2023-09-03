#Limpiamos la consola
import os 

#Barra de carga
import tqdm

#Tiempo
import time as t

#_____________________________________________________________________Simulacion de carga_____________________________________________________________________

# Create an instance of the tqdm.tqdm class.
pbar = tqdm.tqdm(range(0,100,5))

# Iterate over the list of elements.
for i in pbar:
    
    #limpiamos la terminal
    os.system('cls')
    
    # Actualizacion de la barra de progreso.
    pbar.update()

    # Escribimos el estado del bucle
    pbar.write(f"{i}")

    t.sleep(0.15)

os.system('cls')

# Close the progress bar.
pbar.close()

os.system("cls")
#_____________________________________________________________________Simulacion de carga_____________________________________________________________________
