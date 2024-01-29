# Set up a class that adds to the count when it is called,
# and can return the stored value
class Counter:
    def __init__(self):
        self.count = 0

    def add(self, num):
        self.count += num

    def report(self):
        return f"Counted to {self.count} so far."