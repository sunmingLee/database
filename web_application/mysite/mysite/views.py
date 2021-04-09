from django.shortcuts import render
import pickle
import lightgbm

# our home page view
def input(request):    
    return render(request, 'input.html')

def getPredictions(Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness, Department, Type_of_Admission):
    model = pickle.load(open("./mysite/code_final.sav", "rb"))
    scaled = pickle.load(open("./mysite/scaler_final.sav", "rb"))

    Visitors_with_Patient = getVisitors(Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness,Department, Type_of_Admission)
    prediction = model.predict(scaled.transform([[Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness, Visitors_with_Patient, Department, Type_of_Admission]]))
    if prediction >= 0:
        return prediction
    else:
        return "error"

def getVisitors(Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness, Department, Type_of_Admission):
    Visitors_with_Patient = pickle.load(open("./mysite/V_code_final.sav", "rb"))
    V_scaled = pickle.load(open("./mysite/V_scaler_final.sav", "rb"))
    number = Visitors_with_Patient.predict(V_scaled.transform([[Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness, Department, Type_of_Admission]]))
    
    if number >= 0:
        return number
    else:
        return "error" 


# our result page view
def result(request):
    Age = int(request.GET['Age'])
    Available_Extra_Rooms_in_HosPital = int(request.GET['Available_Extra_Rooms_in_HosPital'])
    Admission_Deposit = int(request.GET['Admission_Deposit'])
    Severity_of_Illness = int(request.GET['Severity_of_Illness'])

    Department = int(request.GET['department'])
    Type_of_Admission = int(request.GET['admission'])
    result = getPredictions(Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness, Department, Type_of_Admission)

    return render(request, 'result.html', {'result':result, 'department':Department, 'admission':Type_of_Admission})

def bad_request(request, exception):
    return render(request, 'error_400.html', status = 400)

def page_not_found(request, exception):
    return render(request, 'error_404.html', status = 404)

def server_error(request):
    return render(request, 'error_500.html', status = 500)
    
def index(request):
   return render(request, 'index.html')

def map(request):
   return render(request, 'map.html')

def contact(request):
   return render(request, 'contact.html')


