from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from Arts_App.models import Club, User_reg, UserType, Events, Category, Schedule_time, Feedback, Competition


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class Add_category(TemplateView):
    template_name = 'admin/club_category.html'
    def post(self, request, *args, **kwargs):
        category=request.POST['category']
        se=Category()
        se.category=category
        se.save()
        return render(request, 'admin/admin_index.html', {'message': "Club category Added"})


class Club_Registration(TemplateView):
    template_name = 'admin/club_registration.html'

    def get_context_data(self, **kwargs):
        context = super(Club_Registration, self).get_context_data(**kwargs)
        categ = Category.objects.all()
        context['categ'] = categ
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        category=request.POST['category']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'admin/club_registration.html', {'message': "already added the username or email"})

        else:
            user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                             is_staff='0', last_name='1')
            user.save()
            us = Club()
            us.user=user
            us.categ_id=category
            us.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "club"
            usertype.save()
            return render(request, 'admin/admin_index.html', {'message': "successfully added"})

class User_Approvel(TemplateView):
    template_name = 'admin/user_approval.html'

    def get_context_data(self, **kwargs):
        context = super(User_Approvel,self).get_context_data(**kwargs)

        user = User_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['user'] = user
        return context




class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})



class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Rejected"})

class View_Event(TemplateView):
    template_name = 'admin/event_approve.html'

    def get_context_data(self, **kwargs):
        context = super(View_Event, self).get_context_data(**kwargs)
        event_view = Events.objects.filter(status='pending')
        context['event_view'] = event_view
        return context


class Approve_Event(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        accept = Events.objects.get(pk=id)
        accept.status = 'Approve'
        accept.save()
        return render(request, 'admin/admin_index.html', {'message': "Approve"})


class Reject_Event(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        reject = Events.objects.get(pk=id)
        reject.status = 'Reject'
        reject.save()
        return render(request, 'admin/admin_index.html', {'message': "Reject"})

class Event_view(TemplateView):
    template_name = 'admin/events.html'
    def get_context_data(self, **kwargs):
        context = super(Event_view, self).get_context_data(**kwargs)
        event = Events.objects.filter(status='Approve')
        context['event'] = event
        return context

class Scheduled_view(TemplateView):
    template_name = 'admin/practice_time.html'
    def get_context_data(self, **kwargs):
        context = super(Scheduled_view, self).get_context_data(**kwargs)
        event = Schedule_time.objects.all()
        context['event'] = event
        return context


class Time_Schedule(TemplateView):
    template_name = 'admin/time_schedule.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(Time_Schedule, self).get_context_data(**kwargs)
        event = Events.objects.get(id=id)
        context['event'] = event
        return context
    def post(self, request, *args, **kwargs):
        id=request.POST['id']
        id2 = request.POST['id2']
        starttime = request.POST['starttime']
        endtime=request.POST['endtime']
        practicedate = request.POST['practicedate']
        se=Schedule_time()
        se.club_id=id2
        se.starttime=starttime
        se.endtime=endtime
        se.practicedate=practicedate
        se.event_id=id
        se.save()
        return render(request, 'admin/admin_index.html', {'message': "successfully added"})

class update_schedule(TemplateView):
    template_name = 'admin/re_schedule.html'

    def get_context_data(self, **kwargs):
        context = super(update_schedule, self).get_context_data(**kwargs)
        try:
            id = self.request.GET['id']
            m = Schedule_time.objects.get(event_id=id)
            print("2222222222222222222222222222222", m)
            print("qqqqqqqqqqqq", m)
            context['m'] = m
            return context
        except:
            pass
    def post(self, request, *args, **kwargs):

        id = request.POST['id']
        ev = Schedule_time.objects.get(id=id)
        c = Events.objects.get(id=ev.event_id)

        id2 = request.POST['id2']
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        practicedate = request.POST['practicedate']
        se = Schedule_time.objects.get(id=id)
        se.club_id = id2
        se.starttime = starttime
        se.endtime = endtime
        se.practicedate = practicedate
        se.event_id = c.id
        se.save()
        return render(request, 'admin/admin_index.html', {'message': "re"})




class View_Feedback(TemplateView):
    template_name = 'admin/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(View_Feedback, self).get_context_data(**kwargs)

        feed = Feedback.objects.filter(status='added')

        context['feed'] = feed
        return context

    def post(self, request, *args, **kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        action = request.POST['action']
        act = Feedback.objects.get(id=id)
        # act.complaint=complaint
        act.action = action

        act.status = 'replied'
        act.save()

        return render(request, 'admin/admin_index.html', {'message': "Replyed"})

class Club_View(TemplateView):
    template_name = 'admin/view_club.html'
    def get_context_data(self, **kwargs):
        context = super(Club_View,self).get_context_data(**kwargs)

        club = Club.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['club'] = club
        return context

class Delete_Club(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        id1 = request.GET['userid']

        Club.objects.get(id=id).delete()
        User.objects.get(id=id1).delete()

        return render(request, 'admin/admin_index.html', {'message': "Replyed"})

class Add_competition(TemplateView):
    template_name = 'admin/add_competition.html'
    def post(self, request, *args, **kwargs):
        number = request.POST['number']
        ctnumber=request.POST['ctnumber']
        ctname = request.POST['ctname']
        duration = request.POST['duration']
        se=Competition()
        se.number=number
        se.count=number
        se.ctnumber=ctnumber
        se.duration=duration
        se.ctname=ctname
        se.save()
        return render(request, 'admin/admin_index.html', {'message': "successfully added"})