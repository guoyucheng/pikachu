# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class CustomUserSession(models.Model):
    user = models.ForeignKey(User,verbose_name="userid")
    session_key = models.CharField(max_length=1024, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True) #创建时间

    class Meta:
        db_table = "custom_user_session"
        verbose_name = u'custom_user_session'
        verbose_name_plural = u'custom_user_session'
