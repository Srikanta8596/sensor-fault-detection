from modulefinder import packagePathMap
from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str]=[]

    """
    Code to read requirements.txt file
    """
    #print("------READING REQUIREMENTS FILE STARTED-----")
    with open('./requirements.txt','r') as file:

        lines = file.readlines()
        for line in lines:
            
            print(line)
            requirement_list.append(line)
    
    print("------READING REQUIREMENTS FILE ENDED-----")
    print('requirement_list------',requirement_list)
        

    return requirement_list[:-1] ## -1 Because we are taking input -e . in requirement file.


setup (
    name='sensor',
    version="0.0.1",
    author="Srikanta Biswal",
    author_email="srikantabiswal8093@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),#[],
)