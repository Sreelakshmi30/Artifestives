from django.urls import path

from Arts_App.admin_views import IndexView, Club_Registration, User_Approvel, ApproveView, RejectView, View_Event, \
    Approve_Event, Reject_Event, Add_category, Event_view, Time_Schedule, View_Feedback, Delete_Club, Club_View, \
    Add_competition, update_schedule, Scheduled_view

urlpatterns = [

    path('',IndexView.as_view()),
    path('club_reg',Club_Registration.as_view()),
    path('User_Approvel',User_Approvel.as_view()),
    path('Approve',ApproveView.as_view()),
    path('Reject',RejectView.as_view()),
    path('View_Event',View_Event.as_view()),
    path('approve',Approve_Event.as_view()),
    path('Reject',Reject_Event.as_view()),
    path('categ',Add_category.as_view()),
    path('Event_view',Event_view.as_view()),
    path('Time_Schedule',Time_Schedule.as_view()),
    path('View_Feedback',View_Feedback.as_view()),
    path('Club_View',Club_View.as_view()),
    path('delete',Delete_Club.as_view()),
    path('Add_competition',Add_competition.as_view()),
    path('update',update_schedule.as_view()),
    path('Scheduled_view',Scheduled_view.as_view())


]
def urls():
    return urlpatterns, 'admin','admin'