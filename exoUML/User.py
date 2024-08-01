class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"User(name={self.name})"