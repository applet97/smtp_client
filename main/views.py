# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from smtp_util import smtp_client
# Create your views here.

@csrf_exempt
def send_email(request):
	fromaddr = None
	toaddr = None
	subject = None
	msg = None

	if request.method == "POST":
		fromaddr = request.POST.get('fromaddr')
		toaddr = request.POST.get('toaddr')
		subject = request.POST.get('subject')
		msg = request.POST.get('message')
	else:
		fromaddr = request.GET.get('fromaddr')
		toaddr = request.GET.get('toaddr')
		subject = request.GET.get('subject')
		msg = request.GET.get('message')

	return HttpResponse(smtp_client.send_mailru_email(fromaddr=fromaddr, toaddr=toaddr, subject=subject, message=msg))