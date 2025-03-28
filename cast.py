import subprocess

RPC_URL="" # URL for a hosted blockchain network
TARGET_ADDR="" # The Adress of the blockchain
PRIV_KEY = "" # The private key for your acount on the blockchain

## 
def get_balance(player_addr):
    print(subprocess.check_output(["cast", "balance", "--rpc-url", RPC_URL, player_addr], text=True))

def swap_for_mal(amount):
    print(subprocess.check_output(["cast", "send", TARGET_ADDR, "swapForMAL()", "--value", str(amount)+"ether", "--rpc-url", RPC_URL, "--private-key", PRIV_KEY], text=True))

def get_mal_addr():
    return subprocess.check_output(["cast", "call", TARGET_ADDR, "malakarEssence()", "--rpc-url", RPC_URL], text=True).replace("000000000000000000000000", "").strip()

def get_mal_balance():
    MAL_ADDR = ""
    PLAYER_ADDR = ""
    print(subprocess.check_output(["cast", "call", MAL_ADDR, "balanceOf(address)", PLAYER_ADDR, "--rpc-url", RPC_URL], text=True))

def one_time_refund(amount):
    MAL_ADDR = ""
    print(subprocess.check_output(["cast", "send", TARGET_ADDR, "oneTimeRefund(address,uint256)", MAL_ADDR, str(amount), "--rpc-url", RPC_URL, "--private-key", PRIV_KEY], text=True))

def approve(amount):
    
    print(subprocess.check_output(["cast", "send", MAL_ADDR, "approve(address,uint256)", TARGET_ADDR, str(amount), "--rpc-url", RPC_URL, "--private-key", PRIV_KEY], text=True))

print(subprocess.check_output(["cast"], text=True))