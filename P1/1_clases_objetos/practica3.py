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

  def inscribirse(self):
     pass

  def estudiar(self):
    pass

  def getNombre(self):
    return self.nombre

  def setNombre(self, nombre):
    self.nombre = nombre

  def getEdad(self):
    return self.edad

  def setEdad(self, edad):
    self.edad = edad

  def getMatricula(self):
    return self.matricula

  def setMatricula(self, matricula):
    self.matricula = matricula

class Profesor:
  def __init__(self,nombre,experencia,num_profesor):
    self.nombre=nombre
    self.experncia=experencia
    self.num_profesor=num_profesor

  def impartir(self):
    pass

  def evaluar(self):
    pass

  # Getters y setters
  def getNombre(self):
    return self.nombre

  def setNombre(self, nombre):
    self.nombre = nombre

  def getExperiencia(self):
    return self.experncia

  def setExperiencia(self, experiencia):
    self.experncia = experiencia

  def getNumProfesor(self):
    return self.num_profesor

  def setNumProfesor(self, num_profesor):
    self.num_profesor = num_profesor

#Alumno
alumno1=Alumnos("Gabriel",19,3195719)

alunno2=Alumnos("li",20,16465)


#Curso

matematicas=Cursos(86521,50,"matematicas")

programacion=Cursos(56515,40,"programacion")

#profesor

russo=Profesor("nombre",10,6942)

dagoberto=Profesor("dagoberto",15,54036)



