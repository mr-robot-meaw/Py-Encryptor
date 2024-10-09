# Py-Encryptor

This repository contains a Python script that encrypts passwords using Base64 encoding. 

## Features

- Simple command-line interface
- Encrypts and decrypts passwords using Base64 encoding
- Easy to understand and modify for educational purposes

## Requirements

- Python 3.x
- No external libraries required

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-encryptor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-encryptor
   ```

## Usage

To encrypt a password:
```bash
python encryptor.py --encrypt your_password
```

To decrypt a password:
```bash
python encryptor.py --decrypt encrypted_password
```

## Example

```bash
$ python encryptor.py --encrypt my_secret_password
Encoded password: bXlfc2VjcmV0X3Bhc3N3b3Jk

$ python encryptor.py --decrypt bXlfc2VjcmV0X3Bhc3N3b3Jk
Decoded password: my_secret_password
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or enhancements, please open an issue or submit a pull request.


## Acknowledgments

- Base64 Encoding reference: [RFC 4648](https://tools.ietf.org/html/rfc4648)
