from setuptools import setup, find_packages

setup(
    name='SystemInfo',
    packages=find_packages(),
    version='1.0',
    author='Kiryl Kaminski',
    author_email='Kiryl_Kaminski@epam.com',
    description='Gets common system information '
                ' and writes to the json or txt file',
    license="MIT",
    install_requires=[
        'psutil'
    ],
    include_package_data=True
)
