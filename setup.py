from pathlib import Path

from setuptools import find_packages, setup

test_requires = ["pytest"]

setup(
    name="Ordered-set-37",
    version="1.0b2",
    url="https://github.com/bustawin/ordered-set-37",
    project_urls={
        "Documentation": "https://github.com/bustawin/ordered-set-37",
        "Code": "https://github.com/bustawin/ordered-set-37",
        "Issue tracker": "https://github.com/bustawin/ordered-set-37/issues/",
    },
    license="Unlicense",
    author="Xavier Bustamante",
    author_email="xavier@bustawin.com",
    description="Dead simple & fast ordered set using python's 3.7+ dict.",
    packages=find_packages(),
    python_requires=">=3.7",
    long_description=Path("README.rst").read_text("utf8"),
    extras_require={"test": test_requires},
    tests_require=test_requires,
    setup_requires=["pytest-runner"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
