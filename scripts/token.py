#!/usr/bin/python3

from brownie import Airdrop, Token, accounts


def main():
    token = Token.deploy("Test Token", "TST", 18, 0, {"from": accounts[0]})
    minter = Airdrop.deploy(token, {"from": accounts[0]})
    token.transfer_owner(minter, {"from": accounts[0]})
    return minter
