# Fix event loop issue in Jupyter Notebook
nest_asyncio.apply()

# Function to get a random API key
def get_random_api_key():
    return random.choice(API_KEYS)

# Function to connect to Web3 using a random API key
def get_web3():
    api_key = get_random_api_key()
    provider_url = f"https://eth-mainnet.alchemyapi.io/v2/{api_key}"
    return Web3(Web3.HTTPProvider(provider_url))

# Define block range
START_BLOCK = 8000000  # Number of the block at desired timeline
END_BLOCK = get_web3().eth.block_number  # Latest block number
BLOCK_STEP = 100000 # Number of block to process for one call

# Estimate total batches
total_batches = (END_BLOCK - START_BLOCK) // BLOCK_STEP

# Function to fetch transactions **without async/await**
def fetch_block_transactions(block_number):
    web3 = get_web3()  # Get a new Web3 connection with a random key
    try:
        block = web3.eth.get_block(block_number, full_transactions=True)
        transactions = [
            {
                "timestamp": block.timestamp,
                "from": tx["from"],
                "to": tx["to"],
                "value": tx["value"] / 10**18,  # Convert Wei to ETH
                "gas_price": tx["gasPrice"] / 10**9,  # Convert Wei to Gwei
                "hash": tx["hash"].hex()
            }
            for tx in block.transactions
        ]
        return transactions
    except Exception as e:
        print(f"Error fetching block {block_number}: {e}")
        return []

# Main function to fetch all transactions (running in parallel batches)
def fetch_all_transactions():
    block_count = 0
    all_transactions = []
    with tqdm(total=total_batches, desc="Fetching Blocks", unit="batch") as pbar:
        for block in range(START_BLOCK, END_BLOCK, BLOCK_STEP):
            block_count += 1
            txs = fetch_block_transactions(block)
            all_transactions.extend(txs)
            pbar.update(1)  # Update progress bar

            # Avoid rate limit by sleeping for a short duration
            time.sleep(0.5)

    
    return all_transactions
