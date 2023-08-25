import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject  # noqa


class DataObject(GObject.GObject):
    def __init__(self, txt: str, children=None):
        super(DataObject, self).__init__()
        self.data = txt
        self.children = children


def add_tree_node(item):

    if not (item):
        print("no item")
        return model
    else:
        if type(item) == Gtk.TreeListRow:
            item = item.get_item()

            print("converteu")
            print(item)

        if not item.children:
            return None
        store = Gio.ListStore.new(DataObject)
        for child in item.children:
            store.append(child)
        return store


def setup(widget, item):
    """Setup the widget to show in the Gtk.Listview"""
    label = Gtk.Label()
    expander = Gtk.TreeExpander.new()
    expander.set_child(label)
    item.set_child(expander)


def bind(widget, item):
    """bind data from the store object to the widget"""
    expander = item.get_child()
    label = expander.get_child()
    row = item.get_item()
    expander.set_list_row(row)
    obj = row.get_item()
    label.set_label(obj.data)


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

    model = Gtk.TreeListModel.new(store, False, False, add_tree_node)

    selection.set_model(model)

    list_view.set_model(selection)

    v1 = [DataObject("entrada 01")]
    v2 = [DataObject("entrada 01", v1)]
    store.append(DataObject("entrada 01", v2))

    # store.append(DataObject("entrada 02"))

    sw.set_child(list_view)
    win.set_child(sw)
    win.present()


app = Gtk.Application(application_id="org.gtk.Example")
app.connect("activate", on_activate)
app.run(None)
