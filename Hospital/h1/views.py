from django.shortcuts import render,redirect
from django.contrib import messages
from h1.models import 	Hospital,Doctor
from dateutil import parser
# Create your views here.


def Show(request):

	return render(request,'indexx.html')


def hospital(request):

	return render(request,'hospital.html')

def save_hospital(request):
	h_name=request.POST.get('h1')
	B_count=request.POST.get('h2')
	
	Hospital(Hospital_name=h_name,Bed_count=B_count).save()
	messages.success(request,'Data has been saved')
	return redirect('main')


def doctor(request):

	return render(request,'doctor.html',{'h_data':Hospital.objects.all(),'d_data':Doctor.objects.all()})

def doctor_save(request):
	n=request.POST.get('n1')
	d=request.POST.get('n2')
	spe=request.POST.get('n3')
	sal=request.POST.get('n4')
	exp=request.POST.get('n5')
	h_id=request.POST.get('n6')


	Doctor(Doctor_name=n,Joining_date=d,Speciality=spe,Salary=sal,Experiance=exp,hospital_id_id=h_id).save()
	messages.success(request,'Data has been saved')
	return redirect('main')
	
def delete(request):

	idn=request.GET.get('D_id')
	Doctor.objects.filter(Doctor_id=idn).delete()
	return redirect('main')
def update(request):
	idn=request.GET.get('D_id')
	res=Doctor.objects.get(Doctor_id=idn)
	return render(request,'update.html',{'data':res})

def data_update(request):
	idn=request.POST.get('u1')
	n  =request.POST.get('u2')
	d  =request.POST.get('u3')

	new_date=parser.parse(d)
	date=new_date.strftime("%Y-%m-%d")
	print('===========================>>>>>>>>>>>>>>>>>>>>>>',date)
	spe=request.POST.get('u4')
	sal=request.POST.get('u5')
	exp=request.POST.get('u6')

	Doctor.objects.filter(Doctor_id=idn).update(Doctor_name=n,
		Joining_date=new_date,Speciality=spe,Salary=sal,Experiance=exp)
	return redirect('main')


