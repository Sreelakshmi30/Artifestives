from django.urls import path

from Arts_App.club_views import IndexView, Add_Events, Add_Album, View_events, View_Participant, View_Scheduledtime

urlpatterns = [

    path('',IndexView.as_view()),
    path('Add_Events', Add_Events.as_view()),
    path('Add_Album',Add_Album.as_view()),
    path('View_events',View_events.as_view()),
    path('participant',View_Participant.as_view()),
    path('setime',View_Scheduledtime.as_view())

]
def urls():
    return urlpatterns, 'club','club'