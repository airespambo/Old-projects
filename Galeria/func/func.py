import os
import cv2
import time

class Func:

    ext = ('.jpg', '.jpeg', '.png','.PNG','.JPG','.mp4', '.mkv', '.avi')
    video_ext = ('.mp4', '.mkv', '.avi')

    def get_base_folders(self) -> list:
        base = os.path.expanduser("~")

        folders = [
            os.path.join(base, "Pictures"),
            os.path.join(base, "Videos"),
            os.path.join(base, "Desktop"),
            os.path.join(base, "Downloads"),
        ]

        onedrive_pictures = os.path.join(base, "OneDrive", "Pictures")

        if os.path.exists(onedrive_pictures):
            folders.append(onedrive_pictures)

        return [f for f in folders if os.path.exists(f)]

    def get_files(self) -> list:
        archives = list()

        for folder in self.get_base_folders():
            for root, _, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith(self.ext):
                        archives.append(os.path.join(root, file))

        return archives
    
    def get_albums(self) -> tuple[list, list]:

        albums = list()
        dirs = list()
        for folder in self.get_base_folders():
            for root, _, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith(self.ext):
                        dirs.append(root)
                        albums.append(os.path.basename(root))

        return dirs, albums


    def delete(self, file: str) -> bool:

        try:

            if os.path.exists(file):
                os.remove(file)
            return True
            
        except Exception as e:

            print(e)
            return False
        
    def open_v(self, file: str) -> None:

        os.startfile(file)
    
    def save(self, img, file: str) -> str:

        base, ext = os.path.splitext(file)
        new_path = base + "_edit_" + str(int(time.time())) + ext
        cv2.imwrite(new_path, img)

        return new_path