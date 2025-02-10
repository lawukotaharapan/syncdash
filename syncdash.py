import os
import shutil
import zipfile
from pathlib import Path

class SyncDash:
    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)
        if not self.base_directory.exists():
            raise FileNotFoundError(f"The directory {self.base_directory} does not exist.")
    
    def zip_files(self, folder_name: str, output_name: str):
        folder_path = self.base_directory / folder_name
        if not folder_path.exists():
            raise FileNotFoundError(f"The folder {folder_name} does not exist in {self.base_directory}.")
        
        output_path = self.base_directory / f"{output_name}.zip"
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = Path(root) / file
                    zipf.write(file_path, file_path.relative_to(folder_path))
        
        print(f"Folder {folder_name} zipped successfully into {output_path}.")

    def unzip_files(self, zip_name: str, extract_to: str):
        zip_path = self.base_directory / zip_name
        extract_path = self.base_directory / extract_to
        
        if not zip_path.exists():
            raise FileNotFoundError(f"The zip file {zip_name} does not exist in {self.base_directory}.")
        
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_path)
        
        print(f"Zip file {zip_name} extracted successfully to {extract_path}.")

if __name__ == "__main__":
    syncdash = SyncDash(base_directory=".")
    
    # Example usage:
    # syncdash.zip_files(folder_name="example_folder", output_name="example_output")
    # syncdash.unzip_files(zip_name="example_output.zip", extract_to="extracted_folder")