import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import secrets


def main():
    # Create the application
    app = QApplication(sys.argv)

    # Create a window
    window = QWidget()
    # Set window title
    window.setWindowTitle("RNG")
    # left margin, top margin, width, height
    window.setGeometry(100, 100, 200, 170)

    # Create a vertical layout for the window
    layout = QVBoxLayout(window)

    # Create a button
    button = QPushButton("Roll", window)

    # Set fixed width and height for the button
    button.setFixedSize(100, 100)

    # Add the button to the layout
    layout.addWidget(button, 0, alignment=Qt.AlignCenter)

    # Set the font size of the button text
    font = QFont()
    font.setPointSize(14)  # Increase the font size to 12
    button.setFont(font)

    # Define a function to handle button clicks
    def on_button_clicked():
        # Generates a random integer in the range 0-100
        random_integer = secrets.randbelow(101)
        button.setText(str(random_integer))

    # Connect the button"s clicked signal to the function
    button.clicked.connect(on_button_clicked)

    # Show the window
    window.show()

    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
