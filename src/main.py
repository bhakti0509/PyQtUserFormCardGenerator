# main.py

# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from Login.login import LoginWindow # Import the LoginWindow class from login module
from PyQt5 import QtGui

# Entry point of the application

if __name__ == '__main__':

    # Create a QApplication instance
    app = QApplication(sys.argv)
    # Create an instance of the LoginWindow class
    ex = LoginWindow()
    # Set window properties
    ex.setWindowIcon(QtGui.QIcon('./assets/images/logo.png')) # Set window icon
    ex.setWindowTitle('User Info Form Application') # Set window title
    ex.setGeometry(1100, 40, 768, 1024) # Set window geometry
    ex.setFixedSize(768, 1024) # Set fixed window size
    ex.show() # Display the login window

# Start the application event loop
sys.exit(app.exec_())