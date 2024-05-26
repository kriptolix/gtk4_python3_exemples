from gi.repository import Gtk, Gio, GObject
import gi

gi.require_version("Gtk", "4.0")


class DataObject(GObject.GObject):

    __gtype_name__ = 'DataObject'

    text = GObject.Property(type=str, default=None)

    def __init__(self, text):

        super().__init__()

        self.text = text


def setup(widget, item):
    """Setup the widget to show in the Gtk.Listview"""
    label = Gtk.Label()
    item.set_child(label)


def bind(widget, item):
    """bind data from the store object to the widget"""
    label = item.get_child()
    obj = item.get_item()

    label.set_text(obj.text)


def on_activate(app):
    win = Gtk.ApplicationWindow(
        application=app,
        title="Gtk4 is Awesome !!!",
        default_height=400,
        default_width=400,
    )
    sw = Gtk.ScrolledWindow()
    list_view = Gtk.ListView()
    factory = Gtk.SignalListItemFactory()
    factory.connect("setup", setup)
    factory.connect("bind", bind)

    list_view.set_factory(factory)

    selection = Gtk.SingleSelection()

    store = Gio.ListStore.new(DataObject)

    selection.set_model(store)

    list_view.set_model(selection)

    v1 = DataObject("entry")
    v2 = DataObject("other")

    store.append(v1)
    store.append(v2)

    sw.set_child(list_view)
    win.set_child(sw)
    win.present()


app = Gtk.Application(application_id="org.gtk.Example")
app.connect("activate", on_activate)
app.run(None)
