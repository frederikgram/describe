""" """

import os
import sys
import subprocess

from typing import List, Dict

def detect_objects(path_to_image: str) -> List[Dict]:
    """ """
    
    p = subprocess.Popen([
        ".\\describe\\processing\\objects\\tf2-10\Scripts\python.exe", 
        ".\\describe\\processing\\objects\\yolov3-tf2\\detect.py",
        "--image",
        f"{path_to_image}"],
        shell=True, 
        stdout=subprocess.PIPE)

    # Wait for subprocess to finish
    p_status = p.wait()
    out, err = p.communicate()
    out = str(out)[2:]
    
    try:
        return [{name: float(score[:-1])} for name, score in [obj.split(':') for obj in out.split(',')]]
    except Exception as e:
        print(e)
        return list()