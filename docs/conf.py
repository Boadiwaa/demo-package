import sys
import os

sys.path.insert(0, os.path.abspath(os.sep.join((os.curdir, '..'))))
project = 'acsefunctions'
copyright = '2024, Paulina Boadiwaa Mensah'
author = 'Paulina Boadiwaa Mensah'
release = '0.10'
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.mathjax']
source_suffix = '.rst'
master_doc = 'index'
autoclass_content = "both"
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
