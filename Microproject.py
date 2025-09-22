# Importing the libraries
from tkinter import *
import requests
import json
import datetime
from PIL import Image, ImageTk

# Interface of the application:
root = Tk()
root.title("Weather App")
root.geometry("500x600")
root['background'] = "white"

# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A  '), bg='white', font=("Bold", 15))
date.place(x=15, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("Bold", 15))
month.place(x=100, y=130)

# Time
hour = Label(root, text=dt.strftime('%I : %M %p'), bg='white', font=("Bold", 15))
hour.place(x=15, y=160)

# Theme for the respective time the application is used:
if 6 <= dt.hour <= 18:  
    image = Image.open('python/sun.png')  
    resized_image = image.resize((100, 100))
    img = ImageTk.PhotoImage(resized_image)
else:
    img = ImageTk.PhotoImage(Image.open('python/moon.png'))

panel = Label(root, image=img)
panel.place(x=210, y=200)

# City search
city_var = StringVar()
city_entry = Entry(root, textvariable=city_var, width=45)
city_entry.grid(row=1, column=0, ipady=10, sticky=W+E+N+S)

# Function where the API calls:
def city_name():
    try:
        # API Call
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_var.get()}&appid=65ffd36134ef2690fe7ba9353140276c"
        api_request = requests.get(api_url)
        api = json.loads(api_request.content)

        # Extract data
        y = api['main']
        current_temperature = round(y['temp'] - 273.15, 2)  
        tempmin = round(y['temp_min'] - 273.15, 2)
        tempmax = round(y['temp_max'] - 273.15, 2)
        humidity = y['humidity']

        # Coordinates
        x = api['coord']
        longitude = x['lon']
        latitude = x['lat']

        # Country and City
        z = api['sys']
        country = z['country']
        city = api['name']

        # Updating the labels with data
        lable_temp.configure(text=f"{current_temperature}°C")
        lable_humidity.configure(text=f"{humidity}%")
        max_temp.configure(text=f"Max: {tempmax}°C")
        min_temp.configure(text=f"Min: {tempmin}°C")
        lable_lon.configure(text=f"Lon: {longitude}")
        lable_lat.configure(text=f"Lat: {latitude}")
        lable_city.configure(text=f"{city}")
        lable_country.configure(text=f"{country}")

    except Exception as e:
        lable_city.configure(text="City Not Found", fg="red")

# Search bar and button:
city_nameButton = Button(root, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=5, sticky=W+E+N+S)

# Labels for City and Country
lable_city = Label(root, text="...", bg='white', font=("Bold", 15))
lable_city.place(x=15, y=63)

lable_country = Label(root, text="...", bg='white', font=("Bold", 15))
lable_country.place(x=220, y=63)

lable_lon = Label(root, text="...", bg='white', font=("Helvetica", 15))
lable_lon.place(x=15, y=95)

lable_lat = Label(root, text="...", bg='white', font=("Helvetica", 15))
lable_lat.place(x=180, y=95)

# Current Temperature:
lable_temp = Label(root, text="...", bg='white', font=("Helvetica", 30), fg='black')  
lable_temp.place(x=18, y=250)

# Other temperature details:
humi = Label(root, text="Humidity:", bg='white', font=("Bold", 15))
humi.place(x=15, y=400)

lable_humidity = Label(root, text="...", bg='white', font=("Bold", 15))
lable_humidity.place(x=115, y=400)

maxi = Label(root, text="Max. Temp:", bg='white', font=("Bold", 15))
maxi.place(x=15, y=430)

max_temp = Label(root, text="...", bg='white', font=("Bold", 15))
max_temp.place(x=128, y=430)

mini = Label(root, text="Min. Temp:", bg='white', font=("Bold", 15))  # Added title for min temp
mini.place(x=15, y=460)

min_temp = Label(root, text="...", bg='white', font=("Bold", 15))
min_temp.place(x=128, y=460)

# The main event loop to take action event triggered by the user:
root.mainloop()
