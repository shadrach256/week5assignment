import os

def process_file():
    """
    Reads a file, modifies its content, and writes to a new file
    with robust error handling at each step.
    """
    print("=== File Processing Program ===")
    print("This program will read a file, modify its content,")
    print("and save the modified version to a new file.\n")
    
    # Get input file with error handling
    while True:
        input_path = input("Enter the input file path: ").strip()
        if not input_path:
            print("Error: Please enter a file path.")
            continue
            
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            break
        except FileNotFoundError:
            print(f"Error: File '{input_path}' not found.")
        except PermissionError:
            print(f"Error: No permission to read '{input_path}'.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode '{input_path}' as UTF-8 text.")
        except Exception as e:
            print(f"Error reading file: {str(e)}")
    
    # Process content (example: uppercase conversion)
    modified_content = content.upper()
    # Alternative modifications you could use:
    # modified_content = content.lower()  # lowercase
    # modified_content = content[::-1]   # reverse content
    
    # Get output file with error handling
    while True:
        output_path = input("Enter the output file path: ").strip()
        if not output_path:
            print("Error: Please enter an output path.")
            continue
            
        if os.path.exists(output_path):
            print(f"Warning: '{output_path}' already exists.")
            overwrite = input("Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                continue
                
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"\nSuccess! Modified content saved to '{output_path}'")
            print(f"Original size: {len(content)} bytes")
            print(f"New size: {len(modified_content)} bytes")
            break
        except PermissionError:
            print(f"Error: No permission to write to '{output_path}'.")
        except Exception as e:
            print(f"Error writing file: {str(e)}")

if __name__ == "__main__":
    process_file()
    