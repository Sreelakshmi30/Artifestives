from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Arts_App.user_views import Indexview, Event_View, Albums_view, Add_cart, View_Cart, Payment, chpayment, Event_part, \
    Priactice_time, Feedback, Add_Feedback, Feedback_Replay, Add_Talents, Talents_view, Competition_view, \
    Add_parti_competition, Profile_view

urlpatterns = [

    path('',Indexview.as_view()),
    path('Event_View',Event_View.as_view()),
    path('Albums_view',Albums_view.as_view()),
    path('add_cart',Add_cart.as_view()),
    path('View_Cart',View_Cart.as_view()),
    path('payment',Payment.as_view()),
    path('chpayment',chpayment.as_view()),
    path('Event_part',Event_part.as_view()),
    path('time',Priactice_time.as_view()),
    path('Feedback',Add_Feedback.as_view()),
    path('Feedback_Replay',Feedback_Replay.as_view()),
    path('Add_Talents',Add_Talents.as_view()),
    path('Talents_view',Talents_view.as_view()),
    path('Competition_view',Competition_view.as_view()),
    path('participate',Add_parti_competition.as_view()),
    path('Profile_view',Profile_view.as_view())



]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def urls():
    return urlpatterns, 'user','user'