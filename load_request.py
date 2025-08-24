import os

# trida co zpracovava pozadavky na nacteni souboru
# a slouceni jejich obsahu do jednoho vystupniho souboru
class Load_request:

    output_file = None # cesta k vystupnimu souboru
    input_folders = None # seznam zdrojovych adresaru
    accepted_file_types = None # seznam typu souboru, ktere budou zpracovany

    project_directory = None # cesta k projektu, pokud je potreba
    use_poject_directory_mark = "[pd]"

    # konstruktro tridy na spojeni souboru
    # parametry:
    # output_file - cesta k vystupnimu souboru
    # input_folders - seznam zdrojovych adresaru oddelenych znakem "|"
    # accepted_file_types - seznam typu souboru, ktere budou zpracovany, oddelenych znakem "|"
    # project_directory - cesta k projektu, pokud je potreba
    def __init__(self, output_file, input_folders, accepted_file_types, project_directory):
        self.project_directory = project_directory
        self.output_file = output_file
        self.output_file = self.process_file_or_foler(self.output_file)
        self.input_folders = input_folders.split("|")
        for i in range(len(self.input_folders)):
            self.input_folders[i] = self.process_file_or_foler(self.input_folders[i])
        print(self.output_file)
        self.accepted_file_types = accepted_file_types.split("|")

    def process_file_or_foler(self, file_or_folder):
        if file_or_folder.startswith(self.use_poject_directory_mark):
            file_or_folder = file_or_folder.replace(self.use_poject_directory_mark, self.project_directory)
        else:
            file_or_folder = file_or_folder
        return file_or_folder

    # metoda pro slouceni souboru z jednotlivych zdrojovych adresaru
    # do jednoho vystupniho souboru
    def merge_input_files(self):
        with open(self.output_file, 'w') as outfile:
            for folder in self.input_folders:
                for file in os.listdir(folder):
                    if any(file.endswith(ext) for ext in self.accepted_file_types):
                        outfile.write("---\n")
                        outfile.write("---\n")
                        #outfile.write("\\n")
                        outfile.write("#Directory: " + folder.replace(self.project_directory + "\\", "") + "\n")
                        outfile.write("#Script: " + file.replace(self.project_directory + "\\", "") + "\n")
                        #outfile.write("\\n")
                        outfile.write("---\n")
                        outfile.write("---\n")
                        file_path = os.path.join(folder, file)
                        with open(file_path, 'r') as infile:
                            outfile.write(infile.read())
                            outfile.write("\n")
