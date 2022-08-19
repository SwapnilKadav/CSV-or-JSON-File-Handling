from django.shortcuts import render, redirect
from .forms import DataTable
from model.models import Data
import matplotlib.pyplot  as plt
import numpy as np
import calendar
# Create your views here.
def data_view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        form = DataTable(request.POST)
        if form.is_valid():
            choice1= request.POST.get('choice1')
            choice2= request.POST.get('choice2')
            month = Data.objects.values('joining_month')
            year = Data.objects.values('joining_year')
            if choice2 == 'p':
                if choice1 == 'm':
                    x=[]
                    x1={}
                    data=[]
                    lable1=[]
                    for col in month:
                        x.append(calendar.month_name[np.array(int(col['joining_month']))])
                    x.sort()
                    for i in x:
                        x1[i]=x.count(i)
                    for k , v in x1.items():
                        lable1.append(k)
                        data.append(v)
                    plt.title('Joining Per Month')
                    plt.pie(data,labels=lable1,autopct='%.0f%%')
                    plt.show()
                if choice1 == 'y':
                    y=[]
                    y1={}
                    data=[]
                    lable1=[]
                    for col in year:
                        y.append(np.array(int(col['joining_year'])))
                    y.sort()
                    for i in y:
                        y1[str(i)]=y.count(i)
                    for k , v in y1.items():
                        lable1.append(k)
                        data.append(v)
                    plt.title('Joining Per Year')
                    plt.pie(data,labels=lable1, autopct='%.0f%%')
                    plt.show()
            if choice2 == 'b':
                if choice1 == 'm':
                    x=[]
                    x1=[]
                    x2=[]
                    for col in month:
                        x.append(np.array(int(col['joining_month'])))
                    for i in x:
                        x1.append(x.count(i))
                        x2.append(calendar.month_name[i])
                    plt.bar(x2,x1)
                    plt.title('Joining Per Month')
                    plt.xlabel('Months')
                    plt.ylabel("Number of Joiners in month's")
                    plt.show()
                if choice1 == 'y':
                    y=[]
                    y1=[]
                    for col in year:
                        y.append(np.array(int(col['joining_year'])))
                    for i in y:
                        y1.append(y.count(i))
                    plt.bar(y,y1)
                    plt.title('Joining Per Year')
                    plt.xlabel('Year')
                    plt.ylabel("Number of Joiners in Year's")
                    plt.show()
                # for col in year:
                #     print(col['joining_year'],"-------------------------")
                    
    else:
        form = DataTable() 
    context = {
        'form': form
    }
    return render(request, "dataview/DataTable.html", context)
