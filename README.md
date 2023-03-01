
# Wallpaper Randomizer

This was made for BSPWM, but really with some editing it can be used for any Window Manager as long as it uses 'feh' in it's config file for the wallpaper.


## Installation

    1. Clone it anywhere on the computer.
    2. Edit the "wallpaper_dir" and "config_file" for you're system path's.
       Also to restart my BSPWM I use "Win+Alt+R" if you use something
       else you will have to change the "pyautogui.hotkey(YOUR HOTKEY)".
    3. Make sure you have images in you're "wallpaper_dir". (Only .png or .jpg)
    4. Install dependencies (Tkinter, and PyAutoGui). I used "sudo pacman -S tk"
       and "pip install PyAutoGui".
    5. Run it as "python wallpaper.py". If I didn't missout on dependencies to
       install or things to edit it should work.