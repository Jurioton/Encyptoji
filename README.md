# Encyptoji

## Overview
This project provides a simple way to encrypt and decrypt files using the `cryptmoji` library. Users can securely encrypt their text files and later decrypt them using the same key, ensuring the confidentiality of their content.

## Features
- **Encryption**: Encrypt text files using a specified key.
- **Decryption**: Decrypt previously encrypted text files using the same key.
- **File Handling**: Automatically saves encrypted and decrypted content to new files.

## How It Works
The project utilizes the `cryptmoji` library to encrypt and decrypt file contents. The encryption process involves reading the content from a source file, applying the encryption function with the provided key, and saving the output to a new file. The decryption process follows a similar flow.

## Getting Started

### Prerequisites
- Python 3.x
- `cryptmoji` library

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Jurioton/Encyptoji.git
   cd Encyptoji
   #encryption 
   python encryption.py
   #decryption 
   python decryption.py 
   ```

   ## Future Improvements
- Implement a graphical user interface (GUI) for easier interaction.
- Add error handling to manage incorrect file paths or keys.
- Extend functionality to support other file formats.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [cryptmoji](https://pypi.org/project/cryptmoji/) for the encryption and decryption functionality.

