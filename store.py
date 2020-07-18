import os
path = "/home/blackandromeda/PycharmProjects/password_manager/"
class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    def __init__(self):
        Borg.__init__(self)
        if os.path.exists(path):
            pass



