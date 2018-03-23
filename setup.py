from setuptools import setup

setup(name='convention_appearance_finder',
      version='0.0.1',
      description='Tool to find appearances of creators and celebs at conventions',
	  entry_points = {'console_scripts': ['caf=convention_appearance_finder.command_line:main']},
      url='https://github.com/rrrxr6/convention_appearance_finder',
      author='Ryan Roach',
      author_email='rrrxr6@gmail.com',
      license='MIT',
      packages=['convention_appearance_finder'],
	  python_requires='>=3',
      zip_safe=False)