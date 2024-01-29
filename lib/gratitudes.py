# Create class to store and return a list of strings
class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted

new_gratitudes = Gratitudes()
print(new_gratitudes.format())