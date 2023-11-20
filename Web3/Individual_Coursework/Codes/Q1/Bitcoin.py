from ecc import PrivateKey
from helper import hash256, little_endian_to_int, decode_base58, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx

# Q1: Create 4 Bitcoin Testnet addresses
# Create a Bitcoin Testnet address for address1
secret1 = little_endian_to_int(hash256(b'address1')) 
private_key1 = PrivateKey(secret1)
address1 = private_key1.point.address(testnet=True) 
print("Address1: "+address1)
print("Secret1: ",secret1)

# Create a Bitcoin Testnet address for address2
secret2 = little_endian_to_int(hash256(b'address2')) 
private_key2 = PrivateKey(secret2)
address2 = private_key2.point.address(testnet=True) 
print("Address2: "+address2)
print("Secret2: ",secret2)

# Create a Bitcoin Testnet address for address3
secret3 = little_endian_to_int(hash256(b'address3')) 
private_key3 = PrivateKey(secret3)
address3 = private_key3.point.address(testnet=True) 
print("Address3: "+address3)
print("Secret3: ",secret3)

# Create a Bitcoin Testnet address for address4
secret4 = little_endian_to_int(hash256(b'address4')) 
private_key4 = PrivateKey(secret4)
address4 = private_key4.point.address(testnet=True) 
print("Address4: "+address4)
print("Secret4: ",secret4)

# Q2: from previous transaction the address1 received 0.00006453 BTC from BTC testnet faucet
# i.e. 6453 Satoshis
# Q3: Create a 1-input 3-outputs transactions
# 1 input
prev_tx = bytes.fromhex('7f5efd9faa3a5f0e5f32670e2c5564ce40e6a9c3ebae01c781cdbf527cc05974') 
prev_index = 0
tx_in1 = TxIn(prev_tx, prev_index)

# 3 outputs
tx_outs = []
# Transfer 0.000032265 BTC (50%) to address2 - Output1
target_amount1 = int(3226.5)
target_h160_1 = decode_base58('mmhnuqdP8MsWP5pTBaga3s5Dax9KZvo4BL') 
target_script1 = p2pkh_script(target_h160_1)
target_output1 = TxOut(amount=target_amount1, script_pubkey=target_script1)
# Transfer 0.000019359 BTC (30%) to address3 - Output2
target_amount2 = int(1935.9)
target_h160_2 = decode_base58('mwqRTEDBFNWo3ZAFcYAWovxtq6Muao69f9') 
target_script2 = p2pkh_script(target_h160_2)
target_output2 = TxOut(amount=target_amount2, script_pubkey=target_script2)
# Transfer 0.0000096795 BTC (15%) to address4 - Output3
target_amount3 = int(967.95)
target_h160_3 = decode_base58('mtS5MKhUgiGTqqeQzx6ux8kdegBawYwMsk') 
target_script3 = p2pkh_script(target_h160_3)
target_output3 = TxOut(amount=target_amount3, script_pubkey=target_script3)

# Define the transaction
tx_obj = Tx(1, [tx_in1], [target_output1, target_output2, target_output3], 0, True) 
print(tx_obj)

z = tx_obj.sig_hash(0)
# use address1's secret
private_key = PrivateKey(secret=92796367777975090783698567212022215639238203613608596400466403599635546939269) 
der = private_key.sign(z).der()
sig = der + SIGHASH_ALL.to_bytes(1, 'big')
sec = private_key.point.sec()
script_sig = Script([sig, sec])
tx_obj.tx_ins[0].script_sig = script_sig
print(tx_obj.serialize().hex())