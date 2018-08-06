"""
OpenSCAP gatherer.

This library is meant to read a config file, download a policy if needed,
run OpenSCAP (shelling out), gather the report and upload it to some
destination.
"""
version = "0.0.1.dev1"
# version_info is a four-tuple for programmatic comparison. The first
# three numbers are the components of the version number.  The fourth
# is zero for an official release, positive for a development branch,
# or negative for a release candidate or beta (after the base version
# number has been incremented)
version_info = (0, 0, 1, -100)
