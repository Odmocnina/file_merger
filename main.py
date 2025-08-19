import load_request
import config_loader

print("Starting the file merging process...")
config = config_loader.config_loader("config.txt")
requests = config.load_config()

for request in requests:
    request.merge_input_files()