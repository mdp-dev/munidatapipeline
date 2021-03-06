#!/usr/bin/env python

from setuptools import setup

setup(name='munidatapipeline',
      version='00.02.2',
      description='An ETL tool for working with municipal open data (especially GiS data) on resource constrained systems.',
      author='Charles Landau, Andrew Gobbi',
      author_email='munidatapipelinedevelopment@gmail.com',
      url='https://github.com/mdp-dev/munidatapipeline',
      keywords=['munidatapipeline', 'ETL', 'multiprocessing'],
      packages=['munidatapipeline', 'core'],
     )
