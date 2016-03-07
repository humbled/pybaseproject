import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import glob
def findfiles(pattern, base='.', strip_leading_dirs=0):
    matches = []
    for root,_,_ in os.walk(base):
        matches.extend(glob.glob(os.path.join(root, pattern)))
    return [x.split('/',strip_leading_dirs)[strip_leading_dirs] for x in matches]

# same as requrements.txt
install_requires = [
                    'requests==2.9.1',
                   ]


setup(name='pybaseproj',
      version='0.1',
      install_requires = install_requires,
#       tests_require = tests_require,
#       extras_require={'test': tests_require,},
      scripts = ['setup.py'],
      # non-buildout kickoff as per glyph
      entry_points = {'console_scripts':
                      ['launch = pybaseproj.calculator']}
      )
