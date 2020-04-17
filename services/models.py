from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="services", verbose_name="Imagen")
    created = models.TimeField(auto_now_add="True", verbose_name="Fecha de Creación")
    updated = models.TimeField(auto_now="True", verbose_name="Fecha de Actualización")

    # Update information about the presentation of the app in the admin django
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]

    def __str__(self):
        return self.title
