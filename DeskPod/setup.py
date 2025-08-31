from setuptools import setup, find_packages

setup(
    name='DeskPod',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project to manage multiple desktop environments on Ubuntu using containerization.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/DeskPod',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyGTK',
        'lxc',
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)