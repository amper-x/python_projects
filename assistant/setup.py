from setuptools import setup

setup(name='assistant',
      version='1',
      description="Does the assistin'",
      url='not yet',
      author='Maksym Korniev',
      author_email='wmaksym57@gmail.com',
      license='I made it up',
      packages=['assist'],
      entry_points={'console_scripts': ['hello = assistant.assist_2:main',
                                        'Hello = assistant.assist_2:main',
                                        'HELLO = assistant.assist_2:main']}
      )
