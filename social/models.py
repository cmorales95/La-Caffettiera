from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre Clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=100)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.TimeField(auto_now_add="True", verbose_name="Fecha de Creación")
    updated = models.TimeField(auto_now="True", verbose_name="Fecha de Actualización")

    # Update information about the presentation of the app in the admin django
    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]

    def __str__(self):
        return self.name
