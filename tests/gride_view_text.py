
import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk, Gio, GObject


class DataObject(GObject.GObject):
    def __init__(self, text):
        super(DataObject, self).__init__()
        self.buffer = Gtk.TextBuffer.new()
        self.text = text


def setup(widget, item):
    """Setup the widget to show in the Gtk.Listview"""
    
    def _focus(widget, x, y):
        view.grab_focus()


    box = Gtk.Box.new(1, 0)
    view = Gtk.TextView.new()
    view.set_size_request(390, 190)
    box.append(view)


    event = Gtk.EventControllerMotion.new()
    event.connect("motion", _focus)

    view.add_controller(event)

    item.set_child(box)


def bind(widget, item):
    """bind data from the store object to the widget"""
    box = item.get_child()
    obj = item.get_item()

    view = box.get_first_child()
    view.set_buffer(obj.buffer)

    obj.buffer.set_text(obj.text, -1)

    #box.connect("enter", lambda _: view.grab_focus())


def test(grid, position):
    print(position)


def on_activate(app):
    win = Gtk.ApplicationWindow(
        application=app,
        title="Gtk4 is Awesome !!!",
        default_height=600,
        default_width=800,
    )
    sw = Gtk.ScrolledWindow()

    grid_view = Gtk.GridView()
    factory = Gtk.SignalListItemFactory()
    factory.connect("setup", setup)
    factory.connect("bind", bind)
    grid_view.set_factory(factory)

    # grid_view.set_single_click_activate(True)
    # grid_view.connect("activate", test)

    store = Gio.ListStore.new(DataObject)
    selection = Gtk.NoSelection()

    selection.set_model(store)
    grid_view.set_model(selection)

    v1 = DataObject("entry 01")
    v2 = DataObject("entry 02")
    store.append(v1)
    store.append(v2)

    sw.set_child(grid_view)
    win.set_child(sw)
    win.present()


app = Gtk.Application(application_id="org.gtk.Example")
app.connect("activate", on_activate)
app.run(None)
