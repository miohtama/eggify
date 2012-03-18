#!/usr/bin/env python
"""

"""

import sys
import shutil
import os
import fnmatch

# Replace all these variables
TEMPLATE_NAME="youraddon"

IGNORE_MASKS=["*.pyc", "*.pyo", "*.git*", "*.egg*", "*.EGG*"]

FILES_TO_DELETE=[
    ".git", 
    "README.rst", 
    "Products.youraddon.egg-info", 
]

def process(fname, newname):
    """ """

    # See if we don't want to touch this file
    for mask in IGNORE_MASKS:
        if fnmatch.fnmatch(fname, mask):
            return

    # Do in-place replacement of template strings,
    # all one of them.
    # Because we are workin on a copy, don't be
    # that pick about atomicity
    if not os.path.isdir(fname):

        # Read the source file
        f = open(fname, "rt")
        data = f.read()
        f.close()

        # Replace template variables
        data = data.replace(TEMPLATE_NAME, newname)

        # Clean up all lines between EXAMPLES START and EXAMPLES END section
        new_lines = []
        filtering = False
        for line in data.split("\n"):
            if "EXAMPLES START" in line:
                filtering = True
            
            if not filtering:
                new_lines.append(line)

            if "EXAMPLES END" in line:
                filtering = False

        # Write the output
        data = "\n".join(new_lines)

        f = open(fname, "wt")       
        f.write(data)
        f.close()

    path, file = os.path.split(fname)

    if file == TEMPLATE_NAME:
        # Rename youraddon folders to something else
        newname = os.path.join(path, newname)
        shutil.move(fname, newname)

def post_copy_in(source, target):
	"""
	Copy in Python files from old namespace.
	"""
	shutil.copytree(source, target)

def post_cleanup(target, newname):
    """
    Remove unneeded files.
    """

    for f in FILES_TO_DELETE:
        fname = os.path.join(target, f)
        if os.path.exists(fname):
            if os.path.isdir(fname):
                shutil.rmtree(fname)
            else:
                os.remove(fname)
                
def fancy_replace(source, target):
    """ """

    target = os.path.join(os.getcwd(), "..", newname)
    if os.path.exists(target):
        print "Already exists:" + target
        print "Plese remove first"
        sys.exit(1)

    # Where are our template files
    template = os.getcwd()

    # Create a copy of the skeleton
    shutil.copytree(template, target)

    post_cleanup(target, newname)

    # Replace strings and filenames
    for root, dirs, files in os.walk(target, topdown=False):
        for name in files:
            fname = os.path.join(root, name)
            process(fname, newname)
    
        for name in dirs:
            fname = os.path.join(root, name)
            process(fname, newname)

    module_name = os.path.basename(source)
    post_copy_in(os.path.join(source, "Products"), os.path.join(target, module_name))

    print "Created:" + target

def scan(source, target):
	""" 
	Read source directory and eggify every folder in it.
	"""

	for f in os.listdir(source):
		fname = os.path.join(source, f)
		if os.path.isdir(fname):
			ftarget = os.path.join(target, f)
			fancy_replace(fname, ftarget)

def main():
    """ 
    """

    if len(sys.argv) < 3:
        print "Usage: ./eggify.py [folder with products] [target folder]"
        sys.exit(1)

    scan(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
