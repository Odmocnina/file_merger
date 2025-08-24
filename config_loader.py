from load_request import Load_request

# trida co nacte konfiguraci ze souboru
# a vrati seznam Load_request objektu
class config_loader:
    config_file = None # cesta k souboru s konfiguraci
    config_signature = "#file_merger_config" # znak, ktery oznacuje zacatek konfiguracniho souboru
    new_config_mark = "#section" # znak, ktery oznacuje zacatek nove konfigurace
    project_directory_mark = "project_directory" # znak, ktery oznacuje cestu k projektu
    file_mark = "file" # znak, ktery oznacuje typ souboru, ktery bude zpracovan
    source_mark = "source" # znak, ktery oznacuje zdrojovy adresar
    ext_mark = "ext" # znak, ktery oznacuje typ souboru, ktery bude zpracovan
    project_directory_position = 1 # pozice, na ktere se nachazi cesta k projektu v konfiguraci

    # Konstruktor pro nacteni konfiguracniho souboru
    # parametry:
    # config_file - cesta k souboru s konfiguraci
    def __init__(self, config_file):
        self.config_file = config_file

    # nacte konfiguraci ze souboru
    # vraci seznam Load_request objektu
    # kazdy objekt obsahuje informace o vystupnim souboru, zdrojovych adresarich a typu souboru
    def load_config(self):
        configs = []
        with open(self.config_file, "r") as file:
            lines = file.readlines()
        outfile = None
        source = None
        file_types = None
        project_directory = None
        i = 0
        for line in lines:
            print(line)
            line = line.strip()
            if line == "":
                continue
            if i == 0 and not line.startswith(self.config_signature):
                print("Invalid configuration file format, missing signature.")
                return []
            if i == self.project_directory_position and not line.startswith(self.project_directory_mark):
                print("Invalid configuration file format, missing project directory mark.")
                return []
            else:
                if line.startswith(self.project_directory_mark):
                    project_directory = line.split("=", 1)[1].strip()
                    print(f"Project directory found: {project_directory}")
            if line.startswith(self.file_mark):
                outfile = line.split("=", 1)[1].strip()
            elif line.startswith(self.source_mark):
                source = line.split("=", 1)[1].strip()
            elif line.startswith(self.ext_mark):
                file_types = line.split("=", 1)[1].strip()
            if (line.startswith(self.new_config_mark) or i == len(lines) - 1) and i > 2:
                if outfile is not None and source is not None and file_types is not None:
                    print("Creating new configuration")
                    configs.append(
                        Load_request(outfile, source, file_types, project_directory)
                    )
                    outfile = None
                    source = None
                    file_types = None
                else:
                    print("Incomplete configuration found, skipping...")
                    print("Expected: outfile, source, file_types")
                    outfile = None
                    source = None
                    file_types = None
            i = i + 1

        if outfile is not None and source is not None and file_types is not None:
            print("Creating new configuration")
            configs.append(
                Load_request(outfile, source, file_types, project_directory)
            )
        else:
            print("Incomplete configuration found, skipping...")
            print("Expected: outfile, source, file_types")

        return configs
