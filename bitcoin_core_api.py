import requests
import os
from random import SystemRandom
import base64
import hmac
import json


class BitcoinCoreApi(object):

    schema = 'http://'
    username = ''
    password = ''
    host = 'localhost'
    port = '8332'

    def full_path(self):
        """
        Get full path to RPC
        :return: full url to RPC server
        """
        return '{schema}{username}:{password}@{host}:{port}'.format(schema=self.schema,
                                                                     username=self.username,
                                                                     password=self.password,
                                                                     host=self.host,
                                                                     port=self.port)


    def connect(self,*args,**kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        try:
            request = requests.post(self.full_path(self), data = json.dumps(kwargs))
            result = json.loads(request.text)
            if result.get('error',None):
                # Raise error?
                return result.get('error')
            else:
                return result.get('result')
        except ConnectionRefusedError:
            return
        except requests.exceptions.ConnectionError:
            return


class Blockchain(BitcoinCoreApi):
    def __init__(self,bitcoincoreapi):
        self.conn_properties = bitcoincoreapi

    def get_best_block_hash(self,request_id:str) -> str:
        """
        Returns the header hash of the most recent block on the best block chain.
        :return: The hash of the block header from the most recent block on the best block chain, encoded as hex in
        RPC byte order
        """
        method = 'getblockhash'
        return self.conn_properties.connect(self.conn_properties, method=method, params=[0], id=request_id)

    def get_block(self,block_hash,request_id:str) -> dict:
        """
        Gets a block with a particular header hash from the local block database either as a JSON object or as a
        serialized block.
        :param block_hash: The hash of the header of the block to get, encoded as hex in RPC byte order
        :param request_id:
        :return: The requested block as a serialized block, encoded as hex, or JSON null if an error occurred
        """
        method = 'getblock'
        return self.conn_properties.connect (self.conn_properties, method=method, params=[block_hash], id=request_id)

    def get_block_chain_info(self,request_id:str) -> dict:
        """
        Provides information about the current state of the block chain.
        :param request_id:
        :return: The number of blocks in the local best block chain. For a new node with only the hardcoded genesis
        block, this number will be 0
        """
        method = 'getblockchaininfo'
        return self.conn_properties.connect (self.conn_properties, method=method, params=[], id=request_id)

    def get_block_count(self,request_id:str) -> int:
        """
        Returns the number of blocks in the local best block chain.
        :param request_id:
        :return: The hash of the block at the requested height, encoded as hex in RPC byte order, or JSON null if an
        error occurred
        """
        method = 'getblockcount'
        return self.conn_properties.connect (self.conn_properties, method=method, params=[], id=request_id)

    def get_block_hash(self,block_height:int,request_id:str) -> str:
        """
        Returns the header hash of a block at the given height in the local best block chain.
        :param block_height: The height of the block whose header hash should be returned. The height of the hardcoded
        genesis block is 0
        :param request_id:
        :return:
        """
        method = 'getblockhash'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[int(block_height)], id=request_id)

    def get_block_header(self,block_hash:str,request_id:str) -> dict:
        method = 'getblockheader'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[str (block_hash)], id=request_id)

    def get_chain_tips(self,request_id:str) -> dict:
        method = 'getchaintips'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def get_connection_count(self,request_id:str) -> int:
        method = 'getconnectioncount'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)
    def get_difficulty(self,request_id:str) -> float:
        method = 'getdifficulty'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def get_info(self,request_id:str) -> dict:
        method = 'getinfo'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def get_memory_info(self,request_id:str) -> dict:
        method = 'getmemoryinfo'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def get_mem_pool_ancestors(self,txid:str,request_id:str) -> dict:
        method = 'getmempoolancestors'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[txid], id=request_id)

    def get_mem_pool_descendants(self,txid:str,request_id:str) -> dict:
        method = 'getmempooldescendants'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[txid], id=request_id)

    def get_mem_pool_info(self,txid:str,request_id:str) -> dict:
        method = 'getmempooldescendants'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[txid], id=request_id)

    def get_raw_mem_pool(self,request_id:str) -> dict:
        method = 'getmempoolinfo'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)


    def get_tx_out(self,txid:str,vout:int,request_id:str) -> dict:
        method = 'gettxout'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[txid,vout], id=request_id)


    def get_tx_out_proof(self,txids:list,header:str,request_id:str) -> dict:
        method = 'gettxoutproof'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[txids, header], id=request_id)

    def get_tx_out_set_info(self,request_id:str) -> dict:
        method = 'gettxoutsetinfo'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def precious_block(self,request_id:str) -> dict:
        method = 'preciousblock'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def prune_block_chain(self,height:int,request_id:str) -> dict:
        method = 'pruneblockchain'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[height], id=request_id)

    def verify_chain(self,check_level:int,number_of_blocks:int,request_id:str) -> dict:
        method = 'verifychain'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[check_level,number_of_blocks], id=request_id)

    def verify_tx_out_proof(self,proof:str,request_id:str) -> dict:
        method = 'verifytxoutproof'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[proof], id=request_id)


class Control:

    def get_info(self):
        pass

    def help(self):
        pass

    def stop(self):
        pass


class Generating:

    def generate(self):
        pass

    def generate_to_address(self):
        pass


class Mining:
    def __init__(self,bitcoincoreapi):
        self.conn_properties = bitcoincoreapi

    def get_block_template(self):
        pass

    def get_mining_info(self,request_id:str) -> dict:
        method = 'getmininginfo'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def get_network_hash_ps(self):
        pass

    def prioritise_transactions(self):
        pass

    def submit_block(self):
        pass


class Network:

    def add_node(self):
        pass

    def clear_banned(self):
        pass

    def disconnect_node(self):
        pass

    def get_added_node_info(self):
        pass

    def get_connection_count(self):
        pass

    def get_net_totals(self):
        pass

    def get_network_info(self):
        pass

    def get_peer_info(self):
        pass

    def list_banned(self):
        pass

    def ping(self):
        pass

    def set_ban(self):
        pass

    def set_network_active(self):
        pass

class Wallet(BitcoinCoreApi):
    def __init__(self,bitcoincoreapi):
        self.conn_properties = bitcoincoreapi

    def abandon_transaction(self,txid:str,request_id:str) -> None:
        method = 'abandontransaction'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[txid], id=request_id)

    def add_witness_address(self,address:str,request_id:str) -> str:
        method = 'addwitnessaddress'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[address], id=request_id)

    def add_multisig_address(self, number_of_signatures: int, keys_or_addresses: list,account:str,request_id: str) -> None:
        method = 'addmultisigaddress'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[number_of_signatures,keys_or_addresses], id=request_id)

    def backup_wallet(self,destination:str,request_id:str) -> dict:
        method = 'backupwallet'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[destination], id=request_id)

    def bump_fee(self,txid:str,request_id:str,conf_target:int=None,total_fee:int=None,replaceable:bool=None) -> bytearray:
        method = 'bumpfee'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[txid,conf_target,total_fee,replaceable ], id=request_id)

    def dump_priv_key(self,p2pkh:str,request_id:str) -> str:
        method = 'dumpprivkey'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[p2pkh], id=request_id)

    def dump_wallet(self,filename:str,request_id:str) -> str:
        method = 'dumpwallet'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[filename], id=request_id)

    def encrypt_wallet(self,passphrase:str,request_id:str) -> str:
        method = 'encryptwallet'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[passphrase], id=request_id)

    def get_account(self,address:str,request_id:str) -> str:
        method = 'getaccount'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[address], id=request_id)

    def get_balance(self,account:str,request_id:str,number_of_confirmations:int=1,watch_only:bool=True) -> str:
        method = 'getbalance'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[account,number_of_confirmations,watch_only], id=request_id)

    def get_new_adress(self,account:str,address_type:['legacy','p2sh-segwit','bech32'],request_id:str) -> str:
        method = 'getnewaddress'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[account, address_type], id=request_id)

    def get_raw_change_address(self,request_id:str) -> str:
        method = 'getrawchangeaddress'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def get_received_by_address(self,account:str,request_id:str,number_of_confirmations:int=5) -> str:
        method = 'getreceivedbyaccount'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[account,number_of_confirmations], id=request_id)

    def get_transaction(self,txid:str,request_id:str) -> dict:
        method = 'gettransaction'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[txid], id=request_id)

    def get_unconfirmed_balance(self,request_id:str) -> float:
        method = 'getunconfirmedbalance'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def get_wallet_info(self,request_id:str) -> dict:
        method = 'getwalletinfo'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def import_address(self,address_or_script:str,account:str,request_id:str,rescan:bool=True):
        method = 'importaddress'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[address_or_script,account,rescan], id=request_id)

    def import_multi(self,imports:list,request_id:str) -> dict:
        method = 'importmulti'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[imports], id=request_id)

    def import_pruned_funds(self,raw_transaction:str,tx_out_proof:str,request_id:str) ->None:
        method = 'importprunedfunds'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[raw_transaction,tx_out_proof], id=request_id)

    def import_priv_key(self,priv_key:str,account:str,request_id:str,rescan:bool=True) -> None:
        method = 'importprivkey'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[priv_key,account,rescan], id=request_id)

    def import_wallet(self,filename:str,request_id) -> None:
        method = 'importwallet'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[filename], id=request_id)

    def key_pool_refill(self,key_pool_size:int,request_id) -> None:
        method = 'keypoolrefill'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[key_pool_size], id=request_id)

    def list_address_groupings(self,request_id:str):
        method = 'listaddressgroupings'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def list_lock_unspent(self,request_id:str):
        method = 'listlockunspent'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[], id=request_id)

    def list_received_by_adress(self,request_id:str,confirmations:int=5,include_empty:bool=False,watch_only:bool=True) -> dict:
        method = 'listreceivedbyaddress'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[confirmations,include_empty,watch_only], id=request_id)

    def list_since_block(self,block_header:str,request_id:str,confirmations:int=5,watch_only:bool=True):
        method = 'listsinceblock'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[block_header,confirmations,watch_only], id=request_id)

    def list_transactions(self,account:str,transactions_count:int,skip_transactions:int,request_id:str,watch_only:bool=True) -> dict:
        method = 'listtransactions'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[account,transactions_count,skip_transactions,watch_only], id=request_id)

    def list_unspent(self,min_confirmations:int,max_confirmations:int,addresses:list,request_id):
        method = 'listunspent'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[min_confirmations,max_confirmations,addresses], id=request_id)

    def lock_unspent(self,unlock:bool,outputs:{'txid','vout'},request_id:str):
        method = 'lockunspent'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[outputs,unlock], id=request_id)

    def remove_pruned_funds(self,):
        method = 'removeprunedfunds'
        return self.conn_properties.connect (self.conn_properties, method=method,
                                             params=[outputs, unlock], id=request_id)

    def send_many(self):
        method = ''

    def send_to_address(self):
        method = ''

    def set_tx_fee(self):
        method = ''

    def sign_message(self):
        method = ''

    def sign_message_with_priv_key(self):
        method = ''

    def wallet_lock(self):
        method = ''

    def wallet_passphrase(self):
        method = ''

    def wallet_passphrase_change(self):
        method = ''



def generate_salt():
    # This uses os.urandom() underneath
    cryptogen = SystemRandom()

    # Create 16 byte hex salt
    salt_sequence = [cryptogen.randrange(256) for _ in range(16)]
    return ''.join([format(r, 'x') for r in salt_sequence])

def generate_password():
    """Create 32 byte b64 password"""
    return base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')

def password_to_hmac(salt, password):
    m = hmac.new(bytearray(salt, 'utf-8'), bytearray(password, 'utf-8'), 'SHA256')
    return m.hexdigest()


def main(username,password=None):
    salt = generate_salt()
    if not password:
        password = generate_password()
    password_hmac = password_to_hmac(salt, password)

    print('String to be appended to bitcoin.conf:')
    print('rpcauth={0}:{1}${2}'.format(username, salt, password_hmac))
    print('Your password:\n{0}'.format(password))

