import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GLib


def _state_changed(action, value):

    action.set_state(value)

    print(action, ", ", value)


def on_activate(app):
    win = Gtk.ApplicationWindow(
        application=app,
        title="Gtk4 is Awesome !!!",
        default_height=400,
        default_width=400,
    )
    sw = Gtk.ScrolledWindow()

    box = Gtk.Box()
    check_one = Gtk.CheckButton.new_with_label("One")
    check_two = Gtk.CheckButton.new_with_label("Two")
    check_two.set_group(check_one)

    box.append(check_one)
    box.append(check_two)

    sw.set_child(box)

    action_group = Gio.SimpleActionGroup()
    action = Gio.SimpleAction.new_stateful("alter",
                                           GLib.VariantType('s'),
                                           GLib.Variant('s', "yellow"))
    action.connect("change_state", _state_changed)
    action_group.add_action(action)

    win.insert_action_group("checks", action_group)

    check_one.set_action_name("checks.alter")
    check_one.set_action_target_value(GLib.Variant('s', "yellow"))

    check_two.set_action_name("checks.alter")
    check_two.set_action_target_value(GLib.Variant('s', "blue"))

    win.set_child(sw)
    win.present()


app = Gtk.Application(application_id="org.gtk.Example")
app.connect("activate", on_activate)
app.run(None)
