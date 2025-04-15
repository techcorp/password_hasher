import hashlib
import argparse
import time
import sys

# Define supported hash algorithms
HASH_ALGORITHMS = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256
}

def hash_input(input_str, algorithm='sha256'):
    """Compute the hash of an input string using the specified algorithm."""
    if algorithm not in HASH_ALGORITHMS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    hasher = HASH_ALGORITHMS[algorithm]()
    hasher.update(input_str.encode('utf-8'))
    return hasher.hexdigest()

def load_wordlist(file_path):
    """Load passwords from a wordlist file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: Wordlist file '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading wordlist: {e}")
        sys.exit(1)

def hash_wordlist(words, algorithm):
    """Compute hashes for a list of words."""
    hashes = []
    start_time = time.time()
    for word in words:
        h = hash_input(word, algorithm)
        hashes.append(h)
    elapsed = time.time() - start_time
    return hashes, elapsed

def compare_hashes(computed_hashes, target_hashes, words):
    """Compare computed hashes against target hashes."""
    matches = []
    for i, computed_hash in enumerate(computed_hashes):
        for target_hash in target_hashes:
            if computed_hash.lower() == target_hash.lower():
                matches.append((words[i], target_hash))
    return matches

def main():
    parser = argparse.ArgumentParser(description="CPU-based password hash auditor")
    parser.add_argument('--wordlist', required=True, help="Path to wordlist file")
    parser.add_argument('--hashes', required=True, help="Path to file with target hashes")
    parser.add_argument('--algorithm', choices=['md5', 'sha1', 'sha256'], default='sha256',
                        help="Hash algorithm to use")
    args = parser.parse_args()

    print(f"Loading wordlist from {args.wordlist}...")
    words = load_wordlist(args.wordlist)
    print(f"Loaded {len(words)} words.")

    print(f"Loading target hashes from {args.hashes}...")
    try:
        with open(args.hashes, 'r', encoding='utf-8') as f:
            target_hashes = [line.strip() for line in f if line.strip()]
        print(f"Loaded {len(target_hashes)} target hashes.")
    except FileNotFoundError:
        print(f"Error: Hashes file '{args.hashes}' not found.")
        sys.exit(1)

    print(f"Computing {args.algorithm} hashes on CPU...")
    computed_hashes, elapsed = hash_wordlist(words, args.algorithm)
    print(f"Hashing completed in {elapsed:.2f} seconds.")

    print("Comparing hashes...")
    matches = compare_hashes(computed_hashes, target_hashes, words)
    if matches:
        print("\nFound matches:")
        for word, target_hash in matches:
            print(f"Password: {word} matches hash: {target_hash}")
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
