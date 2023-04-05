from solcx import compile_standard, install_solc
import json
from web3 import Web3


with open("./Web3.py-Storage-Project/SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
print("installing solc..")
install_solc("0.6.0")

# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)
with open("compiled_sol.json", "w") as file:
    json.dump(compiled_sol, file)
# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 5777
my_address = "0x326B00A7A32A4B45E1FaFb530b11eECD59865a62"
private_key = "0xf4e8d7232914e29ffd629dfcb1765b4ef7720a5149abe9ef4fa633bd3248b651"
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# latest transaction count
nonce = w3.eth.get_transaction_count(my_address)
print(nonce)

transaction = SimpleStorage.constructor().build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
print(transaction)

# transaction = SimpleStorage.constructor().build_transaction(
#     {"chainId": chain_id, "from": my_address, "nonce": nonce}
# )
# print(transaction)
