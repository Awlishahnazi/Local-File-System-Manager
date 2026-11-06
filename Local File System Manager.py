import os
from typing import List, Dict

class LocalFileSystemManager:
    def __init__(self):
        pass

    def create_file(self, file_name: str, folder_path: str) -> str:
        try:
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'w') as file:
                pass
            return f"File '{file_name}' created successfully in '{folder_path}'."
        except Exception as e:
            return f"Error creating file: {str(e)}"

    def delete_file(self, file_path: str) -> str:
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                return f"File '{file_path}' deleted successfully."
            return f"File '{file_path}' does not exist."
        except Exception as e:
            return f"Error deleting file: {str(e)}"

    def rename_file_or_folder(self, old_path: str, new_path: str) -> str:
        try:
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                return f"Renamed '{old_path}' to '{new_path}'."
            return f"'{old_path}' does not exist."
        except Exception as e:
            return f"Error renaming: {str(e)}"

    def list_directory_contents(self, folder_path: str) -> List[str]:
        try:
            if os.path.isdir(folder_path):
                return os.listdir(folder_path)
            return []
        except Exception as e:
            return [f"Error listing directory: {str(e)}"]

    def search(self, keyword: str, folder_path: str) -> List[str]:
        results = []
        try:
            for root, dirs, files in os.walk(folder_path):
                results.extend([os.path.join(root, name) for name in files + dirs if keyword in name])
            return results
        except Exception as e:
            return [f"Error searching directory: {str(e)}"]

    def get_file_info(self, file_path: str) -> Dict[str, str]:
        try:
            if os.path.isfile(file_path):
                stat_info = os.stat(file_path)
                return {
                    "name": os.path.basename(file_path),
                    "size": f"{stat_info.st_size} bytes",
                    "type": os.path.splitext(file_path)[-1],
                    "last_modified": f"{stat_info.st_mtime}"
                }
            return {"error": "File does not exist."}
        except Exception as e:
            return {"error": f"Error retrieving file info: {str(e)}"}


manager = LocalFileSystemManager()


data = {
    "operation": "create_file",
    "file_name": "example.txt",
    "folder_path": "./documents"
}


if data["operation"] == "create_file":
    result = manager.create_file(data["file_name"], data["folder_path"])
    print(result)
    print("Current files:", manager.list_directory_contents(data["folder_path"]))
