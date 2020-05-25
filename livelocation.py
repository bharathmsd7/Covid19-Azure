import folium 
  
def create_map(name, loc):
    name = name
    arr = loc.split(" ")

    my_map3 = folium.Map(location = arr, zoom_start = 15) 

    # CircleMarker with radius 
    folium.CircleMarker(location = arr, 
                        radius = 75, popup = name).add_to(my_map3) 
    # Pass a string in popup parameter 
    folium.Marker(arr, 
                popup = ' Bharath ', tooltip='Bharath').add_to(my_map3) 
    
   


    my_map3.save("templates/my_map.html") 

