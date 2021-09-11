from setuptools import setup, find_packages

setup(
    name="py-recycle",
    version="1.2.22",
    description=("Recycle for linux"),
    long_description=open("README.rst").read(),
    author="twfb",
    author_email="twfb@hotmail.com",
    maintainer="twfb",
    maintainer_email="twfb@hotmail.com",
    license="BSD License",
    packages=find_packages(),
    platforms=["all"],
    include_package_data=True,
    url="https://github.com/twfb/recycle",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],
    entry_points={
        "console_scripts": [
            "del=recycle.move_to_trash:main",
            "undel=recycle.recover_from_trash:main",
            "tt=recycle.trash_tree:main",
            "recycle_init=recycle.init_env:main",
            "pdel=recycle.permanently_delete:main",
        ],
    },
),
