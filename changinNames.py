# f = open('textAbsolutelyNoGeneric.txt', 'r', encoding = "utf-8")

# ! os.fsdecode(nombrearchivo)
# ? Decodifica el nombre de archivo de tipo ruta a partir de la codificación del sistema de archivos y el manejador de errores; devuelve str sin cambios.

# TODO: os.fsencode(nombrearchivo)
# ¡ Codifica el nombre de archivo tipo ruta según la codificación del sistema de archivos y el manejador de errores; devuelve los bytes sin cambios.

# * os.listdir(ruta='.')
# $ Devuelve una lista con los nombres de las entradas del directorio indicado por ruta. La lista está en orden arbitrario, y no incluye las entradas especiales '.' y '..' aunque estén presentes en el directorio. Si se elimina o añade un archivo al directorio durante la llamada a esta función, no se especifica si se incluirá un nombre para ese archivo.

import os

directory = input("Please enter the path of the folder in which files are stored: ")
fileNumberUnit = 0
fileNumberTen = 0
fileNumberCent = 0
fileNumberThou = 0

pageNumber = "{:03d}".format(fileNumberThou * 1000 + fileNumberCent * 100 + fileNumberTen * 10 + fileNumberUnit)

print(os.listdir(directory))

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg") or filename.lower().endswith(".png"):
        # CASE SENSITIVE
        # print(os.path.join(directory, filename), " ok")
        print(filename, ": ok")
        print("fileNumberUnit: ", fileNumberTen)
        fileNumberUnit += 1
        print("fileNumberUnit: ", fileNumberTen)
        pageNumber = "{:03d}".format(fileNumberCent * 100 + fileNumberTen * 10 + fileNumberUnit)
        
        if fileNumberUnit > 9:
            fileNumberTen += 1
            print("fileNumberTen: ", fileNumberTen)
            fileNumberUnit = 0
            
            print("pageNumber: ", pageNumber)
            if fileNumberTen > 9:
                fileNumberCent +=1
                print("fileNumberCent: ", fileNumberCent)
                fileNumberTen = 0
                # pageNumber = "{:03d}".format(fileNumberCent * 100 + fileNumberTen * 10 + fileNumberUnit)
                print("pageNumber: ", pageNumber)
                
                if fileNumberCent > 9:
                    fileNumberThou +=1
                    print("fileNumberThou: ", fileNumberThou)
                    fileNumberCent = 0
                    # pageNumber = "{:03d}".format(fileNumberCent * 100 + fileNumberTen * 10 + fileNumberUnit)
                    print("pageNumber: ", pageNumber)

        # os.rename(os.path.join(directory, filename), os.path.join(directory, pageNumber) + ".jpg")
        os.rename(os.path.join(directory, filename), os.path.join(directory, pageNumber) + ".jpg")
        
    else:
        print("Not found, or the file type is incorrect.")
    