from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from Arts_App.models import UserType, Club, User_reg


class IndexView(TemplateView):
    template_name = 'index.html'


class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "club":
                    return redirect('/club')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                # elif UserType.objects.get(user_id=user.id).type == "accounts":
                #     return redirect('/accounts')

            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})


class User_Reg(TemplateView):
    template_name = 'user_registration.html'

    def get_context_data(self, **kwargs):

        context = super(User_Reg,self).get_context_data(**kwargs)
        club_view = Club.objects.all()
        context['club_view'] = club_view
        return context

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        club=request.POST['club']
        address=request.POST['address']
        phonenumber=request.POST['phonenumber']
        email= request.POST['email']
        empid= request.POST['empid']
        dept= request.POST['dept']
        desig= request.POST['desig']

        password = request.POST['password']
        if User.objects.filter(email=email):
            print ('pass')
            return render(request,'user_registration.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            us = User_reg()
            us.empid=empid
            us.dept=dept
            us.desig=desig
            us.user=user
            us.club_id=club
            us.phonenumber=phonenumber
            us.address=address
            us.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            return render(request, 'index.html', {'message':"successfully added"})