from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract
from brownie import AdvancedCollectible, network, config, Contract
from scripts.helpful_json import simple_collection_abi


def deploy_and_create():

    account = get_account()

    simple_collection_contract = Contract.from_abi(
        "SimpleCollectible",
        "0x5f2Ab9986b73C6A29635AAAE7162064755e6Bd85",
        simple_collection_abi,
    )
    print(
        simple_collection_contract.balanceOf(
            "0x1d95133783354988C8804465D23dA8656dF51a66"
        )
    )

    print(simple_collection_contract.tokenURI(0))


def main():
    deploy_and_create()
