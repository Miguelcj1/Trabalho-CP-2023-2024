import sys

def are_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        f1.readline()  # Skip the first line
        f2.readline()  # Skip the first line
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Check if the number of lines in both files is the same
    if len(lines1) != len(lines2):
        print("Number of lines is different.")
        return False

    line = 2
    for line1, line2 in zip(lines1, lines2):
        values1 = line1.split()
        values2 = line2.split()

        if len(values1) != len(values2):
            return False

        for val1, val2 in zip(values1, values2):
            val1_12=val1.replace(".", "")[0:12]
            val2_12=val2.replace(".", "")[0:12]
            if val1_12 != val2_12:
                print(f"Line {line} is different, comparing {file1} and {file2}")
                return False
        line += 1
    return True

# Specify the file paths and error margin
num_args = len(sys.argv) - 1
file1 = "cp_output.txt"
file2 = "../documentation/base/cp_output.txt"
if num_args == 2:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

# Check if the files are equal within the specified error margin
if are_files_equal(file1, file2) > 0:
    print("cp_output files are the SAME")
else:
    print("cp_output files are DIFFERENT")
