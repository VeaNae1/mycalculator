import setuptools

setuptools.setup (
  include_package_data = True,
  name='mycalc0001',
  verson='0.0.1',
  description='oss-dev my calculator 0001',
  author='VeaNae',
  author_email='jess106@naver.com',
  url="https://github.com/VeaNae1/mycalculator.git"
  download_url="https://github.com/VeaNae1/mycalculator/archive/refs/tags/v.0.0.1-alpha.zip",
  install_requires=['pytest'],
  long_description='oss-dev calculator python module',
  long_description_content_type='test/markdown',
  classifiers=[
      "Programming Language :: python :: 3",
      "Operating System :: OS Independent",
  ],
)
