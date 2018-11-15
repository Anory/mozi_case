# from django.shortcuts import render
# from django.http.response import HttpResponse
# from django.shortcuts import render
# from django.http import JsonResponsef
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import requests
import json
# Create your views here.
def Login(request):
    if request.method == "POST":
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['username'] = username
        result['password'] = password
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    else:
        return render_to_response("login.html")

