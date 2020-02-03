class Text:
    data = ""
    theme = "?"

    def __init__(self, data, theme="Misc"):
        self.data = data
        self.theme = theme

    def __str__(self):
        return "{0}".format(self.data)

    def count_letters(self):
        return len(list(filter(
            lambda l: not l in [" ", ",", ".", "!", "?", "-"]
        , self.data)))

    def count_whitespace(self):
        return len(list(filter(lambda l: l == " ", self.data)))
    
    def replace(self, old, new):
        self.data = self.data.replace(old, new)
    
    def remove_word(self, index):
        words = self.data.split(" ")

        del words[index]

        self.data = " ".join(words)

# TEST

t = Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "Latin")
print(t)
print(t.count_letters())
print(t.count_whitespace())
t.replace("i", "1")
t.remove_word(3)
print(t)