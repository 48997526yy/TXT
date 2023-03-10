import tkinter
from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.title('BlockNot')


menu = Menu(root)
root.config(menu=menu)


def close():
  root.destroy()


def save_as():
  textfilesaveas = fd.asksaveasfile(mode='w', defaultextension='.txt')
  data = text.get('1.0', tkinter.END)


def click():
    window = Tk()
    window.title('BlockNot')
    menu = Menu(window)
    window.config(menu=menu)
    text = Text(window)
    text.pack(expand=YES, fill=BOTH)


def click_close():
    root.destroy()
    window = Tk()
    window.title('BlockNot')
    menu = Menu(window)
    window.config(menu=menu)
    text = Text(window)
    text.pack(expand=YES, fill=BOTH)



file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New', command=click_close, accelerator='Ctrl+M')
file_menu.add_command(label='New window', command=click, accelerator='Ctrl+Shift+S')
file_menu.add_command(label='Open file...', accelerator='Ctrl+O')
file_menu.add_command(label='Save', accelerator='Ctrl+S')
file_menu.add_command(label='Save as...', accelerator='Ctrl+Shift+S', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Page setup...')
file_menu.add_command(label='Print...', accelerator='Ctrl+P')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=close)


edit_menu = Menu(menu, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z')
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X')
edit_menu.add_command(label='Copy', accelerator='Ctrl+C')
edit_menu.add_command(label='Paste', accelerator='Ctrl+V')
edit_menu.add_command(label='Delete', accelerator='Del')
edit_menu.add_separator()
edit_menu.add_command(label='Search with Bing...', accelerator='Ctrl+E')
edit_menu.add_command(label='Find...', accelerator='Ctrl+F')
edit_menu.add_command(label='Find Next', accelerator='F3')
edit_menu.add_command(label='Find Previous', accelerator='Shift+F3')
edit_menu.add_command(label='Replace...', accelerator='Ctrl+H')
edit_menu.add_command(label='Go to...', accelerator='Ctrl+G')
edit_menu.add_separator()
edit_menu.add_command(label='Select All', accelerator='Ctrl+A')
edit_menu.add_command(label='Time/Date', accelerator='F5')


format_menu = Menu(menu, tearoff=0)
format_menu.add_command(label='Word Wrap')
format_menu.add_command(label='Font...')


zoom_menu = Menu(menu, tearoff=0)
zoom_menu.add_command(label='Zoom in')
zoom_menu.add_command(label='Zoom out')
zoom_menu.add_command(label='Restore Default Zoom')


view_menu = Menu(menu, tearoff=0)
view_menu.add_cascade(label='Zoom', menu=zoom_menu)
view_menu.add_command(label='Status bar')


help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='View Help')
help_menu.add_command(label='Send Feedback')
help_menu.add_separator()
help_menu.add_command(label='About Notepad')



# Text
text = Text(root)
text.pack(expand=YES, fill=BOTH)

menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Edit', menu=edit_menu)
menu.add_cascade(label='Format', menu=format_menu)
menu.add_cascade(label='View', menu=view_menu)
menu.add_cascade(label='Help', menu=help_menu)

root.mainloop()