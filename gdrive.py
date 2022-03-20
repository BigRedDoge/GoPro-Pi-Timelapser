from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.settings import LoadSettingsFile

GDRIVE_SETTINGS = "./config/settings.yaml"

class GoogleDrive:

    """
    
    """
    def __init__(self, folder_name):
        self.folder_name = folder_name
        
        gauth = GoogleAuth()
        gauth.settings = LoadSettingsFile(filename=GDRIVE_SETTINGS)
        gauth.CommandLineAuth()
        self.drive = GoogleDrive(gauth)

        self.folder_id = self.create_folder(folder_name)

    """
    Create new folder in Google Drive and return Folder ID
    """
    def create_folder(self, name):
        pass
    
    def save_image(self, image_path):
        pass