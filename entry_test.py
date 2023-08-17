import gi
import sys

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk, Gio 

class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.cssProvider = Gtk.CssProvider()
        
        self.file = Gio.File.new_for_path('support.css')
        
        self.cssProvider.load_from_file(self.file)

        self.set_default_size(800, 600)        
        self.set_title("MyApp")        

        self.window = Gtk.ScrolledWindow()

        entry = Gtk.Entry.new()

        delegated = entry.get_delegate()

        delegated.connect("insert-text", self.text_inserted)
        entry.connect("changed", self.text_changed)

        self.window.set_child(entry)

        self.set_child(self.window)

    def text_inserted(self, text, length, position, date):
        print("inserted")

    def text_changed(self, data):
        print("changed")        

class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
    
    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
