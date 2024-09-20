from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from ethio_leap_gui_app.models import SensorsData
from datetime import *
from dateutil.relativedelta import *
import calendar
from django.db.models import F
from django.contrib.auth.decorators import login_required

# Create your views here.
user = get_user_model()

#@login_required
def data_visualization(request):
    return render(request, 'data_visualization/data.html')

def get_data(request):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)

class ChartData(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [1234, 1222, 1211, 2333, 3333, 3422]
        data = {
        "labels": labels,
        "default": default_items,
        "users":user.objects.all().count(),
    }
        
        return Response(data)

# Temperature data visualization

class OneMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+1)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['Temprature']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "temp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)


class TwoMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+2)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        qurey = labels[0]['Temprature']
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['Temprature']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "temp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)

class ThreeMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
            
            
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+3)
        sensorData = list(SensorsData.objects.all().order_by('id').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        qurey = labels[0]['Temprature']
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['Temprature']))
            countT = countT - 1
            
        data = {
            "labels": timeStamp,
            "temp": ec,
            "users":user.objects.all().count(),
            "current": current_time,
            "previous":labels,
        }
            
        return Response(data)

# Humidity data vizualization
#@login_required
def humidity(request):
    return render(request, 'data_visualization/humidity.html')

class HumidityOneMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+1)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['Humidity']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "humid": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)


class HumidityTwoMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+2)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['Humidity']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "disp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)

class HumidityThreeMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
            
            
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+3)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
       
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['Humidity']))
            countT = countT - 1
            
        data = {
            "labels": timeStamp,
            "disp": ec,
            "users":user.objects.all().count(),
            "current": current_time,
            "previous":labels,
        }
            
        return Response(data)

# PH data visualaization

#@login_required
def ph(request):
    return render(request, 'data_visualization/ph.html')

class phOneMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+1)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['PH']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "disp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)


class PhTwoMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+2)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['PH']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "disp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)

class PhThreeMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
            
            
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+3)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
       
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['PH']))
            countT = countT - 1
            
        data = {
            "labels": timeStamp,
            "disp": ec,
            "users":user.objects.all().count(),
            "current": current_time,
            "previous":labels,
        }
            
        return Response(data)

# EC data visualization
#@login_required
def ec(request):
    return render(request, 'data_visualization/ec.html')

class EcOneMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+1)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['EC']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "disp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)


class EcTwoMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+2)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['EC']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "disp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)

class EcThreeMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
            
            
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+3)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
       
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['EC']))
            countT = countT - 1
            
        data = {
            "labels": timeStamp,
            "disp": ec,
            "users":user.objects.all().count(),
            "current": current_time,
            "previous":labels,
        }
            
        return Response(data)

# PH data visualaization
#@login_required

def ec(request):
    return render(request, 'data_visualization/ec.html')

class phOneMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+1)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['PH']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "disp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)


class PhTwoMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+2)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
        
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['PH']))
            countT = countT - 1
        
        data = {
        "labels": timeStamp,
        "disp": ec,
        "users":user.objects.all().count(),
        "current": current_time,
        "previous":labels,
    }
        
        return Response(data)

class PhThreeMonths(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
            
            
        current_time = datetime.now()
        two_months = current_time - relativedelta(months=+3)
        sensorData = list(SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values())
        labels = SensorsData.objects.filter(TimeStamp__lte=current_time, TimeStamp__gte=two_months).order_by('TimeStamp').values()
       
        ec = []
        timeStamp = []
        count = len(sensorData) - 1
        countT = len(sensorData) - 1


        while(count >= 0 ):
            timeStamp.append(sensorData[count]['TimeStamp'])
            count = count - 1

        while(countT >= 0 ):
            ec.append(float(sensorData[countT]['PH']))
            countT = countT - 1
            
        data = {
            "labels": timeStamp,
            "disp": ec,
            "users":user.objects.all().count(),
            "current": current_time,
            "previous":labels,
        }
            
        return Response(data)



