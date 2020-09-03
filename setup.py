import io

from setuptools import find_packages
from setuptools import setup

setup(
    name="Queens",
    version="1.0.0",
    license="BSD",
    maintainer="eocode",
    maintainer_email="hola@eliasojedamedina.com",
    description="The eight queens project.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
