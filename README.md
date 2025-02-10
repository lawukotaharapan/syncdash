# SyncDash

SyncDash is a Python utility for simplifying the zipping and unzipping of files using native Windows capabilities. It efficiently manages compressed files, allowing you to easily compress directories into `.zip` files and extract them back.

## Features

- **Zip Files**: Compress an entire directory into a single `.zip` file.
- **Unzip Files**: Extract the contents of a `.zip` file into a specified directory.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone the repository or download the `syncdash.py` file.
2. Ensure Python is installed on your system.

## Usage

### Zipping a Folder

To zip a folder, use the `zip_files` method. Provide the name of the folder to be zipped and the desired output file name (without the `.zip` extension).

```python
syncdash.zip_files(folder_name="your_folder", output_name="output_zip_file")
```

### Unzipping a File

To unzip a file, use the `unzip_files` method. Provide the name of the zip file and the directory where you wish to extract its contents.

```python
syncdash.unzip_files(zip_name="your_zip_file.zip", extract_to="output_directory")
```

### Example

```python
if __name__ == "__main__":
    syncdash = SyncDash(base_directory=".")
    
    # Compress a folder named 'documents' into 'archive.zip'
    syncdash.zip_files(folder_name="documents", output_name="archive")
    
    # Extract 'archive.zip' into a folder named 'documents_extracted'
    syncdash.unzip_files(zip_name="archive.zip", extract_to="documents_extracted")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.

## Contact

For questions or suggestions, please contact [your-email@example.com].