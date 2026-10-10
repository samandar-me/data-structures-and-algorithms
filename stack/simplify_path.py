def simplifyPath(path: str) -> str:
    stack = []
    folders = path.split('/')

    for folder in folders:
        if folder == "..":
            if stack: stack.pop()
            continue

        if folder in ['.', '']:
            continue

        stack.append(folder)

    return "/" + "/".join(stack)