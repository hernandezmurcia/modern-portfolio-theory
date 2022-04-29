from setuptools import setup, find_namespace_packages
from crateris.version_crateris import __version__
import pip
from os import path


lib_name = "crateris"
pip_major = int(pip.__version__.split(".")[0])

if pip_major < 10:
    from pip.download import PipSession
    from pip.req import parse_requirements
elif pip_major < 20:
    from pip._internal.download import PipSession
    from pip._internal.req import parse_requirements
else:
    from pip._internal.network.session import PipSession
    from pip._internal.req.req_file import parse_requirements

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

session = PipSession()
process_requirements = parse_requirements("requirements.txt", session=session)

complete_reqs = list(process_requirements)
try:
    requirements = [str(ir.req) for ir in complete_reqs]
except:  # noqa: E722
    requirements = [str(ir.requirement) for ir in complete_reqs]

test_requirements = list(parse_requirements("requirements_dev.txt", session=session))
try:
    test_requirements = [str(ir.req) for ir in test_requirements]
except:  # noqa: E722
    test_requirements = [str(ir.requirement) for ir in test_requirements]

path_location = path.abspath(path.dirname(__file__))

with open(path.join(path_location, 'README.md')) as f:
    readme = f.read()

setup(
    name=lib_name,
    version=__version__,
    author="Rafael Hernandez Murcia",
    author_email="hernandezmurciarafael@gmail.com",
    description=readme,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    tests_require=test_requirements,
    url="https://github.com/hernandezmurcia/modern-portfolio-theory",
    project_urls={
        "Bug Tracker": "https://github.com/hernandezmurcia/modern-portfolio-theory/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(include=['crateris.*']),
    include_package_data=True,
    package_data={  # Include notebook tutorials
        "crateris": ["tutorials/*.ipynb"]
    },
    python_requires=">=3.6",
)