# Stuart Daniells
# C0829441
# Sub-Project 1
# Weather GUI

from cgitb import text
import json
from multiprocessing import Condition
from tkinter import *
import tkinter as tk
from unittest import result
# to get geographical location based on city/state/country
from geopy.geocoders import Nominatim
# ttk - to make use of more advcnced tkinter widgets and features
from tkinter import ttk, messagebox
# locating time zone of a place even offline, 
# including day light saving for differnt countries
from timezonefinder import TimezoneFinder
from datetime import datetime
# to make http requets
import requests
# to access different time zones available for use from the 'Olson' database
import pytz

root = Tk()
root.title("Weather App")
# GUI sizing
root.geometry("900x500+300+200")
# preventing auto and manual resizing
root.resizable(False, False)

# to fetch the weather data from openweathermap api based on city entered in text box
def getWeather():

   try:
      city = textfield.get()

      geolocator = Nominatim(user_agent= "geoapiExercises")
      location  = geolocator.geocode(city)
      obj = TimezoneFinder()
      result = obj.timezone_at(lng = location.longitude, lat=location.latitude)
      print(result)

      home = pytz.timezone(result)
      local_time = datetime.now(home)
      current_time = local_time.strftime("%I : %M %p")
      clock.config(text = current_time)
      name.config(text = "CURRENT WEATHER")

      # weather
      # key is appid
      api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d66147f29d6bfe2536431e09be45f19f"

      # getting pressure, temperature, wind speed and humidity from the fetched weather data
      json_data = requests.get(api).json()
      condition = json_data['weather'][0]['main']
      description = json_data['weather'][0]['description']
      temp = int(json_data['main']['temp'] - 273.15)
      pressure = json_data['main']['pressure']
      humidity = json_data['main']['humidity']
      wind = json_data['wind']['speed']

      t.config(text = (temp, "°"))
      c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

      w.config(text = wind)
      h.config(text=humidity)
      d.config(text = description)
      p.config(text = pressure)
   
   except Exception as e:
      messagebox.showerror("Weather App", "Invalid Entry \n-try not hitting the enter key after entering city name")


# search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

# text field box dimentions and focus cursor
textfield = tk.Entry(root, justify = "center", width = 17, font = ("poppins", 25, "bold"), bg = "#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

# Search icon and functionality when clicked
Search_icon = PhotoImage(file="search_icon.png")
myimage = Button (image = Search_icon, borderwidth = 0, cursor= "hand2", bg = "#404040", command = getWeather)
myimage.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file = "logo.png")
logo = Label(image = Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file = "box.png")
frame_myimage = Label (image = Frame_image)
frame_myimage.pack(padx = 5, pady = 5, side = BOTTOM)

#time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock=Label(root, font=("Helvetica", 20))
clock.place(x = 30, y = 130)


# WIND label heading
label1 = Label(root, text = "WIND", font=("Helvetica", 15, 'bold'), fg = "white", bg = "#1ab5ef")
label1.place(x=120, y=400)

# HUMIDITY label heading
label2 = Label(root, text = "HUMIDITY", font=("Helvetica", 15, 'bold'), fg = "white", bg = "#1ab5ef")
label2.place(x=250, y=400)

# DESCRIPTION label heading
label3 = Label(root, text = "DESCRIPTION", font=("Helvetica", 15, 'bold'), fg = "white", bg = "#1ab5ef")
label3.place(x=430, y=400)

# PRESSURE label heading
label4 = Label(root, text = "PRESSURE", font=("Helvetica", 15, 'bold'), fg = "white", bg = "#1ab5ef")
label4.place(x=650, y=400)

# temperature values from api
t = Label(font = ("arial", 70, "bold"), fg = "#ee666d")
t.place(x = 400, y = 150)

# condition (feels like) values from api
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

# WIND label values from api
w = Label(text = "...", font=("arial", 20, "bold"), bg = "#1ab5ef")
w.place(x=120, y = 430)

# HUMIDITY label values from api
h = Label(text = "...", font=("arial", 20, "bold"), bg = "#1ab5ef")
h.place(x=280, y = 430)

# DESCRIPTION label values from api
d = Label(text = "...", font=("arial", 20, "bold"), bg = "#1ab5ef")
d.place(x=450, y = 430)

# PRESSURE label values from api
p = Label(text = "...", font=("arial", 20, "bold"), bg = "#1ab5ef")
p.place(x=670, y = 430)


# keep looping back till application is killed
root.mainloop()
