"""
Todo Data Manager
Handles data storage and retrieval for todo items
"""

from typing import List
from todo_item import TodoItem


class TodoData:
    """
    Manages todo item data storage and operations
    
    This class follows the Single Responsibility Principle - it only handles
    data management. In a more complex app, this could be extended to save/load
    from files or databases.
    """
    
    def __init__(self):
        """Initialize the data manager with an empty list"""
        self._todos: List[TodoItem] = []
        
    def add_todo(self, todo: TodoItem) -> None:
        """
        Add a new todo item
        
        Args:
            todo (TodoItem): The todo item to add
        """
        if not isinstance(todo, TodoItem):
            raise TypeError("Expected TodoItem instance")
            
        self._todos.append(todo)
        
    def remove_todo(self, todo: TodoItem) -> bool:
        """
        Remove a todo item
        
        Args:
            todo (TodoItem): The todo item to remove
            
        Returns:
            bool: True if item was removed, False if not found
        """
        try:
            self._todos.remove(todo)
            return True
        except ValueError:
            return False
            
    def get_all_todos(self) -> List[TodoItem]:
        """
        Get all todo items
        
        Returns:
            List[TodoItem]: List of all todo items
        """
        return self._todos.copy()  # Return copy to prevent external modification
        
    def get_completed_todos(self) -> List[TodoItem]:
        """
        Get all completed todo items
        
        Returns:
            List[TodoItem]: List of completed todo items
        """
        return [todo for todo in self._todos if todo.completed]
        
    def get_pending_todos(self) -> List[TodoItem]:
        """
        Get all pending (incomplete) todo items
        
        Returns:
            List[TodoItem]: List of pending todo items
        """
        return [todo for todo in self._todos if not todo.completed]
        
    def get_todo_count(self) -> int:
        """
        Get total number of todo items
        
        Returns:
            int: Total number of todo items
        """
        return len(self._todos)
        
    def get_completed_count(self) -> int:
        """
        Get number of completed todo items
        
        Returns:
            int: Number of completed todo items
        """
        return len(self.get_completed_todos())
        
    def get_pending_count(self) -> int:
        """
        Get number of pending todo items
        
        Returns:
            int: Number of pending todo items
        """
        return len(self.get_pending_todos())
        
    def clear_completed(self) -> int:
        """
        Remove all completed todo items
        
        Returns:
            int: Number of items that were removed
        """
        completed_todos = self.get_completed_todos()
        for todo in completed_todos:
            self._todos.remove(todo)
        return len(completed_todos)
        
    def clear_all(self) -> None:
        """Clear all todo items"""
        self._todos.clear()
        
    def find_todo_by_text(self, text: str) -> TodoItem:
        """
        Find a todo item by its text
        
        Args:
            text (str): The text to search for
            
        Returns:
            TodoItem: The first matching todo item, or None if not found
        """
        for todo in self._todos:
            if todo.text.lower() == text.lower():
                return todo
        return None
        
    def __len__(self) -> int:
        """Support len() function"""
        return len(self._todos)
        
    def __iter__(self):
        """Support iteration over todos"""
        return iter(self._todos)
        
    def __str__(self) -> str:
        """String representation showing summary"""
        total = len(self._todos)
        completed = self.get_completed_count()
        pending = self.get_pending_count()
        return f"TodoData: {total} items ({pending} pending, {completed} completed)"