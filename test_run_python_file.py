from functions.run_python_file import run_python_file

result = run_python_file("calculator", "main.py")
print("Test 1 - main.py no args:")
print(result)
print()

result = run_python_file("calculator", "main.py", ["3 + 5"])
print("Test 2 - main.py with args:")
print(result)
print()

result = run_python_file("calculator", "tests.py")
print("Test 3 - tests.py:")
print(result)
print()

result = run_python_file("calculator", "../main.py")
print("Test 4 - outside directory:")
print(result)
print()

result = run_python_file("calculator", "nonexistent.py")
print("Test 5 - nonexistent file:")
print(result)
print()

result = run_python_file("calculator", "lorem.txt")
print("Test 6 - not a Python file:")
print(result)
