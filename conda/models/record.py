# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from logging import getLogger

from .._vendor.auxlib.entity import (BooleanField, ComposableField, DictSafeMixin, Entity,
                                     EnumField, IntegerField, ListField, StringField)
from ..base.constants import Arch, Platform
from ..common.compat import string_types

log = getLogger(__name__)


# install.create_meta()
# install.load_linked_data()
# install.linked_data_


# {
#   "arch": "x86_64",
#   "build": "py34_0",
#   "build_number": 0,
#   "channel": "https://repo.continuum.io/pkgs/free/osx-64/",
#   "date": "2016-03-17",
#   "depends": [
#     "python 3.4*",
#     "setuptools",
#     "wheel"
#   ],
#   "files": [
#     "bin/pip",
#     "lib/python3.4/site-packages/pip/wheel.py"
#   ],
#   "license": "MIT",
#   "link": {
#     "source": "/Users/kfranz/.conda/pkgs/pip-8.1.1-py34_0",
#     "type": "hard-link"
#   },
#   "md5": "9570a2a81df3ee9e589954ba652021ab",
#   "name": "pip",
#   "platform": "osx",
#   "requires": [],
#   "size": 1633721,
#   "subdir": "osx-64",
#   "url": "https://repo.continuum.io/pkgs/free/osx-64/pip-8.1.1-py34_0.tar.bz2",
#   "version": "8.1.1"
# }


# {
#     "abstract-rendering-0.5.1-np110py34_0.tar.bz2": {
#         "build": "np110py34_0",
#         "build_number": 0,
#         "date": "2015-10-07",
#         "depends": [
#             "numpy 1.10*",
#             "python 3.4*"
#         ],
#         "license": "3-clause BSD",
#         "license_family": "BSD",
#         "md5": "e541b1ceb9cdb57c6b4e0252f89a8179",
#         "name": "abstract-rendering",
#         "requires": [],
#         "size": 73076,
#         "version": "0.5.1"
#     },
#     "click-6.3-py35_0.tar.bz2": {
#         "build": "py35_0",
#         "build_number": 0,
#         "date": "2016-02-23",
#         "depends": [
#             "python 3.5*"
#         ],
#         "license": "BSD",
#         "md5": "6565a48e21d5b492e8284ba6d3d46c3a",
#         "name": "click",
#         "requires": [],
#         "size": 102493,
#         "version": "6.3"
#     },
#     "requests-futures-0.9.4-py27_1.tar.bz2": {
#         "build_number": 1,
#         "name": "requests-futures",
#         "license": "Apache 2.0",
#         "has_prefix": false,
#         "requires": [],
#         "machine": "x86_64",
#         "platform": "linux",
#         "depends": [
#             "futures >=2.1.3",
#             "python 2.7*",
#             "requests >=1.2.0"
#         ],
#         "version": "0.9.4",
#         "build": "py27_1",
#         "md5": "a998ae57a7d9c5efe81cca4c45c7e5d2",
#         "binstar": {
#             "package_id": "57b45754fe7dbe34b82e796b",
#             "channel": "main",
#             "owner_id": "5528f42ce1dad12974506e8d"
#         },
#         "size": 5482,
#         "arch": "x86_64",
#         "operatingsystem": "linux",
#         "target-triplet": "x86_64-any-linux",
#         "subdir": "linux-64"
#     },
#     "scikit-learn-0.17.1-np110py35_blas_openblas_202.tar.bz2": {
#         "build_number": 202,
#         "features": "blas_openblas",
#         "license": "BSD 3-Clause",
#         "has_prefix": true,
#         "requires": [],
#         "name": "scikit-learn",
#         "machine": "x86_64",
#         "platform": "linux",
#         "depends": [
#             "blas 1.1 openblas",
#             "numpy 1.10*",
#             "openblas 0.2.18|0.2.18.*",
#             "python 3.5*",
#             "scipy"
#         ],
#         "version": "0.17.1",
#         "build": "np110py35_blas_openblas_202",
#         "md5": "4b9cd73864c899a9401f8894262fb09f",
#         "binstar": {
#             "package_id": "574118e308df864266f8d17d",
#             "channel": "main",
#             "owner_id": "5528f42ce1dad12974506e8d"
#         },
#         "size": 9513637,
#         "arch": "x86_64",
#         "operatingsystem": "linux",
#         "target-triplet": "x86_64-any-linux",
#         "subdir": "linux-64"
#     },
# }

# info['fn'] = fn
# info['schannel'] = url_s
# info['channel'] = channel
# info['priority'] = priority
# info['url'] = channel + '/' + fn
# key = url_s + '::' + fn if url_s != 'defaults' else fn
# index[key] = info


class Link(DictSafeMixin, Entity):
    source = StringField()
    type = StringField()


# class LinkedPackageData(DictSafeMixin, Entity):
#     arch = EnumField(Arch, nullable=True)
#     build = StringField()
#     build_number = IntegerField()
#     channel = StringField(required=False)
#     date = StringField(required=False)
#     depends = ListField(string_types)
#     files = ListField(string_types, required=False)
#     license = StringField(required=False)
#     link = ComposableField(Link, required=False)
#     md5 = StringField(required=False, nullable=True)
#     name = StringField()
#     platform = EnumField(Platform)
#     requires = ListField(string_types, required=False)
#     size = IntegerField(required=False)
#     subdir = StringField(required=False)
#     url = StringField(required=False)
#     version = StringField()


class Record(DictSafeMixin, Entity):
    arch = EnumField(Arch, required=False, nullable=True)
    build = StringField()
    build_number = IntegerField()
    date = StringField(required=False)
    depends = ListField(string_types)
    features = StringField(required=False)
    has_prefix = BooleanField(required=False)
    license = StringField(required=False)
    license_family = StringField(required=False)
    md5 = StringField(required=False, nullable=True)
    name = StringField()
    platform = EnumField(Platform, required=False, nullable=True)
    requires = ListField(string_types, required=False)
    size = IntegerField(required=False)
    subdir = StringField(required=False)
    track_features = StringField(required=False)
    version = StringField()

    fn = StringField(required=False)
    schannel = StringField(required=False, nullable=True)
    channel = StringField(required=False, nullable=True)
    priority = IntegerField(required=False)
    url = StringField(required=False, nullable=True)

    files = ListField(string_types, required=False)
    link = ComposableField(Link, required=False)
