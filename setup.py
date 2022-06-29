from distutils.core import setup


import os

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + "/requirements.txt"
install_requires = (
    []
)  # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()
setup(
    name="regextractor",
    version="1.0",
    description="Python regex extractor (list of strings => Regex)",
    author="Iulius Curt",
    packages=["regextractor"],
    provides=["regextractor"],
    install_requires=install_requires,
)
