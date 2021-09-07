# logitech-color-combo
A script which allows you to easily display all matching key combinations on your RGB keyboard.

## Compatible Keyboards
The script ist currently using [g810-led](https://github.com/MatMoul/g810-led) to control the LEDs of following Keyboards:
- G213 Prodigy
- G410 Atlas Spectrum
- G413 Carbon
- G512 Carbon
- G513 Carbon
- G610 Orion Brown
- G610 Orion Red
- G810 Orion Spectrum
- G815 LIGHTSYNC
- G910 Orion Spark
- G910 Orion Spectrum
- GPRO

## Install on Linux

Just download the [ColorCoding.py](https://gitlab.com/p3t1/logitech-color-combo/-/blob/main/ColorCoding.py) (if you want you can download an [example config](https://gitlab.com/p3t1/logitech-color-combo/-/blob/main/Keyboard.yaml) too), and save it anywhere you like.

After you created a config file (if you haven't downloaded the example one), you can add a key to turn the script on and off:
##### on KDE plasma
Go to the settings. Go to "Workspace" > "Shortcuts". In "Custom Shortcus", create a new shortcut, and instert

`/usr/bin/python3 /[path]/ColorCoding.py /[path]/Keyboard.yaml`

under "Action". If you're not using Keyboard.yaml as config, make shure to change it to the name of your config file.
##### on GNOME
Go to the settings. Go to "Keyboard" > "Customize Shortcuts" > "Own Shortcuts" and click on "Add Shortcut". Insert

`/usr/bin/python3 /[path]/ColorCoding.py /[path]/Keyboard.yaml`

as command.

## Configure

