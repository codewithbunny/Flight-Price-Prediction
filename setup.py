from setuptools import find_packages, setup
from typing import List

HYPEN_E = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the liast of requirements
    '''
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.replace('\n','') for r in req]

        if HYPEN_E in req:
            req.remove(HYPEN_E)
    return req

setup(

    name = 'mlproject',
    version= '0.0.1',
    author= 'Bunny',
    author_email= 'bashirjaliyawala@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)