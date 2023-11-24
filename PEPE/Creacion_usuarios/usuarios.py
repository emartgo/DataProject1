import pandas as pd
import random

# lectura de las data bates

nombre_mujeres_df = pd.read_csv('nombre_mujeres.csv', 
                             dtype = {
                                 "nombre": str
                             })
nombre_mujeres_df = nombre_mujeres_df["nombre"].head(5000)
nombre_hombres_df = pd.read_csv('nombre_hombres.csv', 
                             dtype = {
                                 "nombre": str
                             })
nombre_hombres_df = nombre_hombres_df["nombre"].head(5000)
apellidos_df = pd.read_csv('apellidos.csv', 
                             dtype = {
                                 "apellido": str
                             })
apellidos_df = apellidos_df["apellido"].head(5000)

ccaa_df = pd.read_csv('provincias.csv', delimiter=';')
ccaa_df = ccaa_df[["Nombre_CCAA", "Nombre_Provincia"]]



# generacion de un user aleatorio

for usuarios in range(10):

    dni = random.randint(10000000,99999999) 
    sexo_choice = random.randint(1,2)              # seleccion hombre mujer
    if(sexo_choice == 1):
        n = random.randint(0,5000)
        nombre = nombre_hombres_df.iloc[n]
        sexo = "HOMBRE"
    else:
        n = random.randint(0,5000)
        nombre = nombre_mujeres_df.iloc[n]
        sexo = "MUJER"
    
    edad = random.randint(65, 100)
    n_apellido1 = random.randint(0,5000)
    n_apellido2 = random.randint(0,5000)
    apellido_1 = apellidos_df.iloc[n_apellido1]
    apellido_2 = apellidos_df.iloc[n_apellido2]

    n_localidad = random.randint(0, len(ccaa_df))
    municipio = ccaa_df["Nombre_Provincia"].iloc[n_localidad]
    provincia = ccaa_df["Nombre_CCAA"].iloc[n_localidad]

    print(f'{dni}, {nombre}, {apellido_1}, {apellido_2}, {sexo}, {edad}, {provincia}, {municipio}')

    
    
  








