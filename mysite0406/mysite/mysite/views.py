from django.shortcuts import render

# our home page view
def input(request):    
    return render(request, 'input.html')


# custom method for generating predictions
def getPredictions(Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness):
    import pickle
    import lightgbm
    model = pickle.load(open("./mysite/code_modified.sav", "rb"))
    scaled = pickle.load(open("./mysite/scaler_simple.sav", "rb"))
    prediction = model.predict(scaled.transform([[Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness]]))
    
    if prediction >= 0:
        return prediction
    else:
        return "error"
        

# our result page view
def result(request):
    Age = int(request.GET['Age'])
    Available_Extra_Rooms_in_HosPital = int(request.GET['Available_Extra_Rooms_in_HosPital'])
    Admission_Deposit = int(request.GET['Admission_Deposit'])
    Severity_of_Illness = int(request.GET['Severity_of_Illness'])

    result = getPredictions(Age,Available_Extra_Rooms_in_HosPital, Admission_Deposit, Severity_of_Illness)
    # depart = request.POST.getlist['department']
    # department = depart[0]
    # admission = request.POST['admission']
   
    department = request.GET.getlist('department',"")
    admission = request.GET.getlist('admission',"")
     
    return render(request, 'result.html', {'result':result, 'department':department, 'admission':admission})

def index(request):
   return render(request, 'index.html')

def map(request):
   return render(request, 'map.html')

def contact(request):
   return render(request, 'contact.html')

def my_view(request):
    if request.method == 'POST':
        selected = request.POST.getlist('radio')
        print(selected)

    return redirect(...)