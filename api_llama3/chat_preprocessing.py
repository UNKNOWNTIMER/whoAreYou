import re
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Extract and save the game code from LLM
def extract_and_save_code(text, output_file):
    pattern = r"```(?:python\s*)?(.*?)```"  # Ensure matching the code block
    match = re.search(pattern, text, re.DOTALL)
    if match:
        code_block = match.group(1)
        folder_path = os.path.join('generated_data', 'game_code') # Determine folder path
        os.makedirs(folder_path, exist_ok=True)# Create folder if it does not exist
        full_path = os.path.join(folder_path, output_file)# Full file path
        with open(full_path, 'w', encoding='utf-8') as file:# Write the extracted code into the specified Python file
            file.write(code_block)
        print(f"The code has been saved to {full_path}")
    else:
        print("No matching code blocks found.")
    return

# Build the program itself from LLM
def save_program(text, output_file):
    pattern = r"```(?:python\s*)?(.*?)```"  # Ensure matching the code block
    match = re.search(pattern, text, re.DOTALL)
    if match:
        code_block = "import random\n" + match.group(1)
        #code_block = match.group(1)
        folder_path = os.path.join('generated_data', 'generated_RNG_type') # Determine folder path
        os.makedirs(folder_path, exist_ok=True)# Create folder if it does not exist
        full_path = os.path.join(folder_path, output_file)# Full file path
        with open(full_path, 'w', encoding='utf-8') as file:# Write the extracted code into the specified Python file
            file.write(code_block)
        print(f"The code has been saved to {full_path}")
    else:
        print("No matching code blocks found.")
    return

# Text processing
def extract_info(text):
    # Define regular expressions to capture information
    name_pattern = r"name=\"(.*?)\""
    age_pattern = r"age=\"(.*?)\""
    gender_pattern = r"gender=\"(.*?)\""
    background_pattern = r"background=\"(.*?)\""
    # Use regular expressions to search the text
    name = re.search(name_pattern, text)
    age = re.search(age_pattern, text)
    gender = re.search(gender_pattern, text)
    background = re.search(background_pattern, text)
    # Extract the matched strings, return an empty string if no match is found
    name = name.group(1) if name else "Anonymous interviewee."
    age = age.group(1) if age else "unknown"
    gender = gender.group(1) if gender else "unknown"
    background = background.group(1) if background else "Unwilling to disclose his background story."

    return name, age, gender, background
