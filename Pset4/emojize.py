import emoji

def main():
    code = input("Input: ")
    emojized = emoji.emojize(code, language="alias")
    print(f"Output: {emojized}")

main()