from django.shortcuts import render

def renderTemplate(request):
    myDict={"name":"Plaifah"}
    return render(request, 
    'templatesApp/firstTemplate.html',context=myDict)

def renderEmployee(request): 
    myDict={"id":6604101349,"name":"ปลายฟ้า สูงดี","salary":10000}
    return render(request, 
    'templatesApp/employeeTemplate.html',context=myDict)
# Create your views here.
