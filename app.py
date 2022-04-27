import requests
from bs4 import BeautifulSoup
from tkinter import Tk
from tkinter import Label
from PIL import Image, ImageTk

url = 'https://weather.com/lt-LT/orai/siandien/l/LHXX0005:1:LH?Goto=Redirected'

tk = Tk()
tk.title = ("Weather Application")
tk.config(bg = "white")

img = Image.open("C:/Users/Songokas1/Desktop/PythonPortfolio/WeatherApplication/weather.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def getWeatherData():
    r = requests.get(url)
    bs = BeautifulSoup(r.content,"html.parser")
    location = bs.find("h1",{"class":"CurrentConditions--location--kyTeL"}).text
    temperature = bs.find("span",{"class":"CurrentConditions--tempValue--3a50n"}).text
    weather_predict = bs.find("div",{"class":"CurrentConditions--phraseValue--2Z18W"}).text

    temp_label.after(60000,getWeatherData)
    tk.update()

    location_label.config(text=location)
    temp_label.config(text=temperature)
    weather_predict_label.config(text=weather_predict)

Label(tk,image=img, bg="white").grid(row=1,sticky="E")
location_label = Label(tk,font=("Calibri bold",20),bg="white")
location_label.grid(row=0,sticky="N",padx=100)
temp_label = Label(tk,font=("Calibri bold",50),bg="white")
temp_label.grid(row=1,sticky="W",padx=50)
weather_predict_label = Label(tk,font=("Calibri bold",15),bg="white")
weather_predict_label.grid(row=2,sticky="W", padx=50)

getWeatherData()
tk.mainloop()

