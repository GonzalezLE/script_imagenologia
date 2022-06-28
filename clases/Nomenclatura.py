'''
  Esto sirve para la nomenclatura crea la nomenclatura
  nimsas-consecutivo_idEstudio
'''
class Nomenclatura():
  def __init__(self, cadena):    
    self.cadena = cadena

  def crear(self):
    contador=0
    nueva_nomenclatura=''
    for item in self.cadena:            
      if contador>=0 and contador<=8:
        nueva_nomenclatura=nueva_nomenclatura+item
      else:
        if contador==9:
          nueva_nomenclatura=nueva_nomenclatura+'-'
        else:
          if contador>=10 and contador<=13:
            nueva_nomenclatura=nueva_nomenclatura+item
          else:
            if contador==14:
              nueva_nomenclatura=nueva_nomenclatura+'_'
            else:
              if contador>=15 and contador<=19:
                nueva_nomenclatura=nueva_nomenclatura+item
              else:
                if contador==20:
                  nueva_nomenclatura=nueva_nomenclatura+'_'                        
                else:
                  if contador>=21:
                    nueva_nomenclatura=nueva_nomenclatura+item                    
      
      contador=contador+1    
    return nueva_nomenclatura

      