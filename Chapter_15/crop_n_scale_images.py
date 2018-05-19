"""crop images of a planet to a tightly-fitting box around the planet."""
import os
import sys
import shutil
from PIL import Image, ImageOps

def main():
    """Get starting folder, copy folder, run crop function, clean folder."""
    # get name of folder in cwd with original video frames
    frames_folder = 'video_frames'

    # prepare files & folders
    del_folders('cropped')
    shutil.copytree(frames_folder, 'cropped')

    # run cropping function
    print("start cropping and scaling...")
    os.chdir('cropped')
    crop_images()
    clean_folder(prefix_to_save='cropped')  # delete uncropped originals
    
    print("Done! \n")
    
def del_folders(name):
    """If a folder with a named prefix exists in directory delete it."""
    contents = os.listdir()
    for item in contents:
        if os.path.isdir(item) and item.startswith(name):
            shutil.rmtree(item)

def clean_folder(prefix_to_save):
    """Delete all files in folder except those with a named prefix."""
    files = os.listdir()
    for file in files:
        if not file.startswith(prefix_to_save):
            os.remove(file)

def crop_images():
    """Automatically crop and scale images of a planet to box around planet."""
    files = os.listdir()
    for file_num, file in enumerate(files, start=1):
        with Image.open(file) as img:
            gray = img.convert('L')
            bw = gray.point(lambda x: 0 if x < 90 else 255)
            box = bw.getbbox()       
            padded_box = (box[0]-20, box[1]-20, box[2]+20, box[3]+20)
            cropped = img.crop(padded_box)
            scaled = ImageOps.fit(cropped, (860, 860),
                                  Image.LANCZOS, 0, (0.5, 0.5))
            file_name = 'cropped_{}.jpg'.format(file_num)
            scaled.save(file_name, "JPEG")
  

if __name__ == '__main__':
    main()
