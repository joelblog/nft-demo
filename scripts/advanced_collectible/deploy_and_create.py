from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import AdvancedCollectible, network, config


def deploy_and_create():
    # def main():    # joel: for test
    # Rinkeby
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {
            "from": account,
            "gas_limit": 3441409,
            "publish_source": True,
        },  # , "gas_limit": 3441409, "allow_revert": True  2441409 publish_source: True
    )

    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible(
        {"from": account}  # , "allow_revert": True
    )
    creating_tx.wait(1)

    print("New token has been created!")

    return (advanced_collectible, creating_tx)  #


def main():
    deploy_and_create()


# joel: " brownie run scripts/deploy_and_create.py --network rinkeby"
#  first time: ExtraDataLengthError. second time: OK!
#  Opensea testnet is only compatible with Rinkeby
