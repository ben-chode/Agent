from functions.get_file_content import get_file_content

# Test 1: lorem.txt (big file, should truncate)
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print()

# Test 2: main.py (normal file)
result = get_file_content("calculator", "main.py")
print(f"main.py content:")
print(result)
print()

# Test 3: pkg/calculator.py (file in subdirectory)
result = get_file_content("calculator", "pkg/calculator.py")
print(f"pkg/calculator.py content:")
print(result)
print()

# Test 4: /bin/cat (outside working directory)
result = get_file_content("calculator", "/bin/cat")
print(f"/bin/cat result:")
print(result)
print()

# Test 5: file that doesn't exist
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"pkg/does_not_exist.py result:")
print(result)
print()
