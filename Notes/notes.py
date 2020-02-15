import sys
from builtins import str
from datetime import datetime
import os


class NoteAutomator:
    python = ".py"
    java = ".java"
    text = ".txt"
    markdown = ".md"

    extensions = {
        "python" : python,
        ".py" : python,
        "py" : python,
        "text" : text,
        ".txt" : text,
        "java" : java,
        ".java" : java,
        "markdown": markdown,
        ".md": markdown,
        "md": markdown,
    }

    extension = ""
    folderName = ""
    fileName = ""

    def get_folder_name(self, folder_num):
        try:
            self.folderName = str(sys.argv[folder_num])
        except Exception:
            self.folderName = "General"


    def name_file(self):
        if self.fileName == "":
            self.fileName = datetime.today().strftime('%Y-%m-%d') + self.extension


    def create_file_in_folder(self):
        os.chdir('/Users/nirmitshah/Dropbox/')
        if os.path.isdir("./" + self.folderName):
            os.chdir("./" + self.folderName)
        else:
            os.mkdir(self.folderName)
            os.chdir("./" + self.folderName)

        if os.path.isdir("./" + "notes"):
            os.chdir("./" + "notes")
        else:
            os.mkdir("notes")
            os.chdir("./" + "notes")
        if not os.path.isfile("./" + self.fileName):
            open(self.fileName, "a").close()
        os.system("code " + self.fileName)

if __name__ == "__main__":
    notes = NoteAutomator()
    command = sys.argv[1]
    # note folder
    # python nf cs1332
    if command == "nf":
        # create a markdown file named with today's date in the notes subfolder in the folder
        # specified
        notes.get_folder_name(2)
        notes.extension = notes.markdown
        notes.name_file()
        notes.create_file_in_folder()

        
        
