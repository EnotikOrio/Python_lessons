#812

class Upper:
    def get_input(self):
        return input("Введіть рядок: ")
    
    def print_upper_text(self, text):
        print(text.upper())

man1 = Upper()

input_s = man1.get_input()
man1.print_upper_text(input_s)
