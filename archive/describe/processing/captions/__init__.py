""" """

import sys
import subprocess


from typing import *

def generate_caption(path_to_image: str) -> str:
    """ """

    p = subprocess.Popen([
        ".\\describe\\processing\\captions\\tf1-14\\Scripts\\python.exe", 
        ".\\describe\\processing\\captions\\show_and_tell\\main.py",
        path_to_image,],
        shell=True, 
        stdout=subprocess.PIPE)

    # Wait for subprocess to finish
    p_status = p.wait()
    out, err = p.communicate()
    out = out.decode('utf-8')
    return out


def generate_bulk_captions(paths_to_images: List[str]) -> Iterable[str]:
    """ """

    print("Starting Bulk Caption Generation Process")
    p = subprocess.Popen([
        ".\\describe\\processing\\captions\\tf1-14\\Scripts\\python.exe", 
        ".\\describe\\processing\\captions\\show_and_tell\\main.py",
        ','.join([path for path in paths_to_images]),
        "bulk"],
        shell=True, 
        stdout=subprocess.PIPE)

    print("> Reading input")
    while True:
        line = p.stdout.readline()
        line = line.decode('utf-8').strip()
        print(line)
        if line == "done":
            break
        elif not line.startswith("caption:"):
            continue
        else:
            print(f">> Generated caption: {line[8:]}")
            yield line[8:]
        
    print("> Bulk Caption Generation finished")
