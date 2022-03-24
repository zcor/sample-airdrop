#!/usr/bin/python3

import pytest
from brownie import *


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def token(Token, accounts):
    return Token.deploy("Test Token", "TST", 18, 1e21, {"from": accounts[0]})


@pytest.fixture(scope="module")
def alice():
    return accounts[0]


@pytest.fixture(scope="module")
def bob():
    return accounts[0]


@pytest.fixture(scope="module")
def height():
    return 14444444


@pytest.fixture(scope="module")
def airdrop(token, alice, height):
    minter = Airdrop.deploy(token, height, {"from": alice})
    token.transfer_owner(minter, {"from": alice})
    return minter


@pytest.fixture(scope="module")
def crv_holder():
    return "0x989AEb4d175e16225E39E87d0D97A3360524AD80"
