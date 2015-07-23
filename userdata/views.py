from django.shortcuts import render
import json as simplejson
from django.views.decorators.csrf import csrf_exempt  
from django.http import HttpResponse
from models import Userdata
# Create your views here.

@csrf_exempt
def get_userdata(request):

    try:
    	if request.method=='POST':
#get the querydict of post 
	    user_id_list=request.POST.getlist('user_id')
	    username_list=request.POST.getlist('username')
	    gender_list=request.POST.getlist('gender')
	    age_list=request.POST.getlist('age') 
	    blood_type_list=request.POST.getlist('blood_type') 
	    emergency_number_list=request.POST.getlist('emergency_number')  
	    destination_list=request.POST.getlist('destination')     	
#calculate the length
	    l1=len(user_id_list)
	    l2=len(username_list)
	    l3=len(gender_list)
	    l4=len(age_list)
	    l5=len(blood_type_list)
	    l6=len(emergency_number_list)
	    l7=len(destination_list)
	    
	    L=[]    #list of length
	    L.append(l1)
	    L.append(l2)
	    L.append(l3)
	    L.append(l4)
	    L.append(l5)
	    L.append(l6)
	    L.append(l7)
	    
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
		    userdata=Userdata()
		    userdata.user_id=user_id_list[i]
	    	    userdata.username=username_list[i]         
            	    userdata.gender=gender_list[i]
            	    userdata.age=age_list[i]
            	    userdata.blood_type=blood_type_list[i]
            	    userdata.emergency_number=emergency_number_list[i]
            	    userdata.destination=destination_list[i]
	    	    userdata.save()
		    i=i+1
#		    print Userdata.objects.all()
	    	return HttpResponse('Successful !')
	    else:
	    	return HttpResponse('You need transmit again !')

    except:
	print 'something wrong'
        
    return HttpResponse('ERROR')

