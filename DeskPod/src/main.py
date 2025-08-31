# main.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DeskPodApp:
    def __init__(self):
        self.window = Gtk.Window(title="DeskPod")
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_default_size(400, 300)

        self.label = Gtk.Label(label="Welcome to DeskPod!")
        self.window.add(self.label)

    def run(self):
        self.window.show_all()
        Gtk.main()

if __name__ == "__main__":
    app = DeskPodApp()
    app.run()