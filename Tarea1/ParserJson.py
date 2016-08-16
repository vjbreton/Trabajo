# Parser para archivos json

def jsonToDictMio(path):
    archivo = open(path,"r")
    
    return archivo



archivo = jsonToDictMio("routes.json")




archivo2 = ""
for e in archivo:
    archivo2 += e.strip("\n")
print(archivo2)















archivo.close()


