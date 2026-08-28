def convert(input):
    return input.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input()
    print(convert(user_input))

main()