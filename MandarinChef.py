# Inheritance - The MandarinChef can do all the things a Chef can do, with a few differences
from Chef import Chef


class MandarinChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_salad(self):
        print("The chef makes Mandarin salad")
