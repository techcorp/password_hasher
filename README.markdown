# Password Hasher

**Password Hasher** is a CPU-based password hash auditing tool designed for ethical security testing. It computes hashes (MD5, SHA1, or SHA256) for a list of passwords from a wordlist and compares them against a provided list of target hashes to identify matches. This tool is intended for authorized password strength audits, helping security professionals detect weak passwords in systems they have permission to test.

**Created by**: Technical Corp

**License**: MIT License

---

## Features

- **Hash Algorithms**: Supports MD5, SHA1, and SHA256 hashing.
- **Efficient Comparison**: Matches computed hashes against target hashes to find corresponding passwords.
- **Command-Line Interface**: Easy-to-use arguments for specifying wordlist, hashes, and algorithm.
- **Lightweight**: No external dependencies beyond Python's standard library (`hashlib`).
- **Ethical Use**: Built for legal security audits with explicit permission (e.g., penetration testing, password policy enforcement).

**Use Cases**:
- Auditing weak passwords in authorized systems.
- Educational purposes for learning about hashing and password security.
- Testing password strength against common wordlists.

**Warning**: Unauthorized use of this tool to crack passwords or access systems without permission is illegal and unethical. Always obtain explicit consent from system owners before use.

---

## Installation

### Prerequisites
- **Operating System**: Linux (e.g., Kali, Ubuntu), Windows, or macOS.
- **Python**: Version 3.6 or higher.
- **Hardware**: Any CPU (no GPU required).
- **Permissions**: Ensure you have legal authorization to audit the target hashes.

### Step 1: Install Python
- **Linux (e.g., Kali/Ubuntu)**:
  ```bash
  sudo apt update
  sudo apt install -y python3
  ```
- **Windows/macOS**: Download and install from [python.org](https://www.python.org/downloads/).
- Verify:
  ```bash
  python3 --version
  ```
  Expected: `Python 3.x.x` (e.g., 3.11.5).

### Step 2: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/<your-username>/password-hasher.git
cd password-hasher
```

### Step 3: Verify Files
Ensure the following files are present:
- `password_hasher.py`: The main script.
- `wordlist.txt`: A sample wordlist with passwords.
- `hashes.txt`: A sample list of target hashes.

If not present, create sample files (see [Usage](#usage) for examples).

### Step 4: Check Python Dependencies
The tool uses Python's built-in `hashlib` module, so no external libraries are needed. Confirm:
```bash
python3 -c "import hashlib"
```
If no errors, you're ready.

---

## Usage

### Command Syntax
```bash
python3 password_hasher.py --wordlist <wordlist_file> --hashes <hashes_file> --algorithm <algorithm>
```

- `--wordlist`: Path to a text file containing passwords (one per line).
- `--hashes`: Path to a text file containing target hashes (one per line).
- `--algorithm`: Hash algorithm (`md5`, `sha1`, or `sha256`). Default: `sha256`.

### Example Files
- **wordlist.txt** (example content):
  ```
  password
  admin
  test123
  qwerty
  letmein
  ```
  Create with:
  ```bash
  echo -e "password\nadmin\ntest123\nqwerty\nletmein" > wordlist.txt
  ```

- **hashes.txt** (example SHA256 hashes):
  ```
  5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
  8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
  ```
  Create with:
  ```bash
  echo -e "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8\n8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918" > hashes.txt
  ```

### Running the Tool
Run the tool with the example files:
```bash
python3 password_hasher.py --wordlist wordlist.txt --hashes hashes.txt --algorithm sha256
```

**Example Output**:
```
Loading wordlist from wordlist.txt...
Loaded 5 words.
Loading target hashes from hashes.txt...
Loaded 2 target hashes.
Computing sha256 hashes on CPU...
Hashing completed in 0.01 seconds.
Comparing hashes...
Found matches:
Password: password matches hash: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
Password: admin matches hash: 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
```

### Interpreting Results
- **Matches Found**: Indicates passwords from the wordlist that match target hashes (e.g., weak passwords like "password").
- **No Matches**: Suggests the wordlist doesn’t contain the passwords or hashes use a different algorithm.
- **Action**: Use results to recommend stronger passwords (e.g., 12+ characters, mixed case, numbers, symbols).

---

## Testing

### Sample Test
The provided `wordlist.txt` and `hashes.txt` are small for quick testing. For broader tests:
- **Larger Wordlist**: Use a wordlist like `rockyou.txt` from [SecLists](https://github.com/danielmiessler/SecLists):
  ```bash
  sudo apt install -y seclists
  python3 password_hasher.py --wordlist /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt --hashes hashes.txt --algorithm sha256
  ```
  Note: Large wordlists (e.g., 14M entries) take longer (seconds to minutes).

- **Different Algorithms**:
  ```bash
  echo "5f4dcc3b5aa765d61d8327deb882cf99" > md5_hashes.txt  # MD5 for "password"
  python3 password_hasher.py --wordlist wordlist.txt --hashes md5_hashes.txt --algorithm md5
  ```

### Safe Testing
- Use a virtual machine (e.g., Kali Linux in VirtualBox) or platforms like [TryHackMe](https://tryhackme.com/).
- Never test on systems or hashes without explicit permission.

---

## Troubleshooting

- **File Not Found**:
  ```
  Error: Wordlist file 'wordlist.txt' not found.
  ```
  - Fix: Verify file exists (`ls`) and use correct path:
    ```bash
    python3 password_hasher.py --wordlist ./wordlist.txt --hashes ./hashes.txt --algorithm sha256
    ```

- **No Matches**:
  - Ensure `--algorithm` matches hash type (e.g., `sha256` for provided hashes).
  - Check `hashes.txt` for correct format (hex, no spaces).
  - Use `cat hashes.txt` to verify content.

- **Slow Performance**:
  - Small wordlists (<100 entries) are fast (<0.1s). Large wordlists (e.g., millions) are slower. Split large files:
    ```bash
    split -l 10000 wordlist.txt wordlist_split_
    ```

- **Python Errors**:
  - If `hashlib` fails, reinstall Python:
    ```bash
    sudo apt install --reinstall python3
    ```

---

## Legal and Ethical Use

- **Authorization**: Only use this tool on systems or hashes you own or have explicit permission to audit. Unauthorized use violates laws like the Computer Fraud and Abuse Act (US) or Computer Misuse Act (UK).
- **Purpose**: Use for ethical security testing, such as:
  - Verifying password strength.
  - Educating users about weak passwords.
  - Authorized penetration testing.
- **Data Security**: Securely delete wordlists and hashes after use to prevent misuse:
  ```bash
  rm wordlist.txt hashes.txt
  ```

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to your fork (`git push origin feature-name`).
5. Open a pull request.

Suggestions:
- Add support for salted hashes.
- Implement multithreading for faster hashing.
- Add progress bars for large wordlists.

---

## Contact

For questions or support, contact Technical Corp via:
- **GitHub Issues**: Open an issue in this repository.
- **Email**: technicalcorp700@gmail.com.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Created with ❤️ by Technical Corp*
