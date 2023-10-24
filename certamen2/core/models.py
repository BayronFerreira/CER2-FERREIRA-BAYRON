from django.db import models

class Entidad(models.Model):
    id      = models.BigAutoField(primary_key=True)
    nombre  = models.CharField(max_length=50)
    logo    = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self) -> str:
        return self.nombre
class Comunicado(models.Model):
    TIPO_CHICES = [
        ("S","Suspensión de actividades"),
        ("C","Suspensíon de clase"),
        ("I","Información")
    ]
    id                          = models.BigAutoField(primary_key=True)
    titulo                      = models.CharField(max_length=30)
    detalle                     = models.CharField(max_length=200)
    detalle_corto               = models.CharField(max_length=50)
    tipo                        = models.CharField(max_length=1, choices=TIPO_CHICES)
    entidad                     = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible                     = models.BooleanField()
    fecha_de_publicacion        = models.DateTimeField(auto_now=False, auto_now_add=False)
    fecha_ultima_publicacion    = models.DateTimeField(auto_now=False, auto_now_add=False)
    publicado_por               = models.CharField(max_length=50)
    modificado_por              = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.titulo