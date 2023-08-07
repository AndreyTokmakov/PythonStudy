if __name__ == '__main__':
    ready = True
    not_ready = False

    if ready:
        print(f'ready = {ready}')

    # Same as above... but little longer redundant
    if True == ready:
        print(f'ready = {ready}')

    print()

    if not_ready:
        print(f'ready = {ready}')
    else:
        print(f'Else: not_ready = {not_ready}')

    # 'not not_ready' ---> same as ---> 'False == not_ready:'
    if not not_ready:
        print(f'Else: not_ready = {not_ready}')

    if False == not_ready:
        print(f'Else: not_ready = {not_ready}')
