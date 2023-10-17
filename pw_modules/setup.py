from setuptools import setup

setup (
    name="pw-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "pw stands for Personal Website. This is based on the started modules kit",
    packages=['pw_config','pw_models'],
    python_requires=">=3.6",
    )