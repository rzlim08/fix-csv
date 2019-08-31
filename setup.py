from setuptools import setup

setup(
    name="FixCsv",
    version="0.0.1",
    packages=["fix_csv"],
    entry_points={"console_scripts": ["fix_csv = fix_csv.__main__:main"]},
)
