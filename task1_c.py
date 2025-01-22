class String_methods:
    def ___init___(self):
        self.string = None
    def get_string(self):
        self.string = input()
    def print_string(self):
        print(self.string.upper())

methods = String_methods()
methods.get_string()
methods.print_string()