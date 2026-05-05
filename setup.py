from setuptools import find_packages,setup
from typing import List


def get_requirements(filepath:str)-> List[str]:
  requirement_lst:List[str]=[]
  try:
    with open(filepath) as file:
      lines=file.readlines()
      for line in lines:
        requirement=line.strip()
        if requirement and requirement!='-e .':
          requirement_lst.append(requirement)
  except FileNotFoundError:
    print("requirements.txt file not found")
  return requirement_lst


setup(
  name="networksecurity",
  version="0.1",
  author="khushi",
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)

