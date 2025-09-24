class Cursos:
  def __init__(self,codigo,creditos,nombre):
   self.__codigo=codigo
   self.__creditos=creditos
   self.__nombre=nombre

  def asignar(self):
   print("Asignado clase")

  def getCodigo(self):
    return self.__codigo

  def setCodigo(self,codigo):
    self.__codigo=codigo



  def getCreditos(self):
    return self.__creditos

  def setCreditos(self,creditos):
    self.__creditos=creditos

  def getNombre(self):
      return self.__nombre

  def setNombre(self,nombre):
    self.__nombre=nombre           


class Alumnos:
  def __init__(self,nombre,edad,matricula):
    self.nombre=nombre
    self.edad=edad
    self.matricula=matricula

  def inscriberse(self):
     pass
  

  def estudiar(self):
    pass
  

class Profesor:
  def __init__(self,nombre,experencia,num_profesor):
    self.nombre=nombre
    self.experncia=experencia
    self.num_profesor=num_profesor

  def impartir(self):
    pass
  
  def evaluar(self):
    pass
  

#Alumno
alumno1=Alumnos("Gabriel",19,3195719)

alunno2=Alumnos("li",20,16465)


#Curso

matematicas=Cursos(86521,50,"matematicas")

programacion=Cursos(56515,40,"programacion")

#profesor

russo=Profesor("nombre",10,6942)

dagoberto=Profesor("dagoberto",15,54036)



