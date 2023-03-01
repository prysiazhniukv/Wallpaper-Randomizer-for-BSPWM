import os
import random
import fileinput
import shutil
import tempfile
import pyautogui


wallpaper_dir = "/home/vlad/Desktop/wallpapers" #Replace with you're wallpapers folder
config_file = "/home/vlad/.config/bspwm/bspwmrc" # Replace with the path to your bspwm config file

images = [f for f in os.listdir(wallpaper_dir) if f.endswith('.png') or f.endswith('.jpg')]

if images:
    random_image = random.choice(images)

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        with open(config_file, 'r') as original_file:
            for line in original_file:
                if line.startswith("feh"):
                    temp_file.write("feh --bg-fill " + os.path.join(wallpaper_dir, random_image) + " &" + "\n")
                else:
                    temp_file.write(line)
    
    shutil.move(temp_file.name, config_file)
else:
    print("No image files found in the wallpaper directory.")

current_permissions = os.stat(config_file).st_mode

new_permissions = current_permissions | 0o555

os.chmod(config_file, new_permissions)

pyautogui.hotkey('win', 'alt', 'r')

