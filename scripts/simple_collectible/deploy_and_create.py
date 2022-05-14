from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    # def main():    # joel: for test
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    # print(simple_collectible.abi)
    tx = simple_collectible.creatCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)} "
    )
    tx = simple_collectible.creatCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    # joel: wait for 1 block.
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)} "
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")
    simple_collectible.transferFrom(
        account, "0x14B90Dbdb5d63Eea1C1Cb0f2F78C46a628ed6E36", 0
    )

    return simple_collectible  # joel: for test


def main():
    deploy_and_create()


# joel: " brownie run scripts/deploy_and_create.py --network rinkeby"
#  first time: ExtraDataLengthError. second time: OK!
#  Opensea testnet is only compatible with Rinkeby
