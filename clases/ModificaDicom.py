
'''
  Esto sirve para la cambiarle el nombre a la imagen dicom
'''
import os
class ModificaDicom():
  def __init__(self,ruta,rutaRemplaza):    
    self.ruta=ruta
    self.rutaRemplaza=rutaRemplaza

  def Modifica(self):
    try : 
      os.rename(self.ruta,self.rutaRemplaza)
      print('Nombre cambiado correctamente')
      return True
    except IsADirectoryError: 
      print("Source is a file but destination is a directory.")                
      return False
    except NotADirectoryError: 
      print("Source is a directory but destination is a file.")               
      return False
    except PermissionError: 
      print('Error no se pudo modificar el nombre de la imagen Dicom')
      print('Ruta de la imagen : ')
      print(self.ruta)
      return False
    except OSError as error: 
      print(error)
      return False 
    
      
      