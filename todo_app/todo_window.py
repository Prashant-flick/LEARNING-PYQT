"""
Todo App Main Window
Contains the main window layout and UI logic
"""

from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QListWidget, QListWidgetItem,
                             QMessageBox, QLabel, QFrame)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont

from todo_item import TodoItem
from todo_data import TodoData


class TodoWindow(QMainWindow):
    """Main application window for the Todo app"""
    
    def __init__(self):
        super().__init__()
        self.todo_data = TodoData()  # Data manager for todos
        self.init_ui()
        self.load_todos()
        
    def init_ui(self):
        """Initialize the user interface"""
        # Set window properties
        self.setWindowTitle("Simple Todo App")
        self.setFixedSize(500, 600)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main vertical layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Title
        title_label = QLabel("📋 My Todo List")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)
        
        # Add separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)
        
        # Input section
        input_layout = QHBoxLayout()
        
        # Text input for new todos
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Enter a new todo item...")
        self.todo_input.returnPressed.connect(self.add_todo)  # Connect Enter key
        input_layout.addWidget(self.todo_input)
        
        # Add button
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_todo)
        self.add_button.setFixedWidth(80)
        input_layout.addWidget(self.add_button)
        
        main_layout.addLayout(input_layout)
        
        # Todo list widget
        self.todo_list = QListWidget()
        self.todo_list.setAlternatingRowColors(True)  # Nice visual effect
        main_layout.addWidget(self.todo_list)
        
        # Button section
        button_layout = QHBoxLayout()
        
        # Complete button
        self.complete_button = QPushButton("✓ Mark Complete")
        self.complete_button.clicked.connect(self.toggle_complete)
        button_layout.addWidget(self.complete_button)
        
        # Delete button
        self.delete_button = QPushButton("🗑 Delete")
        self.delete_button.clicked.connect(self.delete_todo)
        button_layout.addWidget(self.delete_button)
        
        # Clear completed button
        self.clear_completed_button = QPushButton("Clear Completed")
        self.clear_completed_button.clicked.connect(self.clear_completed)
        button_layout.addWidget(self.clear_completed_button)
        
        main_layout.addLayout(button_layout)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
    def add_todo(self):
        """Add a new todo item"""
        text = self.todo_input.text().strip()
        
        # Validate input
        if not text:
            QMessageBox.warning(self, "Warning", "Please enter a todo item!")
            return
        
        if len(text) > 100:
            QMessageBox.warning(self, "Warning", "Todo item is too long (max 100 characters)!")
            return
        
        # Create new todo
        todo = TodoItem(text)
        self.todo_data.add_todo(todo)
        
        # Add to UI
        self.add_todo_to_list(todo)
        
        # Clear input and update status
        self.todo_input.clear()
        self.todo_input.setFocus()  # Keep focus on input
        self.update_status()
        
    def add_todo_to_list(self, todo):
        """Add a todo item to the list widget"""
        item = QListWidgetItem()
        item.setData(Qt.UserRole, todo)  # Store todo object in the item
        self.update_item_display(item, todo)
        self.todo_list.addItem(item)
        
    def update_item_display(self, item, todo):
        """Update the display of a list item"""
        display_text = todo.text
        if todo.completed:
            display_text = f"✓ {display_text}"
            # Make completed items look different
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)
        else:
            # Reset font for incomplete items
            font = item.font()
            font.setStrikeOut(False)
            item.setFont(font)
            
        item.setText(display_text)
        
    def toggle_complete(self):
        """Toggle completion status of selected todo"""
        current_item = self.todo_list.currentItem()
        if not current_item:
            QMessageBox.information(self, "Info", "Please select a todo item first!")
            return
            
        # Get todo object from item
        todo = current_item.data(Qt.UserRole)
        todo.toggle_completed()
        
        # Update display
        self.update_item_display(current_item, todo)
        self.update_status()
        
    def delete_todo(self):
        """Delete selected todo item"""
        current_item = self.todo_list.currentItem()
        if not current_item:
            QMessageBox.information(self, "Info", "Please select a todo item first!")
            return
            
        # Confirm deletion
        reply = QMessageBox.question(
            self, 
            "Confirm Delete", 
            "Are you sure you want to delete this todo item?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Remove from data
            todo = current_item.data(Qt.UserRole)
            self.todo_data.remove_todo(todo)
            
            # Remove from UI
            row = self.todo_list.row(current_item)
            self.todo_list.takeItem(row)
            
            self.update_status()
            
    def clear_completed(self):
        """Clear all completed todo items"""
        completed_items = []
        
        # Find all completed items
        for i in range(self.todo_list.count()):
            item = self.todo_list.item(i)
            todo = item.data(Qt.UserRole)
            if todo.completed:
                completed_items.append((i, item, todo))
                
        if not completed_items:
            QMessageBox.information(self, "Info", "No completed items to clear!")
            return
            
        # Confirm clearing
        reply = QMessageBox.question(
            self,
            "Confirm Clear",
            f"Are you sure you want to clear {len(completed_items)} completed items?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Remove items (in reverse order to maintain indices)
            for i, item, todo in reversed(completed_items):
                self.todo_data.remove_todo(todo)
                self.todo_list.takeItem(i)
                
            self.update_status()
            
    def load_todos(self):
        """Load todos from data storage"""
        todos = self.todo_data.get_all_todos()
        for todo in todos:
            self.add_todo_to_list(todo)
        self.update_status()
        
    def update_status(self):
        """Update the status bar with current todo counts"""
        total = self.todo_list.count()
        completed = sum(1 for i in range(total) 
                       if self.todo_list.item(i).data(Qt.UserRole).completed)
        pending = total - completed
        
        status_text = f"Total: {total} | Pending: {pending} | Completed: {completed}"
        self.statusBar().showMessage(status_text)
        
    def closeEvent(self, event):
        """Handle application close event"""
        # You could add data saving here if needed
        event.accept()