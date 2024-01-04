def main():
    text = input('Input: ')
    short_form = shorten(text)
    print(f'Output: {short_form}')



def shorten(word):
    new_word = ''
    for char in word:
        if not char.lower() in ['a','e','i','o','u']:
            new_word = new_word + char
    return new_word

if __name__ == "__main__":
    main()
