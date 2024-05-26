from gi.repository import Gtk, Gio, GObject
import gi

gi.require_version("Gtk", "4.0")


class DataObject(GObject.GObject):
    def __init__(self):
        super(DataObject, self).__init__()


def setup(widget, item):
    """Setup the widget to show in the Gtk.Listview"""
    image = Gtk.Image()
    item.set_child(image)


def bind(widget, item):
    """bind data from the store object to the widget"""
    item.get_child().set_from_file("../exemple.jpg")


def on_activate(app):
    win = Gtk.ApplicationWindow(
        application=app,
        title="Gtk4 is Awesome !!!",
        default_height=400,
        default_width=400,
    )
    sw = Gtk.ScrolledWindow()

    grid_view = Gtk.GridView()
    factory = Gtk.SignalListItemFactory()
    factory.connect("setup", setup)
    factory.connect("bind", bind)
    grid_view.set_factory(factory)

    store = Gio.ListStore.new(DataObject)

    selection = Gtk.SingleSelection()

    selection.set_model(store)

    grid_view.set_model(selection)

    v1 = DataObject()
    v2 = DataObject()
    store.append(v1)
    store.append(v2)

    sw.set_child(grid_view)
    win.set_child(sw)
    win.present()


app = Gtk.Application(application_id="org.gtk.Example")
app.connect("activate", on_activate)
app.run(None)
