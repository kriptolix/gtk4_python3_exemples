import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject  # noqa


class DataObject(GObject.GObject):
    def __init__(self, txt: str, txt2: str, children=None):
        super(DataObject, self).__init__()
        self.data = txt
        self.data2 = txt2
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
    
def setup1(widget, item):
    """Setup the widget to show in the Gtk.Listview"""
    label = Gtk.Label()    
    item.set_child(label)


def bind1(widget, item):
    """bind data from the store object to the widget"""
    label = item.get_child()
    row = item.get_item()
    obj = row.get_item()
    label.set_label(obj.data2)


def on_activate(app):
    win = Gtk.ApplicationWindow(
        application=app,
        title="Gtk4 is Awesome !!!",
        default_height=400,
        default_width=400,
    )
    sw = Gtk.ScrolledWindow()
    list_view = Gtk.ColumnView()  
    factory = Gtk.SignalListItemFactory()
    factory.connect("setup", setup)
    factory.connect("bind", bind)
    
    factory1 = Gtk.SignalListItemFactory()
    factory1.connect("setup", setup1)
    factory1.connect("bind", bind1)
    
    
    selection = Gtk.SingleSelection()
    
    store = Gio.ListStore.new(DataObject)
    
    model = Gtk.TreeListModel.new(store, False, False, add_tree_node)
    
    selection.set_model(model)
    
    list_view.set_model(selection)
    
    collum1 = Gtk.ColumnViewColumn.new("collum01", factory)
    collum2 = Gtk.ColumnViewColumn.new("collum02", factory1)
    
    list_view.append_column(collum1)
    list_view.append_column(collum2)
    
    v1 = [DataObject("entrada 01", "other")]
    v2 = [DataObject("entrada 02","", v1)]
    store.append(DataObject("entrada 03", "else", v2)) 

    sw.set_child(list_view)
    win.set_child(sw)
    win.present()


app = Gtk.Application(application_id="org.gtk.Example")
app.connect("activate", on_activate)
app.run(None)
