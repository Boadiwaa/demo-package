from setuptools import setup, find_packages


setup(
    name="ascefunctions",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy>1.2"],
    python_requires='>=3.8',
    description="""
    My Python Package for Calculating Trigonometry
                and Bessel Functions
                """,
    author="Paulina Boadiwaa Mensah",
    license="MIT"
)
