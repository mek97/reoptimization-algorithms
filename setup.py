from io import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='repotimization-algorithms',  # Required
    version='0.0.1',  # Required
    description='Contains famous Reoptimization algorithms',  # Optional

    long_description=long_description,  # Optional

    long_description_content_type='text/x-rst',  # Optional (see note above)

    url='https://github.com/mek97/repotimization-algorithms',  # Optional

    author='Mehul Kumar',  # Optional

    author_email='mehul.k1997@gmail.com',  # Optional

    classifiers=[  # Optional
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords=' Reoptimization Approximation Algorithms Path vertex cover',  # Optional

    package_dir={'': 'src'},  # Optional

    packages=find_packages(where='src'),  # Required

    python_requires='>=3.5',

    install_requires=['pandas', 'scipy', 'numpy'],  # Optional

    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={  # Optional
        'repotimization-algorithms': ['package_data.dat'],
    },

    data_files=[],  # Optional

    entry_points={
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/mek97/repotimization-algorithms/issues',
        'Source': 'https://github.com/mek97/repotimization-algorithms',
    },
)
