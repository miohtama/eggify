"""

"""

from setuptools import setup, find_packages

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
    namespace_packages=['Products'],    
    packages=find_packages(exclude=['ez_setup']),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Framework :: Zope2",        
    ],     
    license="GPL2",
    include_package_data = True,   
    zip_safe=False        
) 