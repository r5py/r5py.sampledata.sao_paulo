#!/usr/bin/env python3

import importlib

import pytest


PACKAGE_NAME = "r5py.sampledata.sao_paulo"


@pytest.fixture
def _module():
    import sys
    print(sys.path)
    _module = importlib.import_module(PACKAGE_NAME)
    yield _module


@pytest.fixture
def data_sets(_module):
    yield [getattr(_module, var) for var in _module.__all__ if var != "__version__"]
