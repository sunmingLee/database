from django.shortcuts import render
import pickle
import lightgbm

# our home page view
def input(request):    
    return render(request, 'input.html')

def getPredictions(Department, Type_of_Admission, Severity_of_Illness, Available_Extra_Rooms_in_HosPital, Age,Admission_Deposit):
    model = pickle.load(open("./mysite/code_final.sav", "rb"))
    scaled = pickle.load(open("./mysite/scaler_final.sav", "rb"))

    visitors = getVisitors(Department, Type_of_Admission, Severity_of_Illness, Available_Extra_Rooms_in_HosPital, Age, Admission_Deposit)
    prediction = model.predict(scaled.transform([[Department, Type_of_Admission, visitors, Severity_of_Illness, Available_Extra_Rooms_in_HosPital, Age,Admission_Deposit]]))
    
    if prediction >= 0:
        return prediction
    else:
        return "error"
        
def getVisitors(Department, Type_of_Admission, Severity_of_Illness, Available_Extra_Rooms_in_HosPital, Age, Admission_Deposit):
    visitors = pickle.load(open("./mysite/V_code_final.sav", "rb"))
    scaler = pickle.load(open("./mysite/V_scaler_final.sav", "rb"))
    number = visitors.predict(scaler.transform([[Department, Type_of_Admission, Severity_of_Illness, Available_Extra_Rooms_in_HosPital, Age, Admission_Deposit]]))
    
    if number >= 0:
        return number
    else:
        return "error"
        

# our result page view
def result(request):
    Age = int(request.GET['Age'])
    Available_Extra_Rooms_in_HosPital = int(request.GET['Available_Extra_Rooms_in_HosPital'])
    Admission_Deposit = int(request.GET['Admission_Deposit'])
    Severity_of_Illness = int(request.GET['severity'])
    Department = int(request.GET['department'])
    Type_of_Admission = int(request.GET['admission'])

    result = getPredictions(Department, Type_of_Admission, Severity_of_Illness, Available_Extra_Rooms_in_HosPital, Age,Admission_Deposit)
    visitors = getVisitors(Department, Type_of_Admission, Severity_of_Illness, Available_Extra_Rooms_in_HosPital, Age, Admission_Deposit)
    return render(request, 'result.html', {'result':result,'visitors':visitors})

# def bad_request(request, exception):
#     return render(request, 'error_400.html', status = 400)

def page_not_found(request):
    return render(request, 'error_404.html', status = 500)

# def server_error(request):
#     return render(request, 'error_500.html', status = 500)
    
def index(request):
   return render(request, 'index.html')

def map(request):
   return render(request, 'map.html')

def contact(request):
   return render(request, 'contact.html')


