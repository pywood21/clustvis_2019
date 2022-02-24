import numpy as np
from PIL import Image
import os

def load_files(imgdir, enzyme_type, xs, ys): 
    x_image = []
    x_label = []
    fl_all=os.listdir(imgdir)
    target_enzyme = [fl for fl in fl_all if enzyme_type in fl]
    fluor = sorted([fl for fl in target_enzyme if 'fl' in fl])
    for flname in fluor:
        fl_t = flname.split('.')
        durations = fl_t[0].split('_')
        duration = int(durations[2])
        img = Image.open(os.path.join(imgdir,flname))
        img = img.resize((xs, ys))
        img = np.array(img.convert('L'))
        x_image.append(img.flatten().astype(np.float32)/255.0)
        x_label.append (duration)
    fluor_image = np.asarray(x_image)
    fluor_label = np.asarray(x_label)
    
    bright = sorted([fl for fl in target_enzyme if 'br' in fl])
    for flname in bright:
        br_t = flname.split('.')
        durations = br_t[0].split('_')
        duration = int(durations[2])
        img = Image.open(os.path.join(imgdir,flname))
        img = img.resize((xs, ys))
        img = np.array(img.convert('L'))
        x_image.append(img.flatten().astype(np.float32)/255.0)
        x_label.append (duration)
    bf_image = np.asarray(x_image)
    bf_label = np.asarray(x_label)
                         
    return fluor_image, fluor_label, bf_image, bf_label
