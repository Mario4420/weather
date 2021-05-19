import tkinter as tk 
from pyowm import OWM 

class App:
    
    def __init__(self):
        self.window = tk.Tk()
        self.owm = OWM("81bd3f534d8625a691bdfa7310e72ebd") 
        self.mgr = self.owm.weather_manager()
        self.city = tk.Entry()
        self.state = tk.Entry()
        self.confirm_button = tk.Button(text = "confirm", command = self.get_weather)  
        self.result = tk.Label() 
        self.main() 

    def main(self):
        self.city.pack()
        self.state.pack()  
        self.confirm_button.pack()
        self.result.pack()  
        self.window.mainloop() 

    def get_weather(self):
        city = self.city.get() 
        state = self.state.get() 
        observation = self.mgr.weather_at_place(city.strip() + "," + state.strip())
        w = observation.weather
        self.result.config(text = str(w.temperature('celsius')["temp"]) + "°") 

if __name__ == "__main__":
    App()

