# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Disease(models.Model):
    name = models.CharField(max_length=10000, null=True, blank=True)
    count = models.IntegerField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=10000, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return self.user

class Patiente(models.Model):
    patiente_id = models.CharField(max_length=10000, null=True, blank=True)
    disease = models.ForeignKey(Disease, null=True)
    comment = models.CharField(max_length=10000, null=True, blank=True)
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return self.disease


class Opd(models.Model):
    name = models.CharField(max_length=10000, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10000, null=True, blank=True)
    department = models.CharField(max_length=10000, null=True, blank=True)
    roomNo = models.CharField(max_length=10000, null=True, blank=True)
    relation = models.CharField(max_length=10000, null=True, blank=True)
    option = models.CharField(max_length=10000, null=True, blank=True)
    phone = models.CharField(max_length=10000, null=True, blank=True)
    address = models.CharField(max_length=10000, null=True, blank=True)
    adhar = models.CharField(max_length=10000, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Ipd(models.Model):
    name = models.CharField(max_length=10000, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10000, null=True, blank=True)
    department = models.CharField(max_length=10000, null=True, blank=True)
    roomNo = models.CharField(max_length=10000, null=True, blank=True)
    relation = models.CharField(max_length=10000, null=True, blank=True)
    option = models.CharField(max_length=10000, null=True, blank=True)
    phone = models.CharField(max_length=10000, null=True, blank=True)
    address = models.CharField(max_length=10000, null=True, blank=True)
    adhar = models.CharField(max_length=10000, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name