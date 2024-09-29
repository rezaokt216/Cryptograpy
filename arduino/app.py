# app.py

from flask import Flask, request, render_template, send_file
import base64
from ciphers import vigenere_encrypt, vigenere_decrypt, auto_key_encrypt, playfair_encrypt, hill_encrypt, super_encrypt, encode_base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    key = request.form['key']
    plaintext = request.form['plaintext']
    cipher_type = request.form['cipher_type']
    
    if cipher_type == 'vigenere':
        ciphertext = vigenere_encrypt(plaintext, key)
    # Implementasi cipher lainnya
    # ...
    
    return encode_base64(ciphertext)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    key = request.form['key']
    ciphertext = request.form['ciphertext']
    cipher_type = request.form['cipher_type']
    
    if cipher_type == 'vigenere':
        plaintext = vigenere_decrypt(ciphertext, key)
    # Implementasi cipher lainnya
    # ...
    
    return encode_base64(plaintext)

if __name__ == '__main__':
    app.run(debug=True)
