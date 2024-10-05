# logitech-color-combo
A script which allows you to easily display all matching key combinations on your RGB keyboard. It automatically displays the preconfigured keyboard shortcuts based on the currently active window, also each window can have its own color scheme.

## Compatible Keyboards
haven't tested yet, but should be compatible with all keyboards that work with Aura Sync / Aura Creator (works on my Laptop keyboard)

## Install on Linux

### Dependencies

- python
- pynput (`pip install pynput`)
- pywin32 (`pip install pywin32`)
- asyncio (`pip install asyncio`)
- wmi (`pip install wmi`)

### Get it to work

Just download the [ColorCoding.py](https://github.com/Peti253/logitech-color-combo/blob/main/ColorCoding.py) (if you want you can download the [example config](https://github.com/Peti253/logitech-color-combo/blob/main/Keyboard.yaml), tested on KDE), and save it anywhere you like. Don't forget to make the python file executable!
When starting the script while it's running, it kills itself. This way you can set a hotkey (e.g. with AutoHotkey) to start and stop the Script

## Configure

The config consists of classes that can be imported from each other and contain both the color data of the keys and the shortcuts. Make shure you have a class called `[standard]`, which the script will use, if you havent configuered specific shortcuts or key colours for the currently active window. You can put any program name in these brackets so that the scheme is applied only to that specific program. For example, if I have a class named `[krita]`, all keyboard shortcuts written in this class will be displayed only if krita is the currently active window. If you are not sure what the process is actually called, a look at the System Monitor might be worth a try.

Inside the classes you can use the following commands (key and group names are imported from g810-led):

| Command | Funtcion | Example | Explanation |
| ------ | ------ | ------ | ------ |
| **i** | Import | i standard | imports everything from standard to the current class |
| **k** | set key colour | k g ff0000 | sets the colour of the G-key to red |
| **a** | set the colour of all keys | a ffffff | sets all keys to white |
| **g** | set key-group colour | g modifiers 0000ff| sets all modifiers to blue |
| **c** | shortcut with ctrl | c v 00ff00  | sets the colour of V to green if ctrl is pressed |
| **m** | shortcut with meta | m e ffff00 | sets the colour of E to yellow if meta is pressed |
| **x** | shortcut with alt | x f4 ff0000| sets the colour of the F4-Key to red if alt is pressed |
| **s** | shortcut with shift | s a 0000ff | sets the colour of a to blue if shift is pressed |
| **b** | block | b s | blocks the shift key, so nothing changes, if only the shift key is pressed |

You can combine **c**, **m**, **x** and **s** to make bigger shortcuts, for example `cx t 00ff00` would make the T-Key green if both ctrl **and** alt are pressed.

Flatpaks are unfortunately all called the same. At least under KDE they are called "kthreadd", so you can only create and use one configuration for all Flatpaks together.

With all that information we can define a simple config:
```
[standard]
    b s
    a ffffff
    m 0000ff
    c x 00ffff
    c c 00ffff
    c v 00ffff
    
[test]
    i standard
    k w ff0000
    k a ff0000
    k s ff0000
    k d ff0000
```
