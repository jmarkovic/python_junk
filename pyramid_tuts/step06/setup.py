__author__ = 'josip'

from setuptools import setup

requires = ["pyramid_chameleon", "pyramid"]

setup(name="tutorial",
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,)
