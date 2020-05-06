""" """

import sys
import subprocess
import typing

def generate_caption(path_to_image: str) -> str:
    """ """

    p = subprocess.Popen([
        ".\\describe\\processing\\captions\\tf1-14\\Scripts\\python.exe", 
        ".\\describe\\processing\\captions\\show_and_tell\\main.py",
        path_to_image],
        shell=True, 
        stdout=subprocess.PIPE)

    # Wait for subprocess to finish
    p_status = p.wait()
    out, err = p.communicate()

    out = out.decode('utf-8')
    out = out.split('\n')[-1]
    return out