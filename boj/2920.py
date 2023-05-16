while True:
    data = input()
    if data == "0":
        break
    reversed_data = data[::-1]
    print('yes' if data == reversed_data else 'no')
