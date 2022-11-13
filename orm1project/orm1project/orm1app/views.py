from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg, Sum, Max, Min, Count
from orm1app.models import Employee1
from django.db.models.functions import Lower

# Create your views here.
def display_view(request):
    #employees=Employee1.objects.all()
    #employees=Employee1.objects.filter(esal__gt=18000)
    #employees=Employee1.objects.filter(esal__gte=15000)
    #employees=Employee1.objects.filter(esal__lt=15000)
    #employees=Employee1.objects.filter(esal__lte=15000)
    #employees=Employee1.objects.get(ename__exact="Keith Brown") # case sensetive
    #employees=Employee1.objects.get(ename__iexact="keith Brown") # not case sensetive
    #employees=Employee1.objects.filter(ename__contains="Dav") # case sensetive
    #employees=Employee1.objects.filter(ename__icontains="jo") # non-case sensetive
    #employees=Employee1.objects.filter(id__in=[10,20,50,12,11,44,55]) 
    #employees=Employee1.objects.filter(ename__startwith='o') #Unsupported lookup 'startwith' for CharField or join on the field not permitted, perhaps you meant startswith or istartswith?
    #employees=Employee1.objects.filter(ename__istartwith='k')#Unsupported lookup 'startwith' for CharField or join on the field not permitted, perhaps you meant startswith or istartswith?
    #employees=Employee1.objects.filter(ename__endswith='e')
    #employees=Employee1.objects.filter(ename__iendswith='y')
    #employees=Employee1.objects.filter(esal__range=(15000,16000))
    #employees=Employee1.objects.filter(esal__range=(15000,16000))|Employee1.objects.filter(ename__iendswith='y')
    #employees=Employee1.objects.filter (Q(esal__range=(15000,16000))|Q(ename__iendswith='y')) #or operation
    #employees=Employee1.objects.filter (Q(esal__range=(10000,16000)) & Q(ename__iendswith='y'))# and operation
    #employees=Employee1.objects.filter(Q(esal__range=(10000,18000),ename__iendswith='y')) # and operation
    #employees=Employee1.objects.filter(esal__range=(10000,18000)) & Employee1.objects.filter(ename__iendswith='y')# and operation
    #employees=Employee1.objects.exclude(esal__range=(10000,18000)) # excluding this range all record display
    #employees=Employee1.objects.filter(Q(esal__range=(10000,18000)))
    #employees=Employee1.objects.filter(~Q(esal__range=(10000,18000))) # this is same working as exclude
    #employees=Employee1.objects.exclude(ename__startswith='A')
    #employees=Employee1.objects.filter(Q(ename__startswith='N'))
    #employees=Employee1.objects.filter(Q(ename__startswith='a'))
    # qs1=Employee1.objects.filter(esal__lt=12000)
    # qs2=Employee1.objects.filter(ename__endswith='y')
    # employees=qs1.union(qs2)
    #employees=Employee1.objects.all().order_by('eno')
    # employees=Employee1.objects.all().order_by('-eno')
    # employees=Employee1.objects.all().order_by('-eno')[0:1] # first highest salary
    # employees=Employee1.objects.all().order_by('-eno')[0:2] # second highest salary
    # employees=Employee1.objects.all().order_by('-eno')[0:3] # top three highest salary
    #employees=Employee1.objects.all().order_by('ename')
    employees=Employee1.objects.all().order_by('-ename')
    # employees=Employee1.objects.all().order_by(Lower('ename'))
    print(type(employees))
    my_dict={'employees':employees}
    return render(request,'orm1app/index.html',my_dict)
    
    
    #Aggrigate functions

    # avg1=Employee1.objects.all().aggregate(Avg('esal'))
    # max=Employee1.objects.all().aggregate(Max('esal'))
    # min=Employee1.objects.all().aggregate(Min('esal'))
    # sum=Employee1.objects.all().aggregate(Sum('esal'))
    # count=Employee1.objects.all().aggregate(Count('esal'))
    # my_dict={'avg':avg1,'max':max,'min':min,'sum':sum,'count':count}
    # return render(request, 'orm1app/aggregate.html',my_dict)