import os
import subprocess

# Path to the directory containing encrypted files
encrypted_data_dir = "encrypted data"
# Path to the sp800_22_tests directory (update this path if necessary)
nist_test_dir = "/Users/sidnair/Desktop/Python Master/SIH/sp800_22_tests"
# Directory to store the NIST test results
output_dir = "nist_test_results"
os.makedirs(output_dir, exist_ok=True)

# Check if the sp800_22_tests.py file exists
sp800_22_path = os.path.join(nist_test_dir, "sp800_22_tests.py")
if not os.path.exists(sp800_22_path):
    print(f"sp800_22_tests.py not found at: {sp800_22_path}")
else:
    print(f"Found sp800_22_tests.py at: {sp800_22_path}")

# Function to run NIST tests on a file
def run_nist_tests(file_path):
    # Create an output file path for the current encrypted file
    output_file = os.path.join(output_dir, os.path.basename(file_path).replace('.bin', '_nist_results.txt'))
    
    command = ['python3', sp800_22_path, file_path]
    try:
        # Run the NIST test and capture the output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Check if there was an error during the run
        if result.returncode != 0:
            print(f"Error running NIST tests on {file_path}: {result.stderr}")
        else:
            # Save the output to a file
            with open(output_file, 'w') as f:
                f.write(result.stdout)
            print(f"NIST tests completed for {file_path}. Results saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Iterate over each encrypted file and run NIST tests
for filename in os.listdir(encrypted_data_dir):
    file_path = os.path.join(encrypted_data_dir, filename)
    if not os.path.exists(file_path):
        print(f"File does not exist: {file_path}")
    else:
        print(f"Running NIST tests on {filename}...")
        run_nist_tests(file_path)

print("Feature extraction complete.")
