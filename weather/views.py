from django.shortcuts import render
import json #when we send a request to the API, it will give us a response in a JSON format
# Create your views here.
import urllib.request
def index(request):
  if request.method == 'POST':
    city = request.POST['city'].title() #the name that we put in the input
    res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=aa329b8063c87fb6687a243bc64f707c').read() # res is request sending to open weather map, q means query
    json_data = json.loads(res)
    data = {
      "country_code": str(json_data['sys']['country']),
      "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
      "temp": str(json_data['main']['temp']) + 'K',
      "pressure": str(json_data['main']['pressure']),
      "humidity": str(json_data['main']['humidity']),
    }

  else:
    city = ''
    data = {} #if the user does not type any city in the input bar, city is blank
  return render(request, 'index.html', {'city': city, 'data': data})