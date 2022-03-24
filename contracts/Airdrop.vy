# @version ^0.3.1

"""
@title Bare-bones Curve Airdrop
@notice Based on the ERC-20 token standard as defined at
        https://eips.ethereum.org/EIPS/eip-20
"""

import Token as Token

interface veCRV:
   def balanceOfAt(addr: address, _block: uint256) -> uint256: view


vecrv: public(veCRV)
height: public(uint256)
token: public(Token)
owner: address

claimed: HashMap[address, bool] 

@external
def __init__(token_addr: address, height: uint256):
    """
    @notice Initialize a token airdrop for Curve holders
    @dev Deploy with an ERC-20 where this contract has unrestricted mint access and airdrop height
    """
    self.vecrv = veCRV(0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2)
    self.height = height
    self.token = Token(token_addr)
    self.owner = msg.sender


@external
def mint():
    """
    @notice Mint if veCRV Holder
    """

    assert self.claimed[msg.sender] == False, "Already Claimed"

    quantity: uint256 = self.vecrv.balanceOfAt(msg.sender, self.height)
    assert quantity > 0, "Ineligible"

    self.claimed[msg.sender] = True
    self.token.mint(msg.sender, quantity)


@external
def transfer_owner(new_addr: address):
    assert self.owner == msg.sender
    self.owner = new_addr


@external
def transfer_token_owner(new_addr: address):
    assert self.owner == msg.sender
    self.token.transfer_owner(new_addr)
