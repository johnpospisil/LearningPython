# static methods - can be called on the class, even if no objects exist.
# static methods are not specific to an instance of a class.
class Math:
    @staticmethod
    def add5(x):
        return x + 5


print(Math.add5(5))
