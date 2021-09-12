from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class OpenWeatherCity(models.Model):
    name = models.CharField(max_length=155, null=False, blank=False, verbose_name=_("Name"))
    country = models.CharField(max_length=10, null=False, blank=False, verbose_name=_("Country"))
    open_weather_id = models.IntegerField(null=False, blank=False, verbose_name=_("Open Weather ID"))

    class Meta:
        verbose_name = _("Open Weather City")
        verbose_name_plural = _("Open Weather Cities")

    