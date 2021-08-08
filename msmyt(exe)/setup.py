from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    ld = readme_file.read() 

setup(
    name="msm_yt_downloader",
    version="1.0.0",
    description="Utiity to download Youtube Videos",
    long_description=ld,
    long_description_content_type="text/markdown",
    author="MandraSaptak Mandal",
    license="MIT",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"
    ],
    keywords="youtube video downloader",
    packages=find_packages(),
    install_requires=["requests>=2"]
)