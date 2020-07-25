from io import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'LICENSE.txt'), encoding='utf-8') as f:
    project_license = f.read()

setup(
    name='reoptimization-algorithms',  # Required
    version='0.0.1.rc.1',  # Required
    description='Contains famous Reoptimization algorithms',  # Optional

    long_description=long_description,  # Optional

    long_description_content_type='text/x-rst',  # Optional (see note above)

    license="MIT License",

    url='https://github.com/mek97/reoptimization-algorithms',  # Optional

    author='Mehul Kumar',  # Optional

    author_email='mehul.k1997@gmail.com',  # Optional

    classifiers=[  # Optional
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords=' Reoptimization Approximation Algorithms Path vertex cover',  # Optional

    package_dir={'': 'src'},  # Optional

    packages=find_packages(where='src', exclude=['tests*', 'docs*', 'docsrc*', 'images*']),  # Required

    python_requires='>=3.6',

    install_requires=[],  # Optional

    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={  # Optional
    },

    data_files=[],  # Optional

    entry_points={
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/mek97/reoptimization-algorithms/issues',
        'Source': 'https://github.com/mek97/reoptimization-algorithms',
    },
)
