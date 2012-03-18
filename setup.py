"""

    Declare a Python package youraddon

    See 

    * http://wiki.python.org/moin/Distutils/Tutorial

    * http://packages.python.org/distribute/setuptools.html#developer-s-

    * http://plone.org/products/plone/roadmap/247

"""

from distutils.core import setup

setup(name = "Products.youraddon",
    version = "0.0",
    description = "",
    author = "",
    author_email = "",
    url = "",
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
    packages = ['youraddon'],
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],     
    license="GPL2",
    include_package_data = True,   
    zip_safe=False        
) 