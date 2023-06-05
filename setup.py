from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='lsdo_acoustics',
    version='0.0.0',
    author='Luca Scotzniovsky',
    author_email='lscotzni@ucsd.edu',
    license='MIT',
    keywords='aircraft acoustics',
    url='https://github.com/LSDOlab/lsdo_acoustics',
    # download_url='http://pypi.python.org/pypi/lsdo_project_template',
    description='A repository for modeling rotorcraft noise',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.7',
    platforms=['any'],
    install_requires=[
        'numpy',
        'pytest',
        'myst-nb',
        'sphinx',
        'sphinx_rtd_theme',
        'sphinx-copybutton',
        'sphinx-autoapi',
        'numpydoc',
        'gitpython',
        # 'sphinxcontrib-collections @ git+https://github.com/anugrahjo/sphinx-collections.git', # 'sphinx-collections',
        'sphinxcontrib-bibtex',
        'setuptools',
        'wheel',
        'twine',
        'csdl'
    ],
)
