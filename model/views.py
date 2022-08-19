import json
from django.shortcuts import render
from .forms import DataForm
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
import pathlib

def dump_data_using_csv(file):
    file_data = file.read().decode("utf-8")
    lines = file_data.split("\n")
    for line in lines[1:-1]:
        fields = line.split(",")
        obj = Data(
            employee_name=fields[0],
            dob=fields[1],
            state = fields[2],
            pincode = fields[3],
            salary = fields[4],
            joining_month = fields[5],
            joining_year = fields[6]
        )
        obj.save()
def dump_data_using_json(file):
    data = json.load(file)
    for row in data:
        obj = Data(
            employee_name=row['employee_name'],
            dob=row['dob'],
            state = row['state'],
            pincode = row['pincode'],
            salary = row['salary'],
            joining_month = row['joining_month'],
            joining_year = row['joining_year']
        )
        obj.save()

# def handle_uploaded_file(f):
#     with open('model/upload/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
# Create your views here.
# Create your views here.
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    name=''
    context = {}
    if request.POST:
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file = request.FILES["choose_file_csv_or_JSON"] 
            name = pathlib.Path(str(upload_file)).suffix
        if str(name) == '.csv':
            dump_data_using_csv(upload_file)
        elif str(name) == '.json':
            dump_data_using_json(upload_file)
        else:
            return HttpResponse("This file format is not supported. Please upload csv or json file.")
    else:
        form = DataForm()
    context['form'] = form
    return render(request, "upload.html", context)
