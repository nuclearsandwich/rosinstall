from setuptools import setup

try:
    import yaml
except:
    raise SystemExit("rosinstall requires python-yaml. Please install python-yaml. On debian systems sudo apt-get install python-yaml.")

import imp

file = None
try:
    file, pathname, description = imp.find_module('__version__', ['src/rosinstall'])
    vermod = imp.load_module('__version__', file, pathname, description)
    version = vermod.version
finally:
    if file is not None:
        file.close()

    
setup(name='rosinstall',
      version= version,
      packages=['rosinstall'],
      package_dir = {'':'src'},
      install_requires = ['vcstools'],
      scripts = ["scripts/rosinstall", "scripts/roslocate", "scripts/rosws", "scripts/rosco"],
      data_files=[('/etc/bash_completion.d', ['contrib/rosws.bash',
                                              'contrib/rosinstall.bash'])], 
      author = "Tully Foote", 
      author_email = "tfoote@willowgarage.com",
      url = "http://www.ros.org/wiki/rosinstall",
      download_url = "http://pr.willowgarage.com/downloads/rosinstall/", 
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python", 
        "License :: OSI Approved :: BSD License" ],
      description = "The installer for ROS", 
      long_description = """\
The installer for ROS
""",
      license = "BSD"
      )
