# 🔢 Matrix Operations Tool

A Python-based matrix calculator that performs essential matrix operations using NumPy. The project includes a command-line application and an interactive web interface built with Streamlit.

## 📌 Project Overview

The Matrix Operations Tool allows users to enter matrices and perform mathematical calculations through a simple interface. It demonstrates Python programming, numerical computation, input handling, and web application development.

## ✨ Features

- ➕ Matrix addition
- ➖ Matrix subtraction
- ✖️ Matrix multiplication
- 🔄 Matrix transpose
- 📐 Determinant calculation
- 🧮 Matrix inverse calculation
- ✅ Input validation in the command-line version
- 🌐 Interactive Streamlit web interface
- 📊 Clear display of calculation results
- ⚠️ Handles square-matrix requirements and singular matrices for determinant and inverse operations

## 🛠️ Technologies Used

- **Python** — Core programming language
- **NumPy** — Matrix calculations and numerical operations
- **Streamlit** — Interactive web interface
- **VS Code** — Development environment

## 📂 Project Structure

```text
Matrix-Operations-Tool/
│
├── matrix_tool.py
├── app.py
├── README.md
└── screenshots/
    ├── homepage.png
    ├── matrix-addition.png
    └── matrix-operations.png
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Matrix-Operations-Tool
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Install dependencies

Make sure Python is installed, then run:

```bash
python -m pip install numpy streamlit
```

## 🚀 Usage

### Option 1: Run the command-line application

Start the terminal version with:

```bash
python matrix_tool.py
```

Follow the prompts to enter matrix dimensions, input matrix values, and select an operation.

Available operations:

1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Determinant
6. Inverse

### Option 2: Run the web application

Launch the Streamlit interface:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

Then:

1. Select the required matrix operation.
2. Choose the number of rows and columns.
3. Enter the values for Matrix A and, when required, Matrix B.
4. Click **Calculate**.
5. View the result on the webpage.

## 🧪 Example

Consider the following matrices:

**Matrix A**

```text
1  2
3  4
```

**Matrix B**

```text
5  6
7  8
```

### Matrix Addition

```text
6   8
10  12
```

### Matrix Subtraction

```text
-4  -4
-4  -4
```

### Matrix Multiplication

```text
19  22
43  50
```

### Transpose of Matrix A

```text
1  3
2  4
```

### Determinant of Matrix A

```text
-2
```

### Inverse of Matrix A

```text
-2.0   1.0
 1.5  -0.5
```

## 🖼️ Screenshots

Add screenshots of your working Streamlit application to the `screenshots/` folder.

### 1. Application Homepage

![Matrix Operations Tool homepage](screenshots/homepage.png)

### 2. Matrix Addition Result

![Matrix addition result](screenshots/matrix-addition.png)

### 3. Matrix Operations Interface

![Matrix operations interface](screenshots/matrix-operations.png)

*Note: These image paths are placeholders. Save your actual screenshots with the specified filenames for them to appear on GitHub.*

## 📚 Concepts Learned

- Python loops, functions, and conditional statements
- Lists and numerical arrays
- Input validation and exception handling
- Matrix arithmetic and linear algebra
- NumPy array operations
- Building interactive applications with Streamlit
- Displaying calculated results through a web interface

## 🔮 Future Improvements

- Support different dimensions for Matrix A and Matrix B where mathematically valid.
- Add random matrix generation.
- Include matrix trace and rank operations.
- Improve error messages and input validation.
- Add a reset button and downloadable results.
- Deploy the application online.

## 👩‍💻 Author

**Chandana ML**

Electronics and Computer Engineering Student

GitHub: [Chandana322006](https://github.com/Chandana322006)

---

*This project was developed for educational purposes to practice Python programming, numerical computation, and web application development.*
