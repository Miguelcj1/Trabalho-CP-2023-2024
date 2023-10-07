import sys

def are_files_equal(file1, file2, error_margin):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        f1.readline()  # Skip the first line
        f2.readline()  # Skip the first line
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Check if the number of lines in both files is the same
    if len(lines1) != len(lines2):
        return False

    for line1, line2 in zip(lines1, lines2):
        values1 = line1.split()
        values2 = line2.split()

        if len(values1) != len(values2):
            return False

        for val1, val2 in zip(values1, values2):
            try:
                float_val1 = float(val1)
                float_val2 = float(val2)
                # print(abs(float_val1 - float_val2))
                if abs(float_val1 - float_val2) > error_margin:
                    return False
            except ValueError:
                return False

    return True

# Specify the file paths and error margin
num_args = len(sys.argv) - 1
file1 = "cp_output.txt"
file2 = "../documentation/base/cp_output.txt"
if num_args == 2:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
error_margin = 1e-6 # 1x10^-6 = 0.000001

# Check if the files are equal within the specified error margin
if are_files_equal(file1, file2, error_margin) > 0:
    print("cp_output files are the SAME")
else:
    print("cp_output files are DIFFERENT")
