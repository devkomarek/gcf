
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='google-cloud-functions',  
     packages = ['googlecloudfunctions'],
     version='0.3.5',
     author="Lukasz Szymszon",
     author_email="devkomarek@gmail.com",
     description="GCF utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/devkomarek/google-cloud-functions",
     download_url="https://github.com/devkomarek/google-cloud-functions/releases/tag/0.3.5",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
