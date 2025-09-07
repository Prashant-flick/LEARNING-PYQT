"""
Simple Todo App using PyQt5
Main application entry point
"""

import sys
from PyQt5.QtWidgets import QApplication
from todo_window import TodoWindow


def main():
    """Main application entry point"""
    # Create the QApplication instance
    # This is required for any PyQt5 application
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Simple Todo App")
    app.setApplicationVersion("1.0")
    
    # Create and show the main window
    window = TodoWindow()
    window.show()
    
    # Start the application event loop
    # This keeps the application running until the user closes it
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()