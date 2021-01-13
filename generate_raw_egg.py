from setuptools import setup, find_packages

setup(name='RawData',
      version='0.0.5',
      description='Ingesting Raw Data',
      author='DataLake',
      author_email='HQ-Dist-GTI-DataLake-DG@gap.com',
      packages=find_packages(exclude=['*enrichment*','*flattening*']),
      zip_safe=False)