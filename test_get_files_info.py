from functions.get_files_info import get_files_info

def test_and_print(working_dir, directory):
    if directory == ".":
        label = "current directory"
    else:
        label = f"'{directory}' directory"
    
    result = get_files_info(working_dir, directory)
    
    print(f"Result for {label}:")
    for line in result.split("\n"):
        print(f"    {line}")
    print()

test_and_print("calculator", ".")
test_and_print("calculator", "pkg")
test_and_print("calculator", "/bin")
test_and_print("calculator", "../")
