# File Merger

This project is a simple Python tool for automatically merging the content of multiple files from different directories into a single output file. It is ideal for merging `.css`, `.js`, or other text files.

## 🌟 Key Features
* **Extension-based Merging:** The tool processes only files with the specified extensions (e.g., `asp|css|aspx|js`).
* **Smart Text Encoding:** The script primarily reads files in `UTF-8`. If it encounters an error, it automatically falls back to `CP1250` (Windows Central European) and, as a last resort, `latin-1`.
* **Output Comments:** The script automatically inserts headers into the final merged file, indicating the source directory and file for each code segment.
* **Dynamic Paths:** The configuration allows the use of the `[pd]` (Project Directory) placeholder, which is automatically replaced with the set project path.

## 📂 Project Structure
* `main.py` *(or the name of your main file)* – The entry point script that loads the configuration and starts the merging process.
* `config_loader.py` – Contains the `config_loader` class, which parses the configuration file and validates its format.
* `load_request.py` – Contains the `Load_request` class, responsible for opening, reading, handling encoding, and merging the files into the output.
* `config.txt` – A text file defining the script's behavior.

## ⚙️ Configuration (`config.txt`) Overview
Settings are read from the `config.txt` file, which must follow a specific format. The file must always start with the `#file_merger_config` signature, followed by the project path defined via `project_directory=`. 

Individual merging tasks are separated by the `#section` tag.

**Example `config.txt`:**
```text
#file_merger_config
project_directory=C:\Users\Michael\Documents\prace\file_merger\css_stuff_to_merge\css

#section
file=C:\Users\Michael\Documents\prace\file_merger\css_stuff_to_merge\output\merged_styles.css
source=[pd]
ext=asp|css|aspx|js