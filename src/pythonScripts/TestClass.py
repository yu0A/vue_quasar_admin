class TestClass:
    def __init__(self):
        pass

    def hello_world(self):
        return "hello world!"

    def __str__(self):
        return "hello world!"

    def __repr__(self):
        return "hello world!"
t = TestClass()
str(t)