from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):
    # The borough and activity arguments are strings taken from the URL
    def get(self, request, borough, activity):
        # context is a dictionary that will be passed to the render function and will be available in the template
        context= {
            'borough': borough, 
            'activity': activity,
        }

        return render(
            request=request,
            template_name='activity.html',
            context=context,
        )
    pass


class VenueView(View):
    pass
