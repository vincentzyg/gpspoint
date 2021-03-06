from django.shortcuts import render ,redirect
import json as simplejson
from django.views.decorators.csrf import csrf_exempt  
from django.http import HttpResponse
from models import Userdata , Sensordata , Emergencydata
from datetime import *
# Create your views here.

@csrf_exempt
def Get_userdata(request):
    
    try:
    	if request.method=='POST':
	    print request.POST
#get the querydict of post ------userdata
	    user_id_get=request.POST.get('user_id')
	    username_get=request.POST.get('username')
	    gender_get=request.POST.get('gender')
	    birthday_get=request.POST.get('birthday') 
	    blood_type_get=request.POST.get('blood_type') 
	    emergency_number_get=request.POST.get('emergency_number')  
	    destination_get=request.POST.get('destination')     	

	    update_userdata=Userdata.objects.update_or_create(user_id=user_id_get,
							username=username_get,
							defaults={'gender':gender_get,
							'birthday':birthday_get,
							'blood_type':blood_type_get,
							'emergency_number':emergency_number_get,
							'destination':destination_get})

#	    if update_userdata[1]:
#		print update_userdata[0].id
		
#	    else:
#		print update_userdata[0].id

	return HttpResponse(update_userdata[0].id)

    except:
	print 'something wrong'
        
    return HttpResponse('ERROR')


@csrf_exempt
def Get_sensordata(request):

    try:
    	if request.method=='POST':
	    print request.POST
#get the querydict of post ------sensordata
	    user_id_list=request.POST.getlist('user_id')
	    timestamp_list=request.POST.getlist('timestamp')
	    lan_list=request.POST.getlist('lan')
	    lon_list=request.POST.getlist('lon')
	    heart_rate_list=request.POST.getlist('heart_rate')
	  
#calculate the length------sensordata
	    l1=len(user_id_list)
	    l2=len(timestamp_list)
	    l3=len(lan_list)
	    l4=len(lon_list)
	    l5=len(heart_rate_list)
#	    l6=len(emergency_number_list)
#	    l7=len(destination_list)
	    
	    L=[]    #list of length
	    L.append(l1)
	    L.append(l2)
	    L.append(l3)
	    L.append(l4)
	    L.append(l5)
#	    L.append(l6)
#	    L.append(l7)
	    
	    compare_list=[]   #compare the items of L, it must have the same number ,if not append 0
	    for i in L:       #else append 1,then compare the result ,if the minimum is 0,drop the userdata
		for j in L:
		    if i==j:
			compare_list.append(1)
		    else:
			compare_list.append(0)
#	    print compare_list,len(compare_list)
	    if min(compare_list)==1:
		i=0		
		while (i<l1):
		    get_sensordata=Sensordata()
		    get_sensordata.user_id=user_id_list[i]
	    	    get_sensordata.timestamp=timestamp_list[i]         
            	    get_sensordata.lan=lan_list[i]
            	    get_sensordata.lon=lon_list[i]
            	    get_sensordata.heart_rate=heart_rate_list[i]
#            	    get_sensordata.emergency_number=emergency_number_list[i]
#            	    get_sensordata.destination=destination_list[i]
	    	    get_sensordata.save()
		    i=i+1
#		print Sensordata.objects.all()
#		print Sensordata.id
	    	return HttpResponse('Successful !')
	    else:
	    	return HttpResponse('You need transmit again !')

    except:
	print 'something wrong'
        
    return HttpResponse('ERROR')


@csrf_exempt
def Get_emergencydata(request):

    try:
    	if request.method=='POST':
	    print request.POST
            print datetime.now()
            print datetime.now().hour
#get the querydict of post ------emergencydata
	    user_id_get=request.POST.get('user_id')
	    timestamp_get=request.POST.get('timestamp')
	    lan_get=request.POST.get('lan')
	    lon_get=request.POST.get('lon')
	    heart_rate_get=request.POST.get('heart_rate')
            body_state_get=request.POST.get('body_state')  

	    get_emergency=Emergencydata()
	    get_emergency.user_id=user_id_get
    	    get_emergency.timestamp=timestamp_get        
       	    get_emergency.lan=lan_get
       	    get_emergency.lon=lon_get
       	    get_emergency.heart_rate=heart_rate_get
            get_emergency.body_state=body_state_get            

            get_emergency.save()

#		print Emergencydata.objects.all()
#		print Emergencydata.id
            return HttpResponse('Successsful ! I will call 999')
        else:
            return HttpResponse('You need transmit again !')

    except:
	print 'something wrong'
        
    return HttpResponse('ERROR')

	
