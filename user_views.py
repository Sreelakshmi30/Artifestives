
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from Arts_App.models import Events, Albums, Club, Add_Cart, User_reg, Event_Participant, Schedule_time, Feedback, \
    Talents, Competition, Competi_Participant


class Indexview(TemplateView):
    template_name = 'user/user_index.html'

class Event_View(TemplateView):
    template_name = 'user/events.html'
    def get_context_data(self, **kwargs):
        id =self.request.user.id

        context = super(Event_View, self).get_context_data(**kwargs)
        user = User_reg.objects.get(user_id=id)
        club=user.club_id

        view_pp = Events.objects.filter(club_id=club,status='Approve')
        context['view_pp'] = view_pp
        return context


class Albums_view(TemplateView):
    template_name = 'user/albums_view.html'
    def get_context_data(self, **kwargs):
        context = super(Albums_view, self).get_context_data(**kwargs)
        view_pp = Albums.objects.all()
        context['view_pp'] = view_pp
        return context



class Add_cart(TemplateView):
    template_name = 'user/albums_view.html'

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        id = self.request.GET['id']
        album = Albums.objects.get(pk=id)
        club = Club.objects.get(id=album.club_id)

        ca = Add_Cart()
        ca.club_id = club.id

        ca.user_id = user.id
        ca.album_id = id
        ca.status = 'cart'
        ca.payment='null'
        ca.save()


        return render(request, 'user/user_index.html', {'message': "Add to cart"})



class View_Cart(TemplateView):
    template_name = 'user/cart.html'

    def get_context_data(self, **kwargs):
        context = super(View_Cart, self).get_context_data(**kwargs)
        cr = self.request.user.id
        ct = Add_Cart.objects.filter(status='cart', user_id=cr)

        total = 0
        for i in ct:
            total = total + int(i.album.price)

        context['ct'] = ct
        context['asz'] = total

        return context

class Payment(TemplateView):
    template_name = 'user/payment.html'

    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)
        cr = self.request.user.id
        ct = Add_Cart.objects.filter(status='cart', user_id=cr)

        total = 0
        for i in ct:
            total = total + int(i.album.price)

        context['ct'] = ct
        context['asz'] = total

        return context

class chpayment(TemplateView):
    def dispatch(self,request,*args,**kwargs):

        pid = self.request.user.id


        ch = Add_Cart.objects.filter(user_id=pid,status='cart')


        print(ch)
        for i in ch:
            i.payment='paid'
            i.status='paid'
            i.save()
        return render(request,'user/user_index.html',{'message':" payment Success"})

class Event_part(TemplateView):
    template_name = 'user/albums_view.html'

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        id = self.request.GET['id']
        event = Events.objects.get(pk=id)
        club = Club.objects.get(id=event.club_id)

        ca = Event_Participant()
        ca.club_id = club.id

        ca.user_id = user.id
        ca.event_id = id
        ca.status = 'added'
        ca.save()


        return render(request, 'user/user_index.html', {'message': "Add to Participate"})

class Priactice_time(TemplateView):
    template_name = 'user/practice_time.html'
    def get_context_data(self, **kwargs):

        id = self.request.user.id

        context = super(Priactice_time, self).get_context_data(**kwargs)
        user = User_reg.objects.get(user_id=id)
        club = user.club_id
        event = Schedule_time.objects.filter(club_id=club)
        context['event'] = event
        return context

class Add_Feedback(TemplateView):
    template_name = 'user/feedback.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)

        subject = request.POST['subject']
        message = request.POST['message']
        fe = Feedback()
        fe.user = user

        fe.subject = subject
        fe.message = message
        fe.status='added'
        fe.save()
        return render(request, 'user/user_index.html', {'message': "Feedback Added"})

class Feedback_Replay(TemplateView):
    template_name = 'user/feedback_replay.html'
    def get_context_data(self, **kwargs):

        context = super(Feedback_Replay, self).get_context_data(**kwargs)
        usid = self.request.user.id
        reply = Feedback.objects.filter(status='replied', user_id=usid,)

        context['reply'] = reply
        return context

class Add_Talents(TemplateView):
    template_name = 'user/talents.html'

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)

        name = request.POST['name']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        desc = request.POST['desc']
        se=Talents()
        se.user=user
        se.talentname=name
        se.image=filesss
        se.desc=desc
        se.save()
        return render(request, 'user/user_index.html', {'message': "successfully added"})

class Talents_view(TemplateView):
    template_name = 'user/view_talents.html'
    def get_context_data(self, **kwargs):
        context = super(Talents_view, self).get_context_data(**kwargs)
        view_pp = Talents.objects.all()
        context['view_pp'] = view_pp
        return context

class Competition_view(TemplateView):
    template_name = 'user/competition_view.html'
    def get_context_data(self, **kwargs):
        context = super(Competition_view, self).get_context_data(**kwargs)
        view_pp = Competition.objects.all()
        context['view_pp'] = view_pp
        return context


class Add_parti_competition(TemplateView):
    template_name = 'customer/competition_view.html'
    def dispatch(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        pid = request.GET['id']
        com = Competition.objects.get(pk=pid)
        count=com.count
        if Competi_Participant.objects.filter(user_id=user,competition_id=com):
            return render(request, 'user/user_index.html', {'message': "already done"})
        else:

            if count==0:
                return render(request, 'user/user_index.html', {'message': "filled"})
            else:

                ca = Competi_Participant()

                ca.user = User.objects.get(id=self.request.user.id)
                ca.competition = Competition.objects.get(pk=pid)
                ca.status = 'added'
                ca.save()
                count=com.count
                com.count=int(count)- 1
                com.save()
                return render(request, 'user/user_index.html', {'message': "successfully Added"})

class Profile_view(TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        cr = self.request.user.id
        context = super(Profile_view, self).get_context_data(**kwargs)
        employee = User_reg.objects.get(user_id=cr)

        context['employee'] = employee
        return context