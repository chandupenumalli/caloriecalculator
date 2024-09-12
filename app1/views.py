from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Register,Message
from django.views.decorators.http import require_POST
def modify(request):
    operation=request.GET['operation']
    print(operation)
    return render(request,"viewusers.html",{"users":Register.objects.all()})
def index(request):
    return render(request,"index.html")
def viewusers(request):
    users=Register.objects.all()
    return render(request,"viewusers.html",{"users":users})
def about(request):
    return render(request,"about.html")
def login(request):
    return render(request,"login.html")
def contact(request):
    return render(request,"contact.html")
def userhome(request):
    return render(request,'userhome.html')
def adminhome(request):
    return render(request,'adminhome.html')
def register(request):
    return render(request,"register.html")
def doregister(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not fullname or not email or not password:
            messages.error(request, "Please fill all fields.")
        elif Register.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
        else:
            Register.objects.create(name=fullname, email=email, password=password)
            messages.success(request, "Registration Success....")
            return redirect('register')

    # Render the form with any error messages
    return render(request, "register.html")
def logincheck(request):
    if request.method == 'POST':
        # Retrieve form data
        email = request.POST.get('username', '').strip()
        password = request.POST.get('pass', '').strip()

        # Check if fields are empty
        if not email or not password:
            return render(request, "login.html", {"msg": "Please fill the details"})
        
        try:
            # Validate user credentials
            r = Register.objects.get(email=email, password=password)
        except Register.DoesNotExist:
            return render(request, "login.html", {"msg": "Invalid Email/Password"})
        
        # Redirect based on designation
        if r.desig == 'user':
            return redirect('/userhome')
        elif r.desig == 'admin':
            return redirect('/adminhome')
        else:
            return render(request, 'login.html', {"msg": "Invalid Designation"})
    else:
        return redirect('/')
def adminhome(request):
    users = Register.objects.all()
    return render(request, 'adminhome.html', {'users': users})

@require_POST
def modify(request):
    operation = request.POST.get('operation')
    email = request.POST.get('email')

    if operation == 'update':
        # Update operation
        try:
            user = Register.objects.get(email=email)
            user.name = request.POST.get('fullname')
            user.password = request.POST.get('password')
            user.desig = request.POST.get('desig')
            user.save()
        except Register.DoesNotExist:
            pass  # Handle the case where user does not exist
    elif operation == 'delete':
        # Delete operation
        try:
            user = Register.objects.get(email=email)
            user.delete()
        except Register.DoesNotExist:
            pass  # Handle the case where user does not exist

    return redirect('viewusers')  # Redirect back to adminhome after operation
def contactmessage(request):
    fullname=request.GET['name']
    Phone=request.GET['Phone']
    email=request.GET['email']
    message=request.GET['message']
    v=Message()
    v.name=fullname
    v.Phone=Phone
    v.email=email
    v.message=message
    v.save()
    return render(request,"contact.html",{"msg":"Message Sent Successfully"})
