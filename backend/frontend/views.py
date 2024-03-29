from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def base(request):
    return render (request,'index.html')

def index(request):
    return render(request,'index.html')


from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from .models import Customer
from django.views import View
from django.contrib.auth.hashers import make_password

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('home')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = " Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = ' First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = ' Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = ' Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = ' Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = ' Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = ' Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = ' Email must be 5 char long'
        elif customer.isExists ():
            error_message = ' Email Address Already Registered..'
        # saving

        return error_message
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')

def medicine(request):
    return render(request,'medicine.html')
def arthritis(request):
    return render(request,'artritis.html')
def Asthma(request):
    return render(request,'Asthma.html')


def Anxiet(request):
    return render(request,'Anxiet.html')

def Diabetes(request):
    return render(request,'Diabetes.html')

def Hypertension(request):
    return render(request,'Hypertension.html')

def Digestive(request):
    return render(request,'Digestive.html')

def Skin(request):
    return render(request,'Skin.html')

def Insomnia(request):
    return render(request,'Insomnia.html')

def Obesity(request):
    return render(request,'Obesity.html')

def Allergies(request):
    return render(request,'Allergies.html')

def Obesity(request):
    return render(request,'Obesity.html')


def info(request):
    return render(request,'info.html')



def Image(request):
    return render(request,'Image.html')