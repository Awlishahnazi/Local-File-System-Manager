
# Local File System Manager

A Python-based Object-Oriented wrapper for managing local files and directories. This project simulates core Operating System file system operations, providing robust error handling and a clean API for file manipulation.

> **📅 Project Timeline:** This project was originally developed and completed in **Autumn 2024** (University Term 5) as part of my Operating Systems coursework. It is uploaded here to document my continuous learning journey in System Design and Python.

## Core Operations

The `LocalFileSystemManager` class provides 6 primary methods that mimic standard OS commands:

1. **Create File (`create_file`):** Creates a new file in a specified directory, creating the directory if it doesn't exist.
2. **Delete File (`delete_file`):** Safely removes a file from the system.
3. **Rename/Move (`rename_file_or_folder`):** Renames or moves files and directories.
4. **List Directory (`list_directory_contents`):** Lists all files and folders in a given path (similar to `ls` or `dir`).
5. **Search (`search`):** Recursively searches for a keyword within file and folder names (similar to `find` or `grep`).
6. **File Info (`get_file_info`):** Retrieves metadata such as file size, extension, and last modified time.

## Key Features

* **Robust Error Handling:** Every method is wrapped in `try...except` blocks to prevent the program from crashing due to permission errors or invalid paths.
* **Object-Oriented Design:** Encapsulates all file operations into a single, reusable class.
* **Recursive Search:** Utilizes `os.walk` for efficient directory tree traversal.
* **Type Hinting:** Uses Python 3 type hints for better code readability and maintainability.

## Tech Stack

* **Python 3.x**
* **OS Module** (Built-in)

## How to Run

1. Clone the repository:

   ```
   git clone https://github.com/Awlishahnazi/Local-File-System-Manager.git
   ```
2. Navigate to the project directory:

   ```
   cd Local-File-System-Manager
   ```
3. Run the script:

   ```
   python "Local File System Manager.py"
   ```

## Author

**Ali Shahnazi Bejarsari**

* [GitHub Profile](https://github.com/Awlishahnazi)
* [LinkedIn](https://www.linkedin.com/in/ali-shahnazi-bejarsari-678bba342)
* [Personal Portfolio](https://alishahnazi.ir/)
