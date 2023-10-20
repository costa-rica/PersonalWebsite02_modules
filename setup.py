from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup (
    name="pw-modules",
    version="0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description="pw stands for Personal Website. This is based on the started modules kit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/costa-rica/PersonalWebsite02_modules",
    packages=['pw_config', 'pw_models'],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
