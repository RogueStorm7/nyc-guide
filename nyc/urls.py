from django.urls import path

from nyc.views import CityView, BoroughView, ActivityView, VenueView

urlpatterns = [
    # all the urls are for free
    path('', CityView.as_view(), name='city'),
    path('<str:borough>', BoroughView.as_view(), name='borough'),
    path('<str:borough>/<str:activity>', ActivityView.as_view(), name='activity'),
    path('<str:borough>/<str:activity>/<str:venue>', VenueView.as_view(), name='venue')
]
