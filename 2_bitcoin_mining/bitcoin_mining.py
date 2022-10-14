from hashlib import sha256

MAX_NONCE = 100000000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == "__main__":
    transactions = """
    Dhaval->Bhavin->20,
    Mando->Cara->45
    """
    difficulty = 4  # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time

    start = time.time()
    print("start mining")
    new_hash = mine(
        5,
        transactions,
        "0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7",
        difficulty,
    )
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)
