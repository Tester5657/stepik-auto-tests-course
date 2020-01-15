s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

full_string = "text"
substring = "text2"

assert substring in full_string, f"expected \'{substring}\' to be substring of \'{full_string}\'"

if __name__ == '__main__':
    main()