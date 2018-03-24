from setuptools import setup

setup(name='convention-appearance-finder',
      version='0.0.2',
      description='Tool to find appearances of creators and celebs at conventions',
	  entry_points = {'console_scripts': ['caf=convention-appearance-finder.command_line:main']},
      url='https://github.com/rrrxr6/convention-appearance-finder',
      author='Ryan Roach',
      author_email='rrrxr6@gmail.com',
      license='MIT',
      packages=['convention-appearance-finder'],
	  python_requires='>=3',
      zip_safe=False)
	  