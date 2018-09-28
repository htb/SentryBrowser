import setuptools


requires = [

]

setuptools.setup(
  name         = 'sentry_browser',
  version      = '0.0.1',
  author       = 'Hans Terje Bakke',
  author_email = 'hans.terje.bakke@gmail.com',
  description  = 'For simple browsing of issues, events and special breadcrumbs from sentry.io.',
  url          = "TODO::GITHUB",
  classifiers  = [
    'Programming Language :: Python :: 2.7',
    'Operating System :: OS Independent'
  ],

  scripts      = ['bin/sentry'],

  install_requires = requires,
  packages = setuptools.find_packages()
)