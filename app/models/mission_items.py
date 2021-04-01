class MissionItem:
    def __init__(self, name, human_name=None, **kwargs):
        self.name = name
        self.human_name = human_name
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def public_name(self):
        if self.human_name:
            return self.human_name
        else:
            return self.name
