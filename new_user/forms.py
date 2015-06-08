# -*- coding: utf-8 -*-
from .models import User
from django.contrib.auth.forms import UserCreationForm


class AdminUserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'avatar', 'email']
