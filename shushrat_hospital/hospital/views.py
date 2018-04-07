# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.decorators.http import require_GET, require_POST
import json
from .models import *

@csrf_exempt
def singupuser(request):
    try:
        if request.method == 'GET':
            print 1
        if request.method == 'POST':
            user_name = request.POST['email'].strip()
            password = request.POST['password'].strip()
            hospital_name = request.POST['hospitalname'].strip()
            if user_name is not None and password is not None:
                user = User.objects.create_user(user_name, user_name, password)
                user.save()
                profile = Profile.objects.create(user=user, hospital_name=hospital_name)
                profile.save()
                if user is not None:
                    return HttpResponseRedirect(reverse(newpatiente(request)))
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def loginuser(request):
    try:
        if request.method == 'GET':
            return render(request, 'login.html')

        if request.method == 'POST':
            user_name = request.POST['username'].strip()
            password = request.POST['password'].strip()
            if user_name is not None and password is not None:
                user = authenticate(username=user_name, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/patiente/')
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def logout_view(request):
    try:
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def newpatienteshow(request):
    try:
        top_disease = Disease.objects.order_by('-count')[:10]
        return render(request, 'patiente/newpatiente.html', {'disease_obj': top_disease})
    except Exception as e:
        return HttpResponse(e)


@csrf_exempt
def newpatiente(request):
    try:
        top_disease = Disease.objects.order_by('-count')[:10]
        if request.method == 'GET':
            return render(request, 'patiente/newpatiente.html', {'disease_obj': top_disease})
        if request.method == 'POST':
            patiente_id = request.POST.get('patiente_id')
            disease = request.POST.get('disease')
            comment = request.POST.get('comment')
            submit = request.POST.get('submit')
            if submit == 'submit':
                try:
                    d = Disease.objects.get(name=disease)
                except:
                    d = None
                if patiente_id is not None and disease is not None and d is None:
                    disease_obj = Disease.objects.create(name=disease, count=1)
                    disease_obj.save()
                    patiente = Patiente.objects.create(patiente_id=patiente_id, disease=disease_obj, comment=comment)
                    patiente.save()
                    return render(request, 'patiente/newpatiente.html', {'disease_obj': top_disease})

                elif patiente_id is not None and disease is not None and d is not None:
                    d.count = d.count + 1
                    d.save()
                    patiente = Patiente.objects.create(patiente_id=patiente_id, disease=d, comment=comment)
                    patiente.save()
                    return render(request, 'patiente/newpatiente.html', {'disease_obj': top_disease})

            else :
                if patiente_id is not None:
                    disease_obj = Disease.objects.get(name=submit)
                    disease_obj.count = disease_obj.count + 1
                    disease_obj.save()
                    patiente = Patiente.objects.create(patiente_id=patiente_id, disease=disease_obj, comment=comment)
                    patiente.save()
                    return render(request, 'patiente/newpatiente.html', {'disease_obj': top_disease})
            return render(request, 'patiente/newpatiente.html', {'disease_obj': top_disease})
    except Exception as e:
        return HttpResponse(e)


@csrf_exempt
def showpatiente(request):
    try:
        patiente = Patiente.objects.filter(active=True)
        return render(request, 'patiente/report.html', {'patiente': patiente})
    except Exception as e:
        print 'Exception:', e
        return e

@csrf_exempt
def newipd(request):
    try:
        if request.method == 'GET':
            return render(request, 'ipd/newipd.html')
        if request.method == 'POST':
            name = request.POST.get('name')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            department = request.POST.get('department')
            roomNo = request.POST.get('roomNo')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            relation = request.POST.get('relation')
            option = request.POST.get('option')
            adhar = request.POST.get('adhar')
            obj = Ipd(name=name, age=age, gender=gender, relation=relation, option=option,
                                  department=department, roomNo=roomNo, phone=phone, address=address,adhar=adhar)
            obj.save()
            opd = Ipd.objects.all()
        return render(request, 'ipd/newipd.html')
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def showipd(request):
    try:
        ipd = Ipd.objects.all()
        return render(request, 'ipd/showipd.html', {'ipd': ipd})
    except Exception as e:
        return HttpResponse(e)


@csrf_exempt
def patientebracode(request):
    try:
        json_obj = {'name':'Ayush Thakur','age':'28 Y / Male','barcode':'305288'}
        return render(request, '400.html', {'barcode': json_obj})
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def newopd(request):
    try:
        if request.method == 'GET':
            return render(request, 'opd/newopd.html')
        if request.method == 'POST':
            name = request.POST.get('name')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            department = request.POST.get('department')
            roomNo = request.POST.get('roomNo')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            relation = request.POST.get('relation')
            option = request.POST.get('option')
            adhar = request.POST.get('adhar')
            # obj = Opd(name=name, age=age, gender=gender, relation=relation, option=option,
            #                       department=department, roomNo=roomNo, phone=phone, address=address,adhar=adhar)
            # obj.save()
            opd = Opd.objects.all()
            barcode_obj = {}
            barcode_obj['name'] = name
            barcode_obj['age'] = age + 'Y /'+ 'Male'
            barcode_obj['barcode'] = '09809'
        return render(request, 'opd/newopd.html')
    except Exception as e:
        print e
        return render(request, 'opd/newopd.html')

@csrf_exempt
def showopd(request):
    try:
        opd = Opd.objects.all()
        return render(request, 'opd/showopd.html',{'opd':opd})
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def showdiseas(request):
    try:
        d = Disease.objects.all()
        # d = Disease.objects.order_by('-count')[:3]
        return render(request, 'patiente/disease.html',{'disease':d})
    except Exception as e:
        return HttpResponse(e)