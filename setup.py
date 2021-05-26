from setuptools import setup, find_packages
import pyunity_tools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyunity-tools",
    version=pyunity_tools.__version__,
    author="Ray Chen",
    author_email="tankimarshal2@gmail.com",
    description="Tools to help with PyUnity development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github/pyunity/pyunity-tools",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        "argparse",
        "pyqt5"
    ],
    entry_points={
        "console_scripts": [
            "pyunity-tools=pyunity_tools.cli:main"
        ]
    }
)
