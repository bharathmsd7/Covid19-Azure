import folium 
from firebase import firebase  
firebase = firebase.FirebaseApplication('https://covid19-37d86.firebaseio.com/', None)

def create_map(name, loc):
    name = name
    #arr = loc.split(" ")
    arr = ['11.956764','79.819659']

    my_map3 = folium.Map(location = arr, zoom_start = 10) 

    # CircleMarker with radius 
    folium.CircleMarker(location = arr, 
                        radius = 75, popup = name).add_to(my_map3) 
    # Pass a string in popup parameter 
    folium.Marker(arr, 
                popup = name, tooltip = name).add_to(my_map3) 
    
    lat = []
    log = []
    uname = []
    result = firebase.get('user', '')
    id = []
    for i in result:
        id.append(i)
    
    for j in id:
        temp = result[j]
        lat.append(temp['latitude'])
        log.append(temp['longitude'])
        uname.append(temp['username'])
    
    for idx, n in enumerate(id):
        location = []
        location.append(lat[idx])
        location.append(log[idx])
        username = uname[idx]
        folium.Marker(location, 
                popup = username , tooltip= username).add_to(my_map3) 

        print("success")


    my_map3.save("templates/my_map.html") 

#create_map('asfjd;l','15.000 15.000')