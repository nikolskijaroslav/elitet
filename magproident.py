class Account:
    def __init__(self, address):
        self.address = address

account = Account("0x1234567890ABCDEF")
address_wallet = account.address

print(address_wallet)  # Output: 0x1234567890ABCDEF
