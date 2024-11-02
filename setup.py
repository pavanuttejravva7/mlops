from setuptools import find_packages, setup

def load_requirements(file):

    requirements = []

    with open(file) as file_obj:
        requirements = file_obj.readlines()
        for n in range(len(requirements)):

            requirements[n] = requirements[n].replace('\n', '')
        
            if requirements[n] == '-e .':
                    requirements.remove(requirements[n])
    
    return requirements


setup(
  
  name = 'Pavan',
  version = '0.0.1',
  author ='pvan',
  author_email= 'ravva@udel.edu',
  packages = find_packages(),
  install_requires = load_requirements('C:\Mlops\Requirements.txt'),

 )

