"""
Todo Item Model
Represents a single todo item with its properties and methods
"""

from datetime import datetime


class TodoItem:
    """
    Represents a single todo item
    
    This class encapsulates all the data and behavior for a todo item.
    Following the principle of encapsulation - keeping data and methods together.
    """
    
    def __init__(self, text, completed=False):
        """
        Initialize a new todo item
        
        Args:
            text (str): The todo item text
            completed (bool): Whether the item is completed (default: False)
        """
        self.text = text
        self.completed = completed
        self.created_at = datetime.now()
        self.completed_at = None
        
    def toggle_completed(self):
        """Toggle the completion status of the todo item"""
        self.completed = not self.completed
        
        # Track when item was completed
        if self.completed:
            self.completed_at = datetime.now()
        else:
            self.completed_at = None
            
    def mark_completed(self):
        """Mark the todo item as completed"""
        if not self.completed:
            self.completed = True
            self.completed_at = datetime.now()
            
    def mark_incomplete(self):
        """Mark the todo item as incomplete"""
        if self.completed:
            self.completed = False
            self.completed_at = None
            
    def __str__(self):
        """String representation of the todo item"""
        status = "✓" if self.completed else "○"
        return f"{status} {self.text}"
        
    def __repr__(self):
        """Developer-friendly representation of the todo item"""
        return f"TodoItem(text='{self.text}', completed={self.completed})"
        
    def to_dict(self):
        """
        Convert todo item to dictionary for easy serialization
        Useful if you want to save/load from JSON files later
        """
        return {
            'text': self.text,
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create TodoItem from dictionary
        Useful for loading from saved data
        """
        item = cls(data['text'], data['completed'])
        item.created_at = datetime.fromisoformat(data['created_at'])
        if data['completed_at']:
            item.completed_at = datetime.fromisoformat(data['completed_at'])
        return item