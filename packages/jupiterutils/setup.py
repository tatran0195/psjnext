from setuptools import setup, find_packages

setup(
    name="jupiterutils",
    version="4.2.0",
    description="Jupiter PSJ Python utilities and class bindings",
    packages=find_packages(),
    package_data={
        "jupiterutils": ["py.typed"],
    },
    python_requires=">=3.8",
    install_requires=[
        "pywin32",
        "psutil",
    ],
)
