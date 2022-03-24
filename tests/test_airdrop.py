#!/usr/bin/python3

import brownie
import pytest


def test_mint_increases_value(airdrop, token, crv_holder):
    init_bal = token.balanceOf(crv_holder)
    airdrop.mint({"from": crv_holder})
    assert token.balanceOf(crv_holder) > init_bal


def test_cannot_remint(airdrop, token, crv_holder):
    airdrop.mint({"from": crv_holder})
    with brownie.reverts("Already Claimed"):
        airdrop.mint({"from": crv_holder})


def test_non_crv_holder_cannot_mint(airdrop, token, bob):
    with brownie.reverts("Ineligible"):
        airdrop.mint({"from": bob})
