
import numpy as np

print("=== Matrix Operations Tool ===")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))


def input_matrix(name, rows, cols):
    matrix = []
    print(f"\nEnter Matrix {name} row by row:")

    for i in range(rows):
        while True:
            try:
                row = list(map(
                    float,
                    input(f"Row {i + 1}: ").split()
                ))

                if len(row) != cols:
                    print(f"Please enter exactly {cols} values.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                print("Invalid input. Enter numbers separated by spaces.")

    return np.array(matrix)


A = input_matrix("A", rows, cols)

print("\nMatrix A:")
print(A)

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
print("5. Determinant")
print("6. Inverse")

choice = input("Enter your choice (1-6): ")

if choice == "4":
    print("\nTranspose:")
    print(A.T)

elif choice == "5":
    if rows == cols:
        print("\nDeterminant:", round(np.linalg.det(A), 4))
    else:
        print("Determinant requires a square matrix.")

elif choice == "6":
    if rows != cols:
        print("Inverse requires a square matrix.")
    elif abs(np.linalg.det(A)) < 1e-10:
        print("Inverse does not exist because the matrix is singular.")
    else:
        print("\nInverse:")
        print(np.linalg.inv(A))

elif choice in ["1", "2", "3"]:
    B = input_matrix("B", rows, cols)

    if choice == "1":
        print("\nAddition:")
        print(A + B)

    elif choice == "2":
        print("\nSubtraction:")
        print(A - B)

    elif choice == "3":
        if A.shape[1] == B.shape[0]:
            print("\nMultiplication:")
            print(A @ B)
        else:
            print("Matrix dimensions are incompatible.")

else:
    print("Invalid choice. Please select 1-6.")
