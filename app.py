
import streamlit as st
import numpy as np

st.set_page_config(page_title="Matrix Operations Tool", page_icon="🔢")

st.title("🔢 Matrix Operations Tool")
st.write("Perform matrix calculations using NumPy.")

operation = st.selectbox(
    "Choose an operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Transpose",
        "Determinant",
        "Inverse"
    ]
)

rows = st.number_input("Number of rows", min_value=1, max_value=5, value=2)
cols = st.number_input("Number of columns", min_value=1, max_value=5, value=2)

st.subheader("Enter Matrix A")

A_values = []
for i in range(int(rows)):
    cols_ui = st.columns(int(cols))
    row_values = []
    for j in range(int(cols)):
        value = cols_ui[j].number_input(
            f"A[{i+1},{j+1}]",
            value=0.0,
            key=f"a_{i}_{j}"
        )
        row_values.append(value)
    A_values.append(row_values)

A = np.array(A_values, dtype=float)

B = None
if operation in ["Addition", "Subtraction", "Multiplication"]:
    st.subheader("Enter Matrix B")
    B_values = []

    for i in range(int(rows)):
        cols_ui = st.columns(int(cols))
        row_values = []
        for j in range(int(cols)):
            value = cols_ui[j].number_input(
                f"B[{i+1},{j+1}]",
                value=0.0,
                key=f"b_{i}_{j}"
            )
            row_values.append(value)
        B_values.append(row_values)

    B = np.array(B_values, dtype=float)

if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = A + B
        elif operation == "Subtraction":
            result = A - B
        elif operation == "Multiplication":
            result = A @ B
        elif operation == "Transpose":
            result = A.T
        elif operation == "Determinant":
            if A.shape[0] != A.shape[1]:
                st.error("Determinant requires a square matrix.")
                st.stop()
            result = np.linalg.det(A)
        else:
            if A.shape[0] != A.shape[1]:
                st.error("Inverse requires a square matrix.")
                st.stop()
            if abs(np.linalg.det(A)) < 1e-10:
                st.error("This matrix has no inverse.")
                st.stop()
            result = np.linalg.inv(A)

        st.subheader("Result")
        if np.isscalar(result):
            st.success(f"{result:.4f}")
        else:
            st.dataframe(np.round(result, 4))

    except ValueError as e:
        st.error(f"Could not calculate the result: {e}")
