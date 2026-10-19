from setuptools import setup, find_packages  # pyright: ignore[reportMissingModuleSource]
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(name='Churn Prediction(Health Insurance)',
      version='0.0.2',
      author='Amit',
      author_email='amitkumars342@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
)
