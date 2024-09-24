from django.shortcuts import render
from django.http import HttpResponse
from .models import SensorsData, ControlParameters, Relays, DutchBucketOne, DutchBucketTwo, SeedlingControl
from datetime import datetime
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

@login_required
def dashboard(request):
    return render(request,
                  'registration/account/dashboard.html',
                  {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home.html')
                else:
                    return HttpResponse('fuck Invalid login')
                    #return render(request, 'home.html')
            else:
                return HttpResponse('Invalid login')
                #return render(request, 'home.html')
    else:
        form= LoginForm()
    return render(request, 'account/login.html', {'form': form})
    #return render(request, 'home.html')

@login_required
def home_page(request):
    return render(request, 'home.html') 

@login_required # decorator for views that checks the user is logd in if not redirect it to login page
def sensor_display(request):
    sensorData = SensorsData.objects.all().order_by('id')
    count = sensorData.count()
    sensorDisplay = sensorData[count-1]
    return render(request, 'sensor_data/sensor_display.html', {'sensorsdata': sensorDisplay})

@login_required
def parameters(request):
    return render(request, 'parameters/index.html')

@login_required
def enviroment_control(request):

    controlParameters = ControlParameters.objects.all()[0]

    if request.method == 'POST':  
              
        temp_Min = request.POST['Temp_Min']
        temp_Max = request.POST['Temp_Max']
        humidity_Min = request.POST['Humidity_Min']
        humidity_Max = request.POST['Humidity_Max']    

        controlParameters.TimeStamp = datetime.now()
        controlParameters.Temperature_Min = temp_Min
        controlParameters.Temperature_Max = temp_Max
        controlParameters.Humidity_Min = humidity_Min
        controlParameters.Humidity_Max = humidity_Max
        
        controlParameters.save()    

    return render(request, 'parameters/enviroment_control.html', {'controlParameters':controlParameters})

@login_required
def nft_system(request):

    nftSystem = ControlParameters.objects.all()[0]

    if request.method == 'POST':  
              
        ph_Min = request.POST['PH_Min']
        ph_Max = request.POST['PH_Max']
        ec_Min = request.POST['EC_Min']
        ec_Max = request.POST['EC_Max']    
        
        nftSystem.TimeStamp = datetime.now()
        nftSystem.PH_Min = ph_Min
        nftSystem.PH_Max = ph_Max
        nftSystem.EC_Min = ec_Min
        nftSystem.EC_Max = ec_Max
        
        nftSystem.save()

    nftSystem = ControlParameters.objects.all()[0]  

    return render(request, 'parameters/nft_system.html', {'nftData': nftSystem})

@login_required
def relays(request):

    relays = Relays.objects.all()[0]

    if request.method == 'POST':
               
        relay1 = request.POST['Relay1']
        relay2 = request.POST['Relay2']
        relay3 = request.POST['Relay3']
        relay4 = request.POST['Relay4']
        relay5 = request.POST['Relay5']
        relay6 = request.POST['Relay6']
        relay7 = request.POST['Relay7']
        relay8 = request.POST['Relay8']      
        
        relays.TimeStamp = datetime.now()
        relays.Relay1 = relay1
        relays.Relay2 = relay2
        relays.Relay3 = relay3
        relays.Relay4 = relay4
        relays.Relay5 = relay5
        relays.Relay6 = relay6
        relays.Relay7 = relay7
        relays.Relay8 = relay8

        relays.save()

    relays = Relays.objects.all()[0]
      

    return render(request, 'relays/index.html', {'relaysData': relays})

@login_required
def ducth_bucket_1(request):

    dutch_bucket_data = DutchBucketOne.objects.all()[0]   

    if request.method == 'POST':

        first_feed = request.POST['firstFeed']
        second_feed = request.POST['secondFeed']
        third_feed = request.POST['thirdFeed']
        feed_duration = request.POST['feedDuration']

        dutch_bucket_data.TimeStamp = datetime.now()
        dutch_bucket_data.FirstFeedStart = datetime.strptime(first_feed, "%I:%M:%S %p").time()            
        dutch_bucket_data.SecondFeedStart = datetime.strptime(second_feed, "%I:%M:%S %p").time()
        dutch_bucket_data.ThirdFeedStart = datetime.strptime(third_feed, "%I:%M:%S %p").time()
        dutch_bucket_data.FeedDuration = feed_duration
       
        dutch_bucket_data.save()   
    

    dutch_bucket_data = DutchBucketOne.objects.all()[0]


    return render(request, 'parameters/dutch_bucket_1.html', {'dutch_bucket_1_data': dutch_bucket_data})

@login_required
def ducth_bucket_2(request):

    dutch_bucket_data = DutchBucketTwo.objects.all()[0]   

    if request.method == 'POST':

        first_feed = request.POST['firstFeed']
        second_feed = request.POST['secondFeed']
        third_feed = request.POST['thirdFeed']
        feed_duration = request.POST['feedDuration']

        dutch_bucket_data.TimeStamp = datetime.now()
        dutch_bucket_data.FirstFeedStart = datetime.strptime(first_feed, "%I:%M:%S %p").time()            
        dutch_bucket_data.SecondFeedStart = datetime.strptime(second_feed, "%I:%M:%S %p").time()
        dutch_bucket_data.ThirdFeedStart = datetime.strptime(third_feed, "%I:%M:%S %p").time()
        dutch_bucket_data.FeedDuration = feed_duration
       
        dutch_bucket_data.save()   
    

    dutch_bucket_data = DutchBucketTwo.objects.all()[0]


    return render(request, 'parameters/dutch_bucket_2.html', {'dutch_bucket_2_data': dutch_bucket_data})
@login_required
def seedling(request):

    seedling_data = SeedlingControl.objects.all()[0]   

    if request.method == 'POST':

        first_feed = request.POST['firstFeed']
        second_feed = request.POST['secondFeed']
        third_feed = request.POST['thirdFeed']
        feed_duration = request.POST['feedDuration']

        seedling_data.TimeStamp = datetime.now()
        seedling_data.FirstFeedStart = datetime.strptime(first_feed, "%I:%M:%S %p").time()            
        seedling_data.SecondFeedStart = datetime.strptime(second_feed, "%I:%M:%S %p").time()
        seedling_data.ThirdFeedStart = datetime.strptime(third_feed, "%I:%M:%S %p").time()
        seedling_data.FeedDuration = feed_duration
       
        seedling_data.save()   
    

    seedling_data = SeedlingControl.objects.all()[0]

    
    return render(request, 'parameters/seedling.html', {'seedling_data': seedling_data})

def get_data(request):
    return JsonResponse()
    
def api(request):
    if request.method == 'POST':
        response =request.url 
        api_key = response.request.params['api_key']

        if api_key == 0:
            return HttpResponse('api key is correct')
        else: 
            return HttpResponse('wrong api key')

    return HttpResponse('no data')