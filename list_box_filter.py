import random
from gi.repository import Gtk
import gi

gi.require_version("Gtk", "4.0")


def row_setup(title, number):

    row = Gtk.ListBoxRow.new()
    row_box = Gtk.Box()
    row_title = Gtk.Label.new(title)
    row_number = Gtk.Label.new(number)
    row_box.append(row_number)
    row_box.append(row_title)
    row.set_child(row_box)

    return row


def sort_function(one, two):

    one_number = int(one.get_child().get_first_child().props.label)
    two_number = int(two.get_child().get_first_child().props.label)

    if one_number < two_number:
        return -1
    elif one_number > two_number:
        return 1
    else:
        return 0


def on_activate(app):
    win = Gtk.ApplicationWindow(
        application=app,
        title="Gtk4 is Awesome !!!",
        default_height=400,
        default_width=600,
    )
    sw = Gtk.ScrolledWindow()

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    sw.set_child(box)

    button = Gtk.Button(label="Insert Row")
    box.append(button)

    list_box = Gtk.ListBox.new()
    list_box.set_sort_func(sort_function)

    box.append(list_box)

    button.connect('clicked', add, list_box)

    win.set_child(sw)
    win.present()


def add(button, list_box):

    number = random.randint(0, 100)
    row = row_setup(f"test {number}", f"{number} ")

    list_box.append(row)


app = Gtk.Application(application_id="org.gtk.Example")
app.connect("activate", on_activate)
app.run(None)
