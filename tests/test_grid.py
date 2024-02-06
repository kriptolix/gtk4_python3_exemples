from gi.repository import Gtk, GdkPixbuf, Gio, Gdk
import gi
import sys

gi.require_version('Gtk', '4.0')


def create_image(file_name, img_width, cssProvider=None):

    info = 'file:' + file_name

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

    box.get_style_context().add_provider(
        cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    box.add_css_class('thumbnail')

    box.set_hexpand(True)
    box.set_vexpand(False)

    # add image to top
    pixbuf = GdkPixbuf.Pixbuf.new_from_file(file_name)
    other = Gdk.Texture.new_for_pixbuf(pixbuf)
    # calculate height to keep width and aspect ratio
    # img_height = pixbuf.get_height() * img_width / pixbuf.get_width()
    image = Gtk.Picture.new_for_paintable(other)

    # image = Gtk.Picture.new_from_pixbuf(pixbuf)
    # image.set_size_request(img_height, img_width)

    image.get_style_context().add_provider(
        cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    image.add_css_class('thumbnail-image')

    box.append(image)

    # add label to bottom
    label = Gtk.Label(label=info)
    label.set_vexpand(False)

    label.get_style_context().add_provider(
        cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    label.add_css_class('thumbnail-label')

    box.append(label)

    return box


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cssProvider = None
        self.cssProvider = Gtk.CssProvider()

        self.file = Gio.File.new_for_path('../support.css')

        self.cssProvider.load_from_file(self.file)

        self.set_default_size(900, 600)
        self.set_title("MyApp")

        self.grid = Gtk.Grid()

        self.window = Gtk.ScrolledWindow()
        self.window.set_child(self.grid)

        self.set_child(self.window)

        idx = 0
        prev = None

        for idx in range(0, 20):
            # 4 columns
            i = int(idx / 4)
            j = int(idx % 4)

            image = create_image('../exemple.jpg', 1920 /
                                 4 - 10, self.cssProvider)

            self.grid.attach(image, i, j, 1, 1)


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
