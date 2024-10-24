# acsefunctions
The `acsefunctions` package consists of 2 modules: `taylors_series` and `bessel_group` consisting of trigonometric functions and the Bessel function
respectively, for use on scalar and numpy array objects. The trigonometric functions were created using Taylors
series. The Bessel function was implemented based on Euler’s definition.

## Installation

- Make sure you have pip installed
- Clone the repository from the URL: https://github.com/ese-ada-lovelace-2024/mpm-assessment-1-esemsc-pbm24.git`
  to your preferred working directory

- Within shell/terminal navigate to the repository directory and use the following command:

```bash
pip install -e .

```
NB: Best practice would be to create a conda environment within the working directory and activate this
before installing the package. For this, you would need to have `conda` pre-installed and then run

```bash
# Create conda environment
conda env create -f environment.yml
# Activate the environment
conda activate acsepackageenvironment
# Install the package
pip install -e .
```
