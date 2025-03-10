import folium

# Crie um mapa Folium
m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

# Adicione um marcador
folium.Marker([51.5074, -0.1278], tooltip='Londres').add_to(m)

# Adicione uma camada de mapa do OpenStreetMap
folium.TileLayer('openstreetmap').add_to(m)

# Adicione uma camada de mapa do Mapbox
folium.TileLayer('Mapbox Bright').add_to(m)

# Adicione um controle de camadas
folium.LayerControl().add_to(m)

# Salve o mapa em um arquivo HTML
m.save('map.html')