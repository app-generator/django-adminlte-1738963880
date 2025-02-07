# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Input(models.Model):

    #__Input_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)

    #__Input_FIELDS__END

    class Meta:
        verbose_name        = _("Input")
        verbose_name_plural = _("Input")


class Output(models.Model):

    #__Output_FIELDS__
    state = models.BooleanField()

    #__Output_FIELDS__END

    class Meta:
        verbose_name        = _("Output")
        verbose_name_plural = _("Output")



#__MODELS__END
