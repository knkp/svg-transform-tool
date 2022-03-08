from pathlib import Path
from io import BytesIO
import numpy as np
from PIL import Image
from cairosvg import svg2png
import cv2
import argparse, os
from transforms import transforms

parser = argparse.ArgumentParser()
parser.add_argument('--path', help= 'paste path to biog.txt file')
args = parser.parse_args()


svgdir = Path(args.path) # to change directory to argument passed for '--path'
outputdir = Path(os.getcwd() + '/output')
# make sure output dir exists
if outputdir.exists() == False:
     outputdir.mkdir()

for svg in svgdir.iterdir():
    if svg.is_dir():
        pass
    else:
        png = svg2png(bytestring=svg.read_bytes())
        pil_img = Image.open(BytesIO(png)).convert('RGBA')
        #pil_img.save(outputdir.stem + '/' + svg.name.split('.')[0] +'-pil.png')
        cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGBA2BGRA)
        transformer = transforms()
        manipulated_img = transformer.filterHologram(cv_img)
        cv2.imwrite(outputdir.stem + '/' + svg.name.split('.')[0] + '.png', manipulated_img)
