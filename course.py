class NewOne:
    def __init__(self) -> None:
        pass

    def __call__(self):
        return "New one class"


newclass = NewOne()

print(newclass)
print(newclass())
