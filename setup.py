from setuptools import setup, find_packages

setup(
    name = "rpi-gpio-http",
    description = "HTTP interface for Raspberry Pi GPIO",
    version = "1.1.0",
    author = 'Lajos Santa',
    author_email = 'santa.lajos@coldline.hu',
    url = 'https://github.com/voidpp/rpi-gpio-http.git',
    install_requires = [
        "Flask==1.0",
        "querystring-parser==1.2.3",
        "RPi.GPIO==0.6.1",
        "voidpp-tools==1.5.0",
    ],
    include_package_data = True,
    packages = find_packages(),
)
