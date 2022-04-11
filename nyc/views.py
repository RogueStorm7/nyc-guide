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
    # Here is the all-important venues data:
            'venues': boroughs[borough][activity].keys(),
        }
        
        # Return the http response with the rendered template.
        return render(
            request=request,
            template_name='activity.html',
            context=context,
        )
class VenueView(View): 
    
#The borough and activity and venue arguments are strings taken from the URL 
    def get (self, request, borough, activity,venue):
# Return the http response with the rendered template
        return render (
        request=request,
        template_name='venue.html',
# context is a dictionary that will be passed to the render function and will be available in the template
        context= {'borough': borough, 
        'activity': activity, 
        'venue': venue, 
        'description': boroughs[borough][activity][venue].get('description')})
        