import tkinter as tk
from threading import Timer

class DisappearingTextApp:
    def __init__(self, root, timeout=5):
        self.root = root
        self.root.title("Disappearing Text Writing App")
        
        # Set up the text box
        self.text_box = tk.Text(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.text_box.pack(expand=True, fill='both')
        
        # Set the timeout duration (in seconds)
        self.timeout = timeout
        self.timer = None
        
        # Bind keypress event to reset the timer
        self.text_box.bind("<KeyPress>", self.reset_timer)
        
        # Start the initial timer
        self.start_timer()

    def start_timer(self):
        """Start a new timer to clear text after a certain timeout."""
        if self.timer:
            self.timer.cancel()  # Cancel any existing timer
        self.timer = Timer(self.timeout, self.clear_text)
        self.timer.start()
        
    def reset_timer(self, event=None):
        """Reset the timer whenever the user types."""
        self.start_timer()
    
    def clear_text(self):
        """Clear the text in the text box."""
        self.text_box.delete(1.0, tk.END)

# Create the main window and run the app
root = tk.Tk()
app = DisappearingTextApp(root, timeout=5)  # Set timeout to 5 seconds
root.mainloop()
