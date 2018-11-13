from setuptools import setup, find_packages


setup(name='tibc',
      version='0.0.1',
      install_requires=[
          'nose'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      )