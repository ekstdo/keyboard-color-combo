#!/usr/bin/python3

import subprocess
import asyncio
from pynput import keyboard
import sys, os
state = {}
importstate = {}
blockstate = {}
cache = open (".tmp","w")
current = "standard"
keystate = 0 #Shift(s), Ctrl(c), Meta(m), Alt(x)
lockfilename = "/tmp/.keyboardlock"
terminatorfilename = "/tmp/.keyboardexit"

if os.path.exists(lockfilename):
    terminator = open(terminatorfilename,"a")
    terminator.write("astala vista baby")
    terminator.close()
    sys.exit()
else:
    lockfile = open(lockfilename,"a")
    lockfile.write ("wer das liest ist dumm")
    lockfile.close()

def run (*args):
    subprocess.run(["g810-led",*args])
    
def changekey (key, color):
    run ("-kn",key,color)
    
def changeall (color):
    run ("-an",color)

def changegroup (group, color):
    run ("-gn",group,color)
    
def commit ():
    run("-c")

def encoding(x):
    enc = 0
    if "s" in x:
        enc = enc | 0b1000
    if "c" in x:
        enc = enc | 0b0100
    if "m" in x:
        enc = enc | 0b0010
    if "x" in x:
        enc = enc | 0b0001
    return enc

def loadfile(filename):
    cfgfile = open (filename)
    lines = (cfgfile.readlines())
    strippedlines = map (lambda line: line.strip ("\t\n "), lines)
    filteredlines = filter (lambda line: line != "", strippedlines)
    splitlines = map (lambda line: line.split(), filteredlines)
    currentprogram = "standard"
    for line in splitlines:
        if line[0].startswith("["):
            currentprogram = line[0].strip("[]")
            state[currentprogram] = []
            importstate[currentprogram] = []
            blockstate[currentprogram] = []
        else:
            if line[0] == "i":
                importstate[currentprogram].append(line[1])
                continue
            if line[0] == "b":
                b = encoding(line[1])
                blockstate[currentprogram].append(b)
            if line[0][0] in "scmx":
                line[0] = encoding(line[0])
            state[currentprogram].append(line)
    for program,modulelist in importstate.items():
        modules = []
        while len(modulelist) > 0:
            module = modulelist.pop()
            if module in modules:
                continue
            modules.append(module)
            modulelist.extend(importstate[module])
        importstate[program] = modules
    for program,modulelist in importstate.items():
        blocked2d = map(lambda module: blockstate[module],modulelist)
        blockstate[program].extend(list(set(i for innerlist in blocked2d for i in innerlist)))

def onpress (key):
    global keystate
    lastkeystate = keystate
    key=str(key).strip("'")
    if key == "Key.shift" or key == "Key.shift_r":
        keystate = keystate | 0b1000
    if key == "Key.ctrl" or key == "Key.ctrl_r":
        keystate = keystate | 0b0100
    if key == "Key.cmd":
        keystate = keystate | 0b0010
    if key == "Key.alt":
        keystate = keystate | 0b0001
    if lastkeystate != keystate:
        render()
        
def onrelease (key):
    global keystate
    lastkeystate = keystate
    key=str(key).strip("'")
    if key == "Key.shift" or key == "Key.shift_r":
        keystate = keystate & 0b0111
    if key == "Key.ctrl" or key == "Key.ctrl_r":
        keystate = keystate & 0b1011
    if key == "Key.cmd":
        keystate = keystate & 0b1101
    if key == "Key.alt":
        keystate = keystate & 0b1110
    if lastkeystate != keystate:
        render()
        
def render():
    keylist = state[current]
    for module in importstate[current]:
        keylist = state[module] + keylist
    if keystate == 0:
        cache = open (".tmp","w")
        for k in keylist:
            if str(k[0]) in "kga":
                cache.write(" ".join(k) + "\n")
        cache.write ("c")
        cache.close()
        run ("-p",".tmp")
    elif keystate not in blockstate[current]:
        cache = open (".tmp","w")
        changeall("000000")
        for k in filter (lambda k:k[0] == keystate,keylist):
            cache.write("k "+" ".join(k[1:]) + "\n")
        cache.write ("c")
        cache.close()
        run ("-p",".tmp")
    
listener=keyboard.Listener (on_press=onpress,on_release=onrelease)
listener.start()

loadfile ("Keyboard.yaml" if len(sys.argv) == 1 else sys.argv[1])

onrelease (None)

def findactivewindow():
    result = ""
    try:
        result = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowpid"]).decode("utf-8").strip()
    except:
        pass
    if result != "":
        processfile = open (f"/proc/{result}/comm")
        process = processfile.read()
        processfile.close()
        return process.lower().strip()
    return ""

async def mainloop():
    global current
    while True:
        await asyncio.sleep(0.2)
        if os.path.exists(terminatorfilename):
            os.remove(terminatorfilename)
            os.remove(lockfilename)
            break
        oldwindowname = current
        windowname = findactivewindow()
        if oldwindowname != windowname and windowname in state.keys():
            current = windowname
            render()
        elif windowname in state.keys():
            render()
        else:
            current = "standard"
            render()

asyncio.run(mainloop())
