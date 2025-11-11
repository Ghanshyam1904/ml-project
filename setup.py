# Reasposible for createing machine learing package
from setuptools import find_packages,setup
from typing import List

HYPE_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements= []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [i.replace('\n','') for i in requirements]

        if HYPE_DOT_E in requirements:
            requirements.remove(HYPE_DOT_E)
        return requirements

setup(
    name='mlproject',
    version='0.0.6',
    author='Ghanshyam',
    author_email='ghanshyampatil2002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)