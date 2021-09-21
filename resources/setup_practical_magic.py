__required_version__ = 2020.1

# check if we need to install / update 

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import os.path
if os.path.isdir("setup_practical_magic"):
    from setup_practical_magic import __version__
else:
    __version__ = 2019.1
if __version__<__required_version__ or True:
    print('Loading ... ')
    import urllib.request
    content = urllib.request.urlopen ("http://DiscreteMathematics-202122.github.io/live/resources/setup_practical_magic.zip")
    import zipfile
    from io import BytesIO
    data = zipfile.ZipFile(BytesIO(content.read()))
    data.extractall(".")
    
# now import magicx  
from setup_practical_magic import *


