class Matrix:
    def define(self, rows: int, columns: int) -> list[list]:
        matrix = []
        for i in range(rows):
            row = []
            for j in range(columns):
                element = int(input(f"Element in row-{i+1}, column-{j+1}: "))
                row.append(element)
            print()
            matrix.append(row)
        return matrix

    def print(self, matrix: list[list]) -> list[list]:
        for i in matrix:
            print(i)


m = Matrix()
m.print(m.define(3, 3))
