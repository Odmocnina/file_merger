import os

# trida co zpracovava pozadavky na nacteni souboru
# a slouceni jejich obsahu do jednoho vystupniho souboru
class Load_request:

    output_file = None # cesta k vystupnimu souboru
    input_folders = None # seznam zdrojovych adresaru
    accepted_file_types = None # seznam typu souboru, ktere budou zpracovany

    project_directory = None # cesta k projektu, pokud je potreba

    # konstruktro tridy na spojeni souboru
    # parametry:
    # output_file - cesta k vystupnimu souboru
    # input_folders - seznam zdrojovych adresaru oddelenych znakem "|"
    # accepted_file_types - seznam typu souboru, ktere budou zpracovany, oddelenych znakem "|"
    # project_directory - cesta k projektu, pokud je potreba
    def __init__(self, output_file, input_folders, accepted_file_types, project_directory):
        self.output_file = output_file
        self.input_folders = input_folders.split("|")
        self.accepted_file_types = accepted_file_types.split("|")

        self.project_directory = project_directory

    # metoda pro slouceni souboru z jednotlivych zdrojovych adresaru
    # do jednoho vystupniho souboru
    def merge_input_files(self):
        with open(self.output_file, 'w') as outfile:
            for folder in self.input_folders:
                for file in os.listdir(folder):
                    if any(file.endswith(ext) for ext in self.accepted_file_types):
                        outfile.write("---")
                        outfile.write("---")
                        outfile.write("\\")
                        outfile.write("#Directory: " + folder.replace(self.project_directory, "") + "\n")
                        outfile.write("#Script: " + file.replace(self.project_directory, "") + "\n")
                        outfile.write("\\")
                        outfile.write("---")
                        outfile.write("---")
                        file_path = os.path.join(folder, file)
                        with open(file_path, 'r') as infile:
                            outfile.write(infile.read())
                            outfile.write("\n")
