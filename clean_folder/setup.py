from setuptools import setup

setup(name='clean_folder',
      version='1',
      description="Cleans 'em folders",
      url='not yet',
      author='Maksym Korniev',
      author_email='wmaksym57@gmail.com',
      license='I made it up',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.sort:startup']}
      )
