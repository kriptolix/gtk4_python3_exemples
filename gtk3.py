import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        self.set_default_size(200, -1)
        self.connect("destroy", Gtk.main_quit)

        self.listbox = Gtk.ListBox()   
        self.add(self.listbox)

        self.row = CustomRow('label content')
        self.listbox.add(self.row)


    def remove_row(self, button, row):
        
        
        
        self.listbox.remove(row)



class CustomRow(Gtk.ListBoxRow):
    def __init__(self, content):
        super.__init__(self)

        self.content = content

        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.HORIZONTAL)

        label = Gtk.Label().new(str=self.content)

        button_remove = Gtk.Button().new_from_icon_name(icon_name='gtk-close', size=1)
        button_remove.connect('clicked', MainWindow.remove_row, self)

        box.pack_start(label, True, True, 5)
        box.pack_start(button_remove, False, False, 5)

        self.add(box)


window = MainWindow()
window.show_all()

Gtk.main()
