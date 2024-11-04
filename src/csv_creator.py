import re
import os
import pandas as pd

# Directory containing the NIST results files
results_dir = "/Users/sidnair/Desktop/Python Master/SIH/nist_test_results"
output_file = "nist_feature_dataset.csv"

def extract_features_from_file(file_path):
    features = {}
    with open(file_path, 'r') as file:
        content = file.read()

        # Extract statistics from monobit_test
        match = re.search(r'TEST: monobit_test.*?Ones count\s*=\s*(\d+).*?Zeroes count\s*=\s*(\d+).*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['monobit_test_ones_count'] = int(match.group(1))
            features['monobit_test_zeroes_count'] = int(match.group(2))
            features['monobit_test_p'] = float(match.group(3))
        else:
            features['monobit_test_ones_count'] = None
            features['monobit_test_zeroes_count'] = None
            features['monobit_test_p'] = None

        # Extract P-value for frequency_within_block_test
        match = re.search(r'TEST: frequency_within_block_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['frequency_within_block_test_p'] = float(match.group(1))
        else:
            features['frequency_within_block_test_p'] = None

        # Extract P-value for runs_test
        match = re.search(r'TEST: runs_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['runs_test_p'] = float(match.group(1))
        else:
            features['runs_test_p'] = None

        # Extract P-value for longest_run_ones_in_a_block_test
        match = re.search(r'TEST: longest_run_ones_in_a_block_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['longest_run_ones_in_a_block_test_p'] = float(match.group(1))
        else:
            features['longest_run_ones_in_a_block_test_p'] = None

        # Extract P-value for binary_matrix_rank_test
        match = re.search(r'TEST: binary_matrix_rank_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['binary_matrix_rank_test_p'] = float(match.group(1))
        else:
            features['binary_matrix_rank_test_p'] = None

        # Extract P-value for dft_test
        match = re.search(r'TEST: dft_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['dft_test_p'] = float(match.group(1))
        else:
            features['dft_test_p'] = None

        # Extract P-value for approximate_entropy_test
        match = re.search(r'TEST: approximate_entropy_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['approximate_entropy_test_p'] = float(match.group(1))
        else:
            features['approximate_entropy_test_p'] = None

        # Extract P-value for serial_test
        match = re.search(r'TEST: serial_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['serial_test_p'] = float(match.group(1))
        else:
            features['serial_test_p'] = None

        # Extract P-value for cumulative_sums_test
        match = re.search(r'TEST: cumulative_sums_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['cumulative_sums_test_p'] = float(match.group(1))
        else:
            features['cumulative_sums_test_p'] = None

        # Extract P-value for non_overlapping_template_matching_test
        match = re.search(r'TEST: non_overlapping_template_matching_test.*?P=([0-9.]+)', content, re.DOTALL)
        if match:
            features['non_overlapping_template_matching_test_p'] = float(match.group(1))
        else:
            features['non_overlapping_template_matching_test_p'] = None

    return features

# Create a dataset for storing features
dataset = []

# Iterate through all files in the results directory
for filename in os.listdir(results_dir):
    if filename.endswith("_nist_results.txt"):
        file_path = os.path.join(results_dir, filename)
        features = extract_features_from_file(file_path)

        # Extract the label from the filename (e.g., "AES_8KB_0_nist_results.txt" -> "AES")
        label = filename.split('_')[0]
        features['label'] = label

        # Append the features and label to the dataset
        dataset.append(features)

# Convert the dataset to a pandas DataFrame
df = pd.DataFrame(dataset)

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False)
print(f"Feature extraction complete. Dataset saved to {output_file}.")
