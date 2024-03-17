from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Docente (models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False)
    apellido = models.TextField(null=False)
    correo = models.EmailField(null=False)
    password = models.TextField(null=False)
    especializacion = models.TextField(null=False)
    telefono = models.TextField(null=False)
    foto = models.ImageField(null=False)
    
    class Meta:
        db_table = 'docentes'


class Estudiante (models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False) 
    apellido = models.TextField(null=False)
    correo = models.EmailField(null=False)
    password = models.TextField(null=False)
    foto = models.ImageField(null=False)

    class Meta:
        db_table = 'estudiantes'

class Curso (models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False)
    seccion = models.TextField(null=False)
    hInicio = models.TimeField(db_column='h_inicio',null=False)
    hFinal = models.TimeField(db_column='h_final', null=False)

    docenteId = models.ForeignKey(to=Docente, db_column='docente_id',on_delete=models.CASCADE)

    class Meta:
        db_table = 'cursos'

class CursoEstudiante (models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    cursoId = models.ForeignKey(to=Curso, db_column='curso_id', on_delete=models.CASCADE)
    estudianteId = models.ForeignKey(to=Estudiante, db_column='estudiante_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'curso_estudiante'

class Calificacion (models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    pc1 = models.FloatField(null=False)
    pc2 = models.FloatField(null=False)
    pc3 = models.FloatField(null=False)
    examenFinal = models.FloatField(db_column='examen_final' ,null=False)
    promedio = models.FloatField(null=False)
    cursoId = models.ForeignKey(to=Curso, db_column='curso_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'calificaciones'
