# Import tkinter and webview libraries
from tkinter import *
import webview
  
# define an instance of tkinter
tk = Tk()


tk.title('JetTweet')
#  size of the window where we show our website
tk.geometry("800x450")

# Open website
webview.create_window('JetTweet', 'https://ali12345.pythonanywhere.com')
webview.start()