
if __name__ == '__main__':
    text: str = 'one two three four five'

    to_find = 'two'
    if to_find in text:
        print(f'string "{text}" contains substring "{to_find}"')

    # idx will contains INDEX of the first occurrence of the substring 'to_find' in
    # the 'text' string, otherwise -1
    idx: int = text.find(to_find)
    if -1 != idx:
        print(f'text "{to_find}" is located at {idx} in the string "{text}"')

    # trying to find 'to_find' in the 'text' starting from index 10
    idx = text.find(to_find, 10)
    if -1 != idx:
        print(f'text "{to_find}" is located at {idx} in the string "{text}"')
    else:
        print(f'Not found. (starting from 10 position)')
    