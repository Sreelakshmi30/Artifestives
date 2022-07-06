from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView

from Arts_App.models import Events, Club, Albums, Event_Participant, Schedule_time


class IndexView(TemplateView):
    template_name = 'club/club_index.html'

class Event_view(TemplateView):
    template_name = 'admin/events.html'
    def get_context_data(self, **kwargs):
        context = super(Event_view, self).get_context_data(**kwargs)
        event = Events.objects.filter(status='Approve')
        context['event'] = event
        return context


class Add_Events(TemplateView):
    template_name = 'club/add_events.html'


    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        club1 = Club.objects.get(user_id=self.request.user.id)

        name = request.POST['eventname']
        venue = request.POST['venue']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        date = request.POST['date']
        time=request.POST['time']
        se=Events()
        se.user=user
        se.club=club1
        se.eventname=name
        se.date=date
        se.image=filesss
        se.time=time
        se.status='pending'
        se.venue=venue
        se.save()
        return render(request, 'club/club_index.html', {'message': "successfully added"})


class Add_Album(TemplateView):
    template_name = 'club/add_albums.html'


    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        club1 = Club.objects.get(user_id=self.request.user.id)
        name = request.POST['name']
        desc = request.POST['desc']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        se=Albums()
        se.user=user
        se.club=club1
        se.name=name
        se.desc=desc
        se.image=filesss
        se.save()
        return render(request, 'club/club_index.html', {'message': "successfully added"})

class View_events(TemplateView):
    template_name = 'club/view_events.html'
    def get_context_data(self, **kwargs):
        context = super(View_events, self).get_context_data(**kwargs)
        event = Events.objects.filter(user_id=self.request.user.id)
        context['event'] = event
        return context

class View_Participant(TemplateView):
    template_name = 'club/view_participant.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(View_Participant, self).get_context_data(**kwargs)
        event = Event_Participant.objects.filter(event_id=id)
        context['event'] = event
        return context

class View_Scheduledtime(TemplateView):
    template_name = 'club/practice_time.html'

    def get_context_data(self, **kwargs):

        id = self.request.user.id

        context = super(View_Scheduledtime, self).get_context_data(**kwargs)
        user = Club.objects.get(user_id=id)
        club = user.id
        event = Schedule_time.objects.filter(club_id=club)
        context['event'] = event
        return context

    def post(self, request, *args, **kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        action = request.POST['action']
        act = Schedule_time.objects.get(id=id)
        # act.complaint=complaint
        act.action = action

        act.save()

        return render(request, 'club/club_index.html', {'message': "successfully added"})
