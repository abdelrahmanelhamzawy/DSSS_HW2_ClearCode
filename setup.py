from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Name of the package
    version="0.1",  # Version number
    packages=find_packages(),  # Automatically find all packages (directories with __init__.py)
    install_requires=[  # List of dependencies, if any
        # 'some_package',  # Uncomment and add any external dependencies you have
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # Make math_quiz script executable
        ],
    },

    test_suite='tests_math_quiz',  # Location of the specific test file
    author="Abdelrahman",  
    author_email="abdelrahmanelhamzawy4@gmail.com",  
    description=" math quiz assignment for version control ",  # A short description of your package
    long_description=open('README.md').read(),  # Read content from README.md for a detailed description
    long_description_content_type='text/markdown',
    url="https://github.com/abdelrahmanelhamzawy/DSSS_HW2_ClearCode.git",  #repo URL
    classifiers=[
        'Programming Language :: Python :: 3',  # This specifies which versions of Python are supported
        'License :: OSI Approved :: MIT License',  #project's license
        'Operating System :: OS Independent',  # Cross-platform
    ],
)
