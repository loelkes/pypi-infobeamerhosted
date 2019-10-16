import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='infobeamerhosted',
    version='1.0',
    author='Christian Lölkes',
    author_email='christian.loelkes@gmail.com',
    description='Python wrapper around the Info Beamer Hosted API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zkmkarlsruhe/pypi-infobeamerhosted',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
    install_requires=[
          'requests',
      ],
)
