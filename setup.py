from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="invokust",
    version="1.0a",
    author="Max Williams",
    author_email="futuresharks@gmail.com",
    description="A small wrapper for locust to allow running load tests from within Python or on AWS Lambda",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FutureSharks/invokust",
    download_url="https://github.com/FutureSharks/invokust/archive/1.0a.tar.gz",
    license="MIT",
    scripts=["invokr.py"],
    packages=["invokust",],
    install_requires=["locust>=1.0.3", "pyzmq", "numpy"],
    keywords=["testing", "loadtest", "lambda", "locust"],
    classifiers=[
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Programming Language :: Python :: 3.6",
    ],
)
