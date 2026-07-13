import os
import shutil

carpeta = input("Que carpeta quieres organizar? (ruta completa): ")
archivos = os.listdir(carpeta)
for archivo in archivos:
    ruta_completa = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta_completa):
        try:
                extension = archivo.split(".")[-1]
                print(archivo, "->", extension)
                if extension == "py":
                     carpeta_destino = "codigos"
                elif extension == "pdf":
                     carpeta_destino = "documentos"
                elif extension == "jpg" or extension == "png":
                     carpeta_destino = "imagenes"
                else :
                     carpeta_destino = "otros"
                carpeta_destino_final = os.path.join(carpeta, carpeta_destino)
                os.makedirs(carpeta_destino_final, exist_ok=True)
                shutil.move(ruta_completa, carpeta_destino_final)
                print(archivo, "movido a:", carpeta_destino_final)

                     
        except:
            print(f"No se pudo procesar : {archivo}")