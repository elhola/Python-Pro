class MaxStudentsError(Exception):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return f'{self.msg}\n{super().__str__()}'