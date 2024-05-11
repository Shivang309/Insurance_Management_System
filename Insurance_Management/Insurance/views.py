from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate
import folium
import geocoder
import time

# Create your views here.
def home_page(request):
    return render(request,'home_page.html')

def Customer_home(request):
    return render(request,'Customer_home.html')

def Customer_login(request):
    error=""
    if request.method=='POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request,'Customer_login.html',locals())

def registration(request):
    error=""
    if request.method=="POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        pn=request.POST['Phone_number']
        lc=request.POST['Address']
        em=request.POST['email']
        pwd=request.POST['pwd']
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            CustomerDetail.objects.create(user=user,Phone_number=pn,Address=lc)
            error="no"
        except:
            error="yes"

    return render(request,'registration.html',locals())

def agent_list(request):
    agents = Ajents.objects.all()

    # Create a map centered at a certain location
    map = folium.Map(location=[26, 80], zoom_start=6)

    # Add markers for each agent's address
    for agent in agents:
        try:
            # Use geocoder to get the location coordinates based on the address
            location = geocoder.osm(agent.address)
            if location.ok:
                lat = location.latlng[0]
                lon = location.latlng[1]

                # Add marker to the map
                folium.Marker(location=[lat, lon], tooltip="Click for more",
                               popup=(agent.name, agent.Phone, agent.start_Time, agent.end_Time)).add_to(map)

            # Introduce a delay to ensure compliance with the rate limit
            time.sleep(1)  # Sleep for 1 second after each request
        except Exception as e:
            # Handle exceptions gracefully
            print(f"Error processing agent '{agent.name}': {str(e)}")

    # Render map to HTML
    map_html = map._repr_html_()

    return render(request, 'agent_list.html', {'agents': agents, 'map_html': map_html})