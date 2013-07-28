# Copyright (C) 2010-2013 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

LOCAL_SETTINGS = True
from settings import *

# If you want to customize your cuckoo path set it here.
# CUCKOO_PATH = "/where/cuckoo/is/placed/"

# If you want to customize your cuckoo temporary upload path set it here.
# CUCKOO_FILE_UPLOAD_TEMP_DIR = "/where/web/tmp/is/placed/"

# Maximum upload size.
MAX_UPLOAD_SIZE = 26214400

# Make this unique, and don't share it with anybody.
SECRET_KEY = "z=#dz9%bce-_%l3s!$uldoq^!mb^kl*k%6p%t2ycn#(ug+6#7o"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "America/Chicago"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

ADMINS = (
    # ("Your Name", "your_email@example.com"),
)

MANAGERS = ADMINS

# Allow verbose debug error message in case of application fault.
# It's strongly suggested to set it to False if you are serving the
# web application from a web server front-end (i.e. Apache).
DEBUG = True

# A list of strings representing the host/domain names that this Django site
# can serve.
# Values in this list can be fully qualified names (e.g. 'www.example.com').
# When DEBUG is True or when running tests, host validation is disabled; any
# host will be accepted. Thus it's usually only necessary to set it in production.
ALLOWED_HOSTS = ["*"]