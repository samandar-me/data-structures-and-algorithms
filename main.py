def is_valid(s: str) -> bool:
    counter = 0

    for i in s:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1

        if counter < 0:
                return False

    return counter == 0

if __name__ == '__main__':
    print(is_valid(")"))