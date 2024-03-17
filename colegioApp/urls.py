from django.urls import path
from .views import  (DocenteRegistro,
                     DocenteControler,
                     CrearCurso,
                     listarCursosDocente,
                     listarCalificaciones,
                     GestionarCursos)


urlpatterns = [
    path('docentes/', view=DocenteRegistro.as_view()),
    path('docente/<int:id>/', view=DocenteControler.as_view()),
    path('cursos/', view=CrearCurso.as_view()),
    path('curso/<int:id>/docente/',view=listarCursosDocente.as_view()),
    path('calificar/curso/<int:id>/', view=listarCalificaciones),
    path('calificar-curso/<int:id>/', view=GestionarCursos.as_view())
    
] 