# SVG CLI based Transformation Tool
Simple CLI tool using opencv to run filters on groups of svg images.

I recommend using a python virtual environment to install all required packages:
```
python3 -m venv svg-generator-venv
source svg-generator-venv/bin/activate
```

Once in your environment install the needed packages
```
pip install -r requirements.txt
```

_If on Ubuntu (or compatible)
You can also just run the `setup.sh` and it will run those commands for you._

Now make a directory of svg image files and pass that directory to the main python script
```
python main.py --path=svgs-to-process
```
And see the results in the `outputs/` directory.

Here's an example, the normal svg image is on the _right_ transformed png on the _left_
![image](https://user-images.githubusercontent.com/5614030/157160939-31eade1b-1a97-4260-90c7-c72ad94007b0.png)

# Goals?
In time, I might add some optional filter flags, we already want to have an ascii filter so it might look like this:
```
python main.py --path=svgs-to-process --ascii-filter
```

# Other Stuff

I've licensed this as MIT - so feel free to do whatever you want with it.
I hope someone enjoys it!
