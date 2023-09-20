from typing import List

if __name__ == '__main__':
    parts: List[str] = ['one', 'two', 'three', 'four', 'five']
    print(f'Original list: {parts}\n')

    line1: str = ','.join(parts)
    print(line1)

    line2: str = ' '.join(parts)
    print(line1)

    line3: str = ' | '.join(parts)
    print(line3)