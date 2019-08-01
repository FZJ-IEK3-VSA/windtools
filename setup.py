from setuptools import setup, find_packages

setup(
    name='windtools',
    version='0.0.1',
    author='D. Severin Ryberg',
    url='https://github.com/FZJ-IEK3-VSA/windtools',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        "numpy",
    ]
)
