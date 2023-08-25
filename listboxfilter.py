import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import random


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(self.box)

        self.button = Gtk.Button(label="Insert Row")
        self.box.append(self.button)

        self.set_default_size(800, 600)

        self.list_box = Gtk.ListBox.new()  
        self.list_box.set_sort_func(self.sort_function)        
        
        self.box.append(self.list_box)

        self.button.connect('clicked', self.add)

    def add(self, button):
        
        number = random.randint(0,100)        
        row = self.row_setup(f"test {number}", f"{number} ")   
        
        self.list_box.append(row)

    def sort_function(self, one, two):

        one_number = int(one.get_child().get_first_child().props.label)
        two_number = int(two.get_child().get_first_child().props.label)        
        
        if  one_number < two_number:            
            return -1
        elif one_number > two_number:            
            return 1
        else:
            return 0        
        
    def row_setup(self, title, number):

        row = Gtk.ListBoxRow.new()
        row_box = Gtk.Box()
        row_title = Gtk.Label.new(title)
        row_number = Gtk.Label.new(number)
        row_box.append(row_number)
        row_box.append(row_title)        
        row.set_child(row_box)

        return row 


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(None)