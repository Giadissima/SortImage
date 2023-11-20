import tkinter as tk
class CustomMessageBox(tk.Toplevel):
  # TODO mettere style in configuration
  # TODO rivedere l'intera grafica e aggiungere il pulsante di warning
  def __init__(self, parent, title, message, icon=None):
    super().__init__(parent)
    self.title(title)

    if icon:
      self.iconbitmap(default=icon)

    self.geometry("350x150")

    self.message_label = tk.Label(self, text=message, padx=10, pady=10)
    self.message_label.pack()

    self.checkbox_var = tk.BooleanVar()
    self.checkbox = tk.Checkbutton(self, text="Don't show again", variable=self.checkbox_var)
    self.checkbox.pack()

    self.ok_button = tk.Button(self, text="OK", command=self.ok_pressed, highlightthickness=0)
    self.ok_button.pack(side=tk.LEFT, padx=35, ipadx=10)

    self.cancel_button = tk.Button(self, text="Annulla", command=self.cancel_pressed, highlightbackground='white')
    self.cancel_button.pack(side=tk.RIGHT, padx=35, ipadx=10)
    

  def ok_pressed(self):
    self.ok = True
    self.destroy()

  def cancel_pressed(self):
    self.ok = False
    self.destroy()