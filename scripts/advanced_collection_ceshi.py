from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract
from brownie import AdvancedCollectible, network, config, Contract
from scripts.helpful_json import advanced_collection_abi


def deploy_and_create():
    account = get_account()

    advanced_collection_contract = Contract.from_abi(
        "AdvancedCollectible",
        "0x1778287887A528AcceBaac6b69C32ECF8EdAC3Ec",  # 0xbA67c6020728AeEcdC45b456076c8559eFa62af0",
        advanced_collection_abi,
    )
    print(
        advanced_collection_contract.balanceOf(
            "0x1d95133783354988C8804465D23dA8656dF51a66"
        )
    )

    print(advanced_collection_contract.tokenURI(0))
    print(advanced_collection_contract.rawFulfillRandomness(0))


def main():
    deploy_and_create()
