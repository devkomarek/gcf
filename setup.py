
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='gcf',  
     version='0.1',
     scripts=['gcf'] ,
     author="Lukasz Szymszon",
     author_email="lukasz.szymszon@gmail.com",
     description="GCF utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/devkomarek/gcf",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
