from pyfiglet import Figlet
import random
import sys

while True:
    f = Figlet()
    fonts = f.getFonts()

    def main():
        local_font = get_font()
        string = input("Input: ")
        f = Figlet(font=local_font)
        print(f.renderText(string))

    def get_font():
        if len(sys.argv) == 1:
            return random.choice(fonts)
        elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            return sys.argv[2]
        else:
            sys.exit("Invalid # of arguments")
    break
main()
