# import yaml
# import os
# import datetime

# def extract_source_code(yaml_file_path):
#     try:
#         # Load the YAML file
#         with open(yaml_file_path, 'r') as file:
#             data = yaml.safe_load(file)

#         # Extract the source code from the YAML
#         source_code = data['cells'][0]['config']['source']

#         return source_code
#     except Exception as e: 
#         print(f"Error occurred while extracting source code: {str(e)}")
#         return None

# def save_source_code(source_code, output_dir):
#     try:
#         # Generate a unique output file name using timestamp
#         timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#         output_file_name = f"output_{timestamp}.py"
        
#         if output_dir:
#             # If output_dir is not empty, save the file in the specified directory
#             os.makedirs(output_dir, exist_ok=True)
#             output_file_path = os.path.join(output_dir, output_file_name)
#         else:
#             # If output_dir is empty, save the file in the current working directory
#             output_file_path = output_file_name

#         # Save the source code to the output file
#         with open(output_file_path, 'w') as file:
#             file.write(source_code)
#         print(f"Source code extracted and saved as {output_file_path}")
#         return output_file_path
#     except Exception as e:
#         print(f"Error occurred while saving source code: {str(e)}")
#         return None
# def main():
#     yaml_file_path = 'hex/py_extraction.yaml'  # Replace with the path to your YAML file
#     output_dir = 'outputs'  # Output directory path

#     # Extract source code from YAML
#     source_code = extract_source_code(yaml_file_path)
#     if source_code:
#         # Save source code to a unique file in the output directory
#         saved_file_path = save_source_code(source_code, output_dir)
#         if saved_file_path:
#             print(f"Saved source code as: {saved_file_path}")

# if __name__ == "__main__":
#     main() 

# import yaml
# import os
# import datetime

# def extract_source_code(yaml_file_path):
#     try:
#         # Load the YAML file
#         with open(yaml_file_path, 'r') as file:
#             data = yaml.safe_load(file)

#         # Extract the source code from the YAML
#         source_code = data['cells'][0]['config']['source']

#         return source_code
#     except Exception as e: 
#         print(f"Error occurred while extracting source code: {str(e)}")
#         return None

# def save_source_code(source_code, yaml_file_path, output_dir):
#     try:
#         # Extract the base name of the YAML file and replace the extension with .py
#         base_name = os.path.splitext(os.path.basename(yaml_file_path))[0]
#         output_file_name = f"{base_name}.py"

#         if output_dir:
#             # If output_dir is not empty, save the file in the specified directory
#             os.makedirs(output_dir, exist_ok=True)
#             output_file_path = os.path.join(output_dir, output_file_name)
#         else:
#             # If output_dir is empty, save the file in the current working directory
#             output_file_path = output_file_name

#         # Save the source code to the output file
#         with open(output_file_path, 'w') as file:
#             file.write(source_code)
#         print(f"Source code extracted and saved as {output_file_path}")
#         return output_file_path
#     except Exception as e:
#         print(f"Error occurred while saving source code: {str(e)}")
#         return None

# def main():
#     yaml_file_path = 'TURNOVER/turnover_forecast.yaml'  # Replace with the path to your YAML file
#     output_dir = 'outputs'  # Output directory path

#     # Extract source code from YAML
#     source_code = extract_source_code(yaml_file_path)
#     if source_code:
#         # Save source code to a file in the output directory with the same name as the YAML file
#         saved_file_path = save_source_code(source_code, yaml_file_path, output_dir)
#         if saved_file_path:
#             print(f"Saved source code as: {saved_file_path}")

# if __name__ == "__main__":
#     main()


# import yaml
# import os
# import datetime

# def extract_source_code(yaml_file_path):
#     try:
#         # Load the YAML file
#         with open(yaml_file_path, 'r') as file:
#             data = yaml.safe_load(file)

#         # Initialize a counter for occurrences of 'source'
#         source_count = 0
#         source_code = None

#         # Recursive function to search for the second occurrence of 'source'
#         def find_second_source(node):
#             nonlocal source_count, source_code
#             if isinstance(node, dict):
#                 for key, value in node.items():
#                     if key == 'source':
#                         source_count += 1
#                         if source_count == 2:
#                             source_code = value
#                             return
#                     find_second_source(value)
#             elif isinstance(node, list):
#                 for item in node:
#                     find_second_source(item)

#         # Start the search from the root of the YAML data
#         find_second_source(data)

#         if source_code:
#             return source_code
#         else:
#             print("Second occurrence of 'source' not found.")
#             return None
#     except Exception as e:
#         print(f"Error occurred while extracting source code: {str(e)}")
#         return None

# def save_source_code(source_code, yaml_file_path, output_dir):
#     try:
#         # Extract the base name of the YAML file and replace the extension with .py
#         base_name = os.path.splitext(os.path.basename(yaml_file_path))[0]
#         output_file_name = f"{base_name}.py"

#         if output_dir:
#             # If output_dir is not empty, save the file in the specified directory
#             os.makedirs(output_dir, exist_ok=True)
#             output_file_path = os.path.join(output_dir, output_file_name)
#         else:
#             # If output_dir is empty, save the file in the current working directory
#             output_file_path = output_file_name

#         # Save the source code to the output file
#         with open(output_file_path, 'w') as file:
#             file.write(source_code)
#         print(f"Source code extracted and saved as {output_file_path}")
#         return output_file_path
#     except Exception as e:
#         print(f"Error occurred while saving source code: {str(e)}")
#         return None

# def main():
#     yaml_file_path = 'hex/py_extraction.yaml'  # Replace with the path to your YAML file
#     output_dir = 'outputs'  # Output directory path

#     # Extract source code from YAML
#     source_code = extract_source_code(yaml_file_path)
#     if source_code:
#         # Save source code to a file in the output directory with the same name as the YAML file
#         saved_file_path = save_source_code(source_code, yaml_file_path, output_dir)
#         if saved_file_path:
#             print(f"Saved source code as: {saved_file_path}")

# if __name__ == "__main__":
#     main()




# import yaml
# import os
# import datetime

# def extract_source_code(yaml_file_path):
#     try:
#         # Load the YAML file
#         with open(yaml_file_path, 'r') as file:
#             data = yaml.safe_load(file)

#         # Initialize a counter for occurrences of 'source'
#         source_count = 0
#         source_code = None

#         # Recursive function to search for the second occurrence of 'source'
#         def find_second_source(node):
#             nonlocal source_count, source_code
#             if isinstance(node, dict):
#                 for key, value in node.items():
#                     if key == 'source':
#                         source_count += 1
#                         if source_count == 2:
#                             source_code = value
#                             return
#                     find_second_source(value)
#             elif isinstance(node, list):
#                 for item in node:
#                     find_second_source(item)

#         # Start the search from the root of the YAML data
#         find_second_source(data)

#         if source_code:
#             return source_code
#         else:
#             print("Second occurrence of 'source' not found.")
#             return None
#     except Exception as e:
#         print(f"Error occurred while extracting source code: {str(e)}")
#         return None

# def save_source_code(source_code, yaml_file_path, output_dir):
#     try:
#         # Extract the base name of the YAML file and replace the extension with .py
#         base_name = os.path.splitext(os.path.basename(yaml_file_path))[0]
#         output_file_name = f"{base_name}.py"

#         if output_dir:
#             # If output_dir is not empty, save the file in the specified directory
#             os.makedirs(output_dir, exist_ok=True)
#             output_file_path = os.path.join(output_dir, output_file_name)
#         else:
#             # If output_dir is empty, save the file in the current working directory
#             output_file_path = output_file_name

#         # Save the source code to the output file
#         with open(output_file_path, 'w') as file:
#             file.write(source_code)
#         print(f"Source code extracted and saved as {output_file_path}")
#         return output_file_path
#     except Exception as e:
#         print(f"Error occurred while saving source code: {str(e)}")
#         return None

# def main():
#     yaml_file_path = 'hex/turnover_forecast.yaml'  # Replace with the path to your YAML file
#     output_dir = 'outputs'  # Output directory path

#     # Extract source code from YAML
#     source_code = extract_source_code(yaml_file_path)
#     if source_code:
#         # Save source code to a file in the output directory with the same name as the YAML file
#         saved_file_path = save_source_code(source_code, yaml_file_path, output_dir)
#         if saved_file_path:
#             print(f"Saved source code as: {saved_file_path}")

# if __name__ == "__main__":
#     main()





import yaml
import os

def extract_source_code(yaml_file_path):
    try:
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)

        source_count = 0
        source_code = None

        def find_second_source(node):
            nonlocal source_count, source_code
            if isinstance(node, dict):
                for key, value in node.items():
                    if key == 'source':
                        source_count += 1
                        if source_count == 2:
                            source_code = value
                            return
                    find_second_source(value)
            elif isinstance(node, list):
                for item in node:
                    find_second_source(item)

        find_second_source(data)

        if source_code:
            return source_code
        else:
            print("Second occurrence of 'source' not found.")
            return None
    except Exception as e:
        print(f"Error occurred while extracting source code: {str(e)}")
        return None

def save_source_code(source_code, yaml_file_path, output_dir):
    try:
        base_name = os.path.splitext(os.path.basename(yaml_file_path))[0]
        output_file_name = f"{base_name}.py"

        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            output_file_path = os.path.join(output_dir, output_file_name)
        else:
            output_file_path = output_file_name

        with open(output_file_path, 'w') as file:
            file.write(source_code)
        print(f"Source code extracted and saved as {output_file_path}")
        return output_file_path
    except Exception as e:
        print(f"Error occurred while saving source code: {str(e)}")
        return None

def main():
    yaml_file_path = 'hex/turnover_forecast.yaml'
    output_dir = 'outputs'

    source_code = extract_source_code(yaml_file_path)
    if source_code:
        saved_file_path = save_source_code(source_code, yaml_file_path, output_dir)
        if saved_file_path:
            print(f"Saved source code as: {saved_file_path}")

if __name__ == "__main__":
    main()


