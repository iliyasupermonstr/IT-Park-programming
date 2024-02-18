def create_matrix(cols_count, rows_count):
    matrix = []
    count = 1
    for row in range(rows_count):
        matrix.append([])
        for col in range(cols_count):
            matrix[row].append(count)
            count += 1
    return matrix


def create_file(matrix, path):
    with open(path, "w") as f:
        for row in matrix:
            f.write("   ".join(map(str, row)) + "\n")


# Создаем матрицу 2x5
matrix = create_matrix(10, 10)

# Сохраняем матрицу в файле "matrix.txt"
create_file(matrix, "matrix3.txt")

