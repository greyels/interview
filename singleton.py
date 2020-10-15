# Method 1: A decorator
def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance
# Pros:
# Decorators are additive in a way that is often more intuitive than multiple inheritance.
# Cons:
# While objects created using MyClass() would be true singleton objects, MyClass itself is a a function, not a class, so you cannot call class methods from it. Also for

# Method 2: A base class
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
# Pros:
# It's a true class
# Cons:
# Multiple inheritance - eugh! __new__ could be overwritten during inheritance from a second base class? One has to think more than is necessary.

# Method 3: A metaclass
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
# Pros:
# It's a true class
# Auto-magically covers inheritance
# Uses __metaclass__ for its proper purpose (and made me aware of it)
# Cons:
# Are there any?