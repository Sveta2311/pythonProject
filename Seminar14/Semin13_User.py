class User:
    def __init__(self, name: str, user_id: str,  level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __repr__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __hash__(self):                                     # при переопределениии eq надо переопределять hash
        return hash(self.name) + hash(self.user_id)

    def __eq__(self, other):                                                           # True/False в зависимоти от выполнения условий
        return self.name == other.name and self.user_id == other.user_id
