from setuptools import setup, find_packages

# See note below for more information about classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="cog-reloader",
    version="0.0.2",
    description="Make reloading cogs easy while editing. Compitable with `nextcord` and `discord.py`",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shahriyardx/cog-relaoder/",
    author="Md Shahriyar Alam",
    author_email="mdshahriyaralam552@gmail.com",
    license="MIT",
    classifiers=classifiers,
    python_requires='>=3.8.0',
    keywords="discord discord.py nextcord.py nextcord",
    packages=find_packages(),
)
