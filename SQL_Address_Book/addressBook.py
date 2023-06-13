''' 
    Nicholas Colan | June 2023
    
    This project is a simple GUI-based (using `PyQt`) address book in which the user can 
    create new contact information as well as search for someone's contact information and 
    have it displayed. All of the contact data will be stored in a `MySQL` database.
'''

'''
- June 12:
    Created GUI and added functionality to switch between screens.
    Need to:
        Setup MySQL database to store/retrieve contact information
        Add MySQL functionality to Find Contact/Create Contact pages
        Add 'Display Contact' Page (have ability to delete contact here)
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QStackedWidget, QMainWindow
from PyQt5.QtCore import Qt

# ------------------------------------------------------------

class HomeScreen(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setUI()
        
    def setUI(self):
        self.create_contact_button = QPushButton('Create New Contact')
        self.create_contact_button.clicked.connect(self.parent.showCreateContactScreen)
        
        self.find_contact_button = QPushButton('Find Contact')
        self.find_contact_button.clicked.connect(self.parent.showFindContactScreen)
        
        self.about_button = QPushButton('About')
        self.about_button.clicked.connect(self.parent.showAboutScreen)
        
        home_page_layout = QVBoxLayout()
        home_page_layout.setSpacing(0)
        
        button_layout1 = QHBoxLayout()
        button_layout1.addWidget(self.find_contact_button)
        button_layout1.addWidget(self.create_contact_button)
        
        home_page_layout.addLayout(button_layout1)
        home_page_layout.addWidget(self.about_button)
        
        self.setLayout(home_page_layout)
        

# ------------------------------------------------------------
        
class CreateContactScreen(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setUI()
        
    def setUI(self):
        # Create QLineEdit widgets for each field
        self.first_name_input = QLineEdit()
        self.first_name_input.setStyleSheet("font-size: 18pt;")
        self.last_name_input = QLineEdit()
        self.last_name_input.setStyleSheet("font-size: 18pt;")
        self.email_input = QLineEdit()
        self.email_input.setStyleSheet("font-size: 18pt;")
        self.phone_number_input = QLineEdit()
        self.phone_number_input.setStyleSheet("font-size: 18pt;")
        self.dob_input = QLineEdit()
        self.dob_input.setStyleSheet("font-size: 18pt;")

        # Create QLabel widgets for the field labels
        self.create_contact_label = QLabel('Create Contact')
        self.create_contact_label.setAlignment(Qt.AlignCenter)

        self.first_name_label = QLabel('First Name:')
        self.last_name_label = QLabel('Last Name:')
        self.email_label = QLabel('Email:')
        self.phone_number_label = QLabel('Phone Number:')
        self.dob_label = QLabel('Date of Birth:')

        # Create QPushButtons to run functions
        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.addToList) # Connects to the 'addToList' method to store data

        self.clear_button = QPushButton('Clear All')
        self.clear_button.clicked.connect(self.clear_fields)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.parent.showHomeScreen)


        # Create horizontal layout for organizing the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)

        # Create a vertical layout for organizing the text fields
        layout = QVBoxLayout()

        # Add the field labels, QLineEdit widgets, and the save button to the layout
        layout.addWidget(self.create_contact_label)
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.phone_number_label)
        layout.addWidget(self.phone_number_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.dob_label)
        layout.addWidget(self.dob_input)
        layout.addLayout(button_layout)
        layout.addWidget(self.home_button)

        self.setLayout(layout)

        self.contactsList = []
        
        
    # Collect all of the data   
    def addToList(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        email = self.email_input.text()
        phone_number = self.phone_number_input.text()
        dob = self.dob_input.text()
        
        contact_data = (first_name,last_name,email,phone_number,dob)
        self.contactsList.append(contact_data)
        
        self.clear_fields()
        
        print(self.contactsList)
        
    # Clear the text fields
    def clear_fields(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.phone_number_input.clear()
        self.email_input.clear()
        self.dob_input.clear()
        
# ------------------------------------------------------------

class FindContactScreen(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setUI()
        
    def setUI(self):
        # Create QLineEdit widgets for each field
        self.first_name_input = QLineEdit()
        self.first_name_input.setStyleSheet("font-size: 18pt;")
        self.last_name_input = QLineEdit()
        self.last_name_input.setStyleSheet("font-size: 18pt;")
        self.email_input = QLineEdit()
        self.email_input.setStyleSheet("font-size: 18pt;")
        
        # Create QLabel widgets
        self.find_contact_label = QLabel('Find Contact')
        self.find_contact_label.setAlignment(Qt.AlignCenter)
        self.tip_label = QLabel('(You can search by first and last name or by email)')
        self.tip_label.setAlignment(Qt.AlignCenter)
        self.tip_label.setStyleSheet("font-size: 18pt;")
        
        self.first_name_label = QLabel('First Name:')
        self.last_name_label = QLabel('Last Name:')
        self.email_label = QLabel('Email:')
        
        # QPushButtons to run functions
        self.search_button = QPushButton('Search')
        # ---------------------------- ADD FUNCTIONALITY ------------------------------------------
        #self.search_button.clicked.connect(self.searchContact) # Connects to the 'searchContact()' method to find data

        self.clear_button = QPushButton('Clear All')
        self.clear_button.clicked.connect(self.clear_fields)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.parent.showHomeScreen)
        
        # Create horizontal layout for organizing the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.clear_button)
        
        # Create a vertical layout for organizing the text fields
        find_contact_layout = QVBoxLayout()

        # Add the field labels, QLineEdit widgets, and the save button to the layout
        find_contact_layout.addWidget(self.find_contact_label)
        find_contact_layout.addWidget(self.tip_label)
        find_contact_layout.addWidget(self.first_name_label)
        find_contact_layout.addWidget(self.first_name_input)
        find_contact_layout.addWidget(self.last_name_label)
        find_contact_layout.addWidget(self.last_name_input)
        find_contact_layout.addWidget(self.email_label)
        find_contact_layout.addWidget(self.email_input)
        
        find_contact_layout.addLayout(button_layout)
        find_contact_layout.addWidget(self.home_button)

        self.setLayout(find_contact_layout)
        
        
    # Clear the text fields
    def clear_fields(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.email_input.clear()

# ------------------------------------------------------------

class AboutScreen(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setUI()
        
    def setUI(self):
        self.about_label = QLabel('About')
        self.about_label.setAlignment(Qt.AlignCenter)
        self.info_label = QLabel('Nicholas Colan \n June 2023')
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("font-size: 18pt;")
        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.parent.showHomeScreen)
        
        about_layout = QVBoxLayout()
        about_layout.addWidget(self.about_label)
        about_layout.addWidget(self.info_label)
        about_layout.addWidget(self.home_button)
        
        self.setLayout(about_layout)
        
# ------------------------------------------------------------

class AddressBook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setWindowTitle('Address Book')
        
        self.stacked_widget = QStackedWidget()
        self.home_screen = HomeScreen(self)
        self.create_contact_screen = CreateContactScreen(self)
        self.find_contact_screen = FindContactScreen(self)
        self.about_screen = AboutScreen(self)
    
        self.stacked_widget.addWidget(self.home_screen)
        self.stacked_widget.addWidget(self.create_contact_screen)
        self.stacked_widget.addWidget(self.find_contact_screen)
        self.stacked_widget.addWidget(self.about_screen)
        
        
        self.setCentralWidget(self.stacked_widget)  # Set the stacked widget as the central widget
        
        self.showHomeScreen()  # Call the showHomeScreen() function to display the home screen
    
    
    def showHomeScreen(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)
        
    def showCreateContactScreen(self):
        self.stacked_widget.setCurrentWidget(self.create_contact_screen) 
    
    def showFindContactScreen(self):
        self.stacked_widget.setCurrentWidget(self.find_contact_screen)
        
    def showAboutScreen(self):
        self.stacked_widget.setCurrentWidget(self.about_screen)
        
# -----        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 25px;
        }
    ''')
    
    gui = AddressBook()
    gui.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

        
        
# ------------------------------------------------------------