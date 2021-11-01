# ==================================================================================
#  This SW is developed as part of ITU-5G-AI/ML challenge
#  ITU-ML5G-PS-014: Build-a-thon(PoC) Network resource allocation
#  for emergency management based on closed loop analysis
#  Team : RAN-RIC-xApp
#  Author : Deena Mukundan
#  Description : This file has the main implementation of predictor xApp
# ==================================================================================

from setuptools import setup, find_packages

setup(
    name="alloc",
    version="0.0.2",
    packages=find_packages(exclude=["tests.*", "tests"]),
    description="Anomaly Detection xApp that integrates with Traffic Steering",
    url="https://gerrit.o-ran-sc.org/r/admin/repos/ric-app/alloc",
    install_requires=["ricxappframe>=1.1.1,<2.4.0", "pandas>=1.1.3", "joblib>=0.3.2", "Scikit-learn>=0.21", "schedule>=0.0.0"],
    entry_points={"console_scripts": ["run-alloc.py=alloc.main:start"]},  # adds a magical entrypoint for Docker
)
