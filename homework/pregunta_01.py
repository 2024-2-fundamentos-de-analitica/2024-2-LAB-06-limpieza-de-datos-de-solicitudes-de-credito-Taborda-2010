import pandas as pd
import os


# Crear el directorio si no existe
os.makedirs('files/output', exist_ok=True)

def pregunta_01():
    """
        Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
        El archivo tiene problemas como registros duplicados y datos faltantes.
        Tenga en cuenta todas las verificaciones discutidas en clase para
        realizar la limpieza de los datos.

        El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
    """
    # Eliminar el archivo si existe
    if os.path.exists('files/output/solicitudes_de_credito.csv'):
        os.remove('files/output/solicitudes_de_credito.csv')
    
    # Se abre el archivo
    ruta = 'files/input/solicitudes_de_credito.csv'
    df = pd.read_csv(ruta, sep=';', index_col=0, encoding='UTF-8')

    #Se limpian las columnas
    #Seleccionamos las columnas a evaluar
    columnas = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]

    #Hacemos un ciclo for para limpiar las columnas
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].str.lower().str.strip().str.replace("_", " ").str.replace("-", " ").str.replace(",", "").str.replace("$", "").str.replace(".00", "").str.strip()

    # Limpiar idea_negocio
    df['idea_negocio'] = df['idea_negocio'].str.replace(' ','_').str.replace('-','_').str.strip('_')

    # Limpiar barrio 
    df['barrio'] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")

    # Dar formato a estrato
    df['estrato'] = df['estrato'].astype(int)

    # Dar formato a comuna_ciudadano
    df['comuna_ciudadano'] = pd.to_numeric(df["comuna_ciudadano"], errors="coerce", downcast="integer")

    # Limpiar la columna fecha_de_beneficio
    df['fecha_de_beneficio'] = df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    # Limpiar la columna monto_del_credito
    df['monto_del_credito'] = pd.to_numeric(df["monto_del_credito"], errors="coerce")


    #Borramos duplicados y nulos
    df = df.drop_duplicates()
    df = df.dropna()
    # Guardar el DataFrame limpio
    df.to_csv('files/output/solicitudes_de_credito.csv', sep=';', index=False)


pregunta_01()