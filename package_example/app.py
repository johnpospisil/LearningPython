# import a module of the package - not preferred
# import my_package.shipping
# my_package.shipping.calc_shipping()


# import a module of the package - preffered
# from my_package import shipping
# shipping.calc_shipping()

# import a specific function from a module
from my_package.shipping import calc_shipping
calc_shipping()
