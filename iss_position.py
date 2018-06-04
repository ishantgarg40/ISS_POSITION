import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import json

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

coordinates = json.loads(response.text)

# Creating a Robinson projection
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='robin',lon_0=0,resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawstates()


m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.))

m.drawmeridians(np.arange(0.,360.,60.))

m.drawmapboundary(fill_color='aqua')

x,y = m(float(coordinates['iss_position']['longitude']),float(coordinates['iss_position']['latitude'])) # setting up the coordinates 

m.plot(x,y,'o',markersize=7,alpha=0.4) # plotting the coordinates

plt.title("POSITION OF ISS IS SHOWN BY MARKER ON THE MAP") # title of the plotted map

plt.show()