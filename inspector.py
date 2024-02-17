import sys
class slopes:
    def __init__(self):
        self.observer = None
        return self
    def __init_subclass__(self):
        self.observer = None
        return str(self)+str(self.observer)
class observe(slopes):
    def __init__(self, observer):
        observer = __spec__.__eq__.__text_signature__
        super(observe, self).__init__()

inspector = observe(sys.argv[1])
(lambda: inspector)()
