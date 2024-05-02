import os
import webbrowser
import folium

def showonmap(placelist):
    # see http://fontawesome.io/icons/ for fancy icons
    center = [42.36165764, -71.08567345]  # The [lat, lon] of the center of Boston
    bostonmap = folium.Map(location = center, zoom_start=12) #Create the map object

    for place in placelist:
        lat = place.get("Lat")
        lon = place.get("Lon")

        icon = folium.Icon(icon= 'graduation-cap', prefix="fa", color='green')
        folium.Marker(location=[lat, lon],
                        popup = '<a href=\"' + place.get("URL") + '\">' + place.get("URL") + '</a>',
                        tooltip= place.get("Name"),
                        icon = icon).add_to(bostonmap)

    #Save the html file in the local directory
    filePath = os.getcwd() + "\\bostonmap.html"
    bostonmap.save(filePath)
    webbrowser.open('file://' + filePath)

def main():
    universities = [{"Name": 'Harvard', "URL": 'https://www.harvard.edu/', 'Lat': 42.373032, 'Lon': -71.116661},
                    {"Name": 'MIT', "URL": 'https://www.mit.edu/', 'Lat': 42.360092, 'Lon': -71.0942},
                    {"Name": 'BU', "URL": 'https://www.bu.edu/', 'Lat': 42.350498, 'Lon': -71.1054}]
    showonmap(universities)

main()
