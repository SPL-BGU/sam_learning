from distutils.core import setup

from setuptools import find_packages

setup(
    name="sam-learning",
    python_requires=">=3.8",
    description="Safe Action Model learning algorithms",
    author="SPL-BGU",
    # Only the packages meant to be imported by consumers.
    #
    # This is an include-list rather than find_packages(exclude=["tests"]) because the
    # repository root also holds `statistics/`, which shadows the Python standard library
    # module of the same name. Installing it would break `import statistics` for every
    # downstream project and for any library that relies on it. Nothing under
    # `sam_learning/` imports it, so leaving it out costs nothing and avoids the collision
    # without renaming anything.
    #
    # `solvers` is included because sam_learning.core.online_learning imports it.
    packages=find_packages(include=["sam_learning*", "utilities*", "solvers*"]),
)
