import os
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    if os.path.exists(file_path):
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]
    else:
        print(f"⚠️ Warning: '{file_path}' not found. No dependencies will be installed.")
    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='sanjana',
    author_email='sanjanachavan2208@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
