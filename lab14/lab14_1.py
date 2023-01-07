import privy

encrypted_pw = privy.hide(b'my_password', b'decrypt')
print(encrypted_pw)
print(privy.peek(encrypted_pw, b'decrypt').decode('utf-8'))