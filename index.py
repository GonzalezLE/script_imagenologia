"""
pip install requests
pip install watchdog
pip install termcolor
"""
import requests
from clases.ModificaDicom import ModificaDicom
from clases.Nomenclatura import Nomenclatura
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from termcolor import colored

##################################################################
#       Ruta de la carpeta que vamos a estar revisando 
##################################################################
path = "C:\wamp\www\Imagenologia2"
##################################################################



if __name__ == "__main__":
  print(colored('****************** Iniciando programa ******************','blue'))
  patterns = "*"
  ignore_patterns = ""
  ignore_directories = False
  case_sensitive = True
  my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
  evento2 = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


def sube_documento(ruta):    
  try:
    print('Subiendo direccion')
    myobj = {'dicom': ruta}
    # mandamos el json a la api
    res=requests.post('https:https://Ruta de la api',data=myobj)
    if res.text=='success':
      print('imagen dicom guardada')
    else:
      print(res.text)        
  except requests.exceptions.ConnectionError as errc:
    #bucle infinito que termina cuando finaliza la petición
    while buscaconeccion(ruta):
      print(colored('Error en conexión de internet','red'))
      print(colored('Buscando conexión','red'))
      print(colored('..','red'))
      print(colored('.','red'))     

def buscaconeccion(ruta):
  try:
    myobj = {'dicom': ruta}
    # mandamos el json a la api
    respuesta=requests.post('https://Ruta de la api',data=myobj)    
    
    if respuesta.status_code==200:
      if respuesta.text=='success':
        print('Imagen dicom guardada ')
      return False
    else:
        print(respuesta.status_code)
        
  except requests.exceptions.ConnectionError as errc:
    return True
  
#Este método escucha todo lo que cae dentro de la carpeta
def on_created(event):  
  try:
    ruta= event.src_path  
    rutaOriginal=ruta
    ruta=ruta.split('\\')    
    tamana=len(ruta)    
    dicom_nomenclatura=ruta[tamana-1]

    Obj=Nomenclatura(dicom_nomenclatura)
    nomenclatura=Obj.crear()

    rutanueva=''      
    #A la ruta original le quitamos la nomenclatura mala y le pasamos la buena para sustituir      
    rutanueva=rutaOriginal.replace(dicom_nomenclatura,nomenclatura)   

    bandera2=False
    #condicion para cer si esta bien la nomenclatura 
    if dicom_nomenclatura==nomenclatura:
      print('nombre bien')
      #mandamos ruta al servidor
      
      
      sube_documento(rutaOriginal)
    else:
      print('*************************************')
      print('   Modificando nombre de la imagen   ')
      print('*************************************')              
      #instancia objeto modificar dicom 
      OBJmodifica=ModificaDicom(rutaOriginal,rutanueva)
      # --- Is_modificado=OBJmodifica.Modifica()
      if Is_modificado :
        print(rutanueva)        
        #bandera2=True                 
        sube_documento(rutanueva)
      else:
        print('ruta guardada')
        sube_documento(rutaOriginal)  
  except:
    print("Error--")



# my_event_handler.on_created = on_created
# my_event_handler.on_modified = on_created
# my_event_handler.on_moved = on_created
my_event_handler.on_any_event = on_created


go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)


my_observer.start()


try:
  while True:
    time.sleep(5)
except:
  my_observer.stop()
  #ba.stop()
my_observer.join()
#ba.join()
