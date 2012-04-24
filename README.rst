A simple script to eggify old-style Plone add-ons from Products namespace.

Example to eggify multiple products::

	./eggify.py ../your-products ../your-eggs


Manual migrations
------------------

You need to add the following to ``configure.zcml``::

	  <five:registerPackage package="." initialize=".initialize" />
