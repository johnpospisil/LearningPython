# Inheritance - when a class inherits functionality from another class.

from Chef import Chef
from MandarinChef import MandarinChef

myChef = Chef()
myChef.make_chicken()
myChef.make_pho()
myChef.make_salad()

myMandarinChef = MandarinChef()
myMandarinChef.make_chicken()
myMandarinChef.make_pho()
myMandarinChef.make_salad()
myMandarinChef.make_fried_rice()
