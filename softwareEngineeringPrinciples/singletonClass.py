class SingletonExample:
    __shared_instance = None

    @staticmethod
    def getInstance():
        if not SingletonExample.__shared_instance:
            SingletonExample()
        return SingletonExample.__shared_instance

    def __init__(self):
        if SingletonExample.__shared_instance:
            raise Exception("Cannot instantiate another instance of SingletonExample")
        else:
            SingletonExample.__shared_instance = self

if __name__ == "__main__":
    obj1 = SingletonExample()
    print (obj1)
    print (obj1.getInstance())

    try:
        obj2 = SingletonExample()
    except Exception as e:
        print (e)

# Thread-safe option

import threading
lock = threading.Lock()

# Metaclass
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    pass