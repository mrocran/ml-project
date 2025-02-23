from setuptools import find_packages, setup
from typing import List

#HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    Returns the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
    #    requirements = [req.strip() for req in file_obj.readlines()]
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("-e")]
    return requirements
        
        #if HYPHEN_E_DOT in requirements:
        #    requirements.remove(HYPHEN_E_DOT)
        
    #return requirements

setup(
    name="ml-project",
    version = "0.0.1",
    author="Ocran",
    author_email="mrocran1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    
)