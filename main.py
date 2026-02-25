def generate(n: int) -> list:
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[i - 1]
        current_row = [1]
        for j in range(0, len(previous_row) - 1):
            sum = previous_row[j] + previous_row[j + 1]
            current_row.append(sum)
        current_row.insert(len(current_row), 1)
        triangle.insert(i, current_row)
    return triangle

if __name__ == '__main__':
    print(generate(-1))