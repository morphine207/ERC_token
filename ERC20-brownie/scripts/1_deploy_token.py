from brownie import BCToken, accounts, config
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000000, "ether")


def main():
    account = accounts.add(config["wallets"]["from_key"])
    bc_token = BCToken.deploy(initial_supply, {"from": account})
    print(bc_token.name())
