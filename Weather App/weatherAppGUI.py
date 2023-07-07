'''
This will be the GUI section of our weather app. It will feature a 'home' page, where the user will be able to enter a city/town or a zip code, and the weekly forecast will then be displayed under the 'weekly forecast screen'. From this screen, the user will also be able to click onto a specific day, and will be brought to a new 'daily forecast' screen. This 'daily forecast' screen will show a more detailed look at the forecast for that day. 
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QStackedWidget, QMainWindow
from PyQt5.QtCore import Qt
from getWeather import *

class weatherGUI(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.resize(600,300)
        self.setWindowTitle('Weather Forecast')
        
        # Create stack for all widgets and instantiate widgets here
        self.stacked_widget = QStackedWidget()
        self.home_screen = HomeScreen(self)
        self.findWeather_screen = FindWeatherScreen(self)
        self.displayWeather_screen = DisplayWeatherScreen(self)
        self.about_screen = AboutScreen(self)
        
        # Add stacked widgets to the stack
        self.stacked_widget.addWidget(self.home_screen)
        self.stacked_widget.addWidget(self.findWeather_screen)
        self.stacked_widget.addWidget(self.displayWeather_screen)
        
        self.setCentralWidget(self.stacked_widget)  # Set the stacked widget as the central widget

        self.showHomeScreen()
        
        
    # Functions that allow to switch between stacked widgets
    def showHomeScreen(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)
        
    def showSearchWeatherScreen(self):
        self.stacked_widget.setCurrentWidget(self.findWeather_screen)
        
    def showDisplayWeatherScreen(self, zipcode):
        self.displayWeather_screen.setZipCode(zipcode)  
        self.stacked_widget.setCurrentWidget(self.displayWeather_screen)
        
    def showAboutScreen(self):
        self.stacked_widget.setCurrentWidget(self.about_screen)
        
#----------------------------------------------------

class HomeScreen(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setUI()
        
        
    def setUI(self):
        self.display_label = QLabel('Weather App')
        self.display_label.setAlignment(Qt.AlignCenter)
        
        self.searchWeather_button = QPushButton('Find Weather')
        self.searchWeather_button.clicked.connect(self.parent.showSearchWeatherScreen)
        
        self.about_button = QPushButton('About')
        self.about_button.clicked.connect(self.parent.showAboutScreen)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.searchWeather_button)
        button_layout.addWidget(self.about_button)
        
        homeScreen_layout = QVBoxLayout()
        homeScreen_layout.addWidget(self.display_label)
        homeScreen_layout.addLayout(button_layout)
        
        self.setLayout(homeScreen_layout)
        
#-----------------------------------------------------

class FindWeatherScreen(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setUI()
        
        
    def setUI(self):
        self.search_label = QLabel('Enter Zip Code Below:')
        self.search_label.setAlignment(Qt.AlignCenter)
        
        self.location_input = QLineEdit()
        self.location_input.setStyleSheet("font-size: 18pt;")
        
        self.searchWeather_button = QPushButton('Search Weather')
        self.searchWeather_button.setFixedSize(200,50)
        self.searchWeather_button.clicked.connect(self.findWeather) 
        
        self.home_button = QPushButton('Home')
        self.home_button.setFixedSize(200,50)
        self.home_button.clicked.connect(self.parent.showHomeScreen)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.searchWeather_button)
        button_layout.addWidget(self.home_button)
        
        findWeather_layout = QVBoxLayout()
        findWeather_layout.addWidget(self.search_label)
        findWeather_layout.addWidget(self.location_input)
        findWeather_layout.addLayout(button_layout)
        
        self.setLayout(findWeather_layout)
        
        
    def findWeather(self):
        zipCode = self.location_input.text()
        self.parent.showDisplayWeatherScreen(zipCode)
        
        
        

#-----------------------------------------------------

class DisplayWeatherScreen(QWidget):
    
    zipCode = ''
    
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
    
    def setUI(self):  
        api_key = '3d457d463e8f2a568c8717d8e9947002'
        weatherInfo = getWeather(api_key,'',self.zipCode)
        
        # Qlabels for all of the weather info
        self.location_label = QLabel(str(weatherInfo.location))
        self.tempH_label = QLabel(str(weatherInfo.temp_high))
        self.tempL_label = QLabel(str(weatherInfo.temp_low))
        self.windSpeed_label = QLabel(str(weatherInfo.wind_speed))
        self.humidity_label = QLabel(str(weatherInfo.humidity))
        self.description_label = QLabel(str(weatherInfo.description))
        self.sunrise_label = QLabel(str(weatherInfo.sunrise))
        self.sunset_label = QLabel(str(weatherInfo.sunset))
        
        # Create vertical layout and add weather info labels
        weather_layout = QVBoxLayout()
        weather_layout.addWidget(self.location_label)
        weather_layout.addWidget(self.tempH_label)
        weather_layout.addWidget(self.tempL_label)
        weather_layout.addWidget(self.windSpeed_label)
        weather_layout.addWidget(self.humidity_label)
        weather_layout.addWidget(self.description_label)
        weather_layout.addWidget(self.sunrise_label)
        weather_layout.addWidget(self.sunset_label)
        
        self.back_button = QPushButton('Go Back')
        self.back_button.clicked.connect(self.parent.showSearchWeatherScreen)
        
        weather_layout.addWidget(self.back_button)
        
        self.setLayout(weather_layout)
        
        
        
    def setZipCode(self,zipCode):
        self.zipCode = zipCode
        self.setUI()
        

#-----------------------------------------------------

class AboutScreen(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        #self.setUI()
        

       
    
#----------------------------------------------------

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 25px;
        }
    ''')
    
    gui = weatherGUI()
    gui.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
        
        
        
