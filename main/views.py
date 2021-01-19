from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from  datetime import date
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
today_date = date.today()



class DateInput(forms.DateInput):
    input_type = "date"


class UserForm(forms.Form):

    start_date = forms.DateField(label="Start Date", widget=DateInput())
    end_date = forms.DateField(label="End Date", widget=DateInput())

    def clean(self):
        cleaned_data= super().clean()
        start = self.cleaned_data["start_date"]
        end = self.cleaned_data["end_date"]
        if end < start:
            raise forms.ValidationError("End date should be greater than start date.")
        
        
        if start >= today_date:
            raise forms.ValidationError("Start date should not be future date and current date.Please enter valid date")
        
        
       
        if end > today_date:
            raise forms.ValidationError("End date should not be future date .Please enter valid date")
        
        if end == start:
            raise forms.ValidationError("Start date should not be equal to end date .Please enter valid date")

        if start.year<2015:
            raise forms.ValidationError("Cannot provide you images before 2015 the sattellite images are not available before 2015")

# Create your views here. 


def map(request):
    
   
    server_date=today_date
    days_before=datetime.timedelta(5)
    date_7_days_before=server_date-days_before
    final_server_date_for_map=str(date_7_days_before)+"/"+str(server_date)
    print(final_server_date_for_map)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            start_point = form.cleaned_data["start_date"]
            end_point = form.cleaned_data["end_date"]
            print(type(str(start_point)))
            print(type(str(end_point)))
            final_date=str(start_point)+"/"+str(end_point)
            print(final_date)
            return render(request, "map.html", {"date":final_date,"form":form})
            



        else:
            return render(request, "map.html", {"date": final_server_date_for_map,"form": form})
    return render(request, "map.html", {"date": final_server_date_for_map, "form": UserForm()})
