<a id="aea.crypto.base"></a>

# aea.crypto.base

Abstract module wrapping the public and private key cryptography and ledger api.

<a id="aea.crypto.base.Crypto"></a>

## Crypto Objects

```python
class Crypto(Generic[EntityClass], ABC)
```

Base class for a crypto object.

<a id="aea.crypto.base.Crypto.__init__"></a>

#### `__`init`__`

```python
def __init__(private_key_path: Optional[str] = None,
             password: Optional[str] = None,
             extra_entropy: Union[str, bytes, int] = "",
             **kwargs: Any) -> None
```

Initialize the crypto object.

The actual behaviour of this constructor is determined by the abstract
methods 'generate_private_key()' and 'load_private_key_from_path().
Either way, the entity object will be accessible as a property.

**Arguments**:

- `private_key_path`: the path to the private key.
If None, the key will be generated by 'generate_private_key()'.
If not None, the path will be processed by 'load_private_key_from_path()'.
- `password`: the password to encrypt/decrypt the private key.
- `extra_entropy`: add extra randomness to whatever randomness your OS can provide
- `kwargs`: keyword arguments.

<a id="aea.crypto.base.Crypto.generate_private_key"></a>

#### generate`_`private`_`key

```python
@classmethod
@abstractmethod
def generate_private_key(cls,
                         extra_entropy: Union[str, bytes,
                                              int] = "") -> EntityClass
```

Generate a private key.

**Arguments**:

- `extra_entropy`: add extra randomness to whatever randomness your OS can provide

**Returns**:

the entity object. Implementation dependent.

<a id="aea.crypto.base.Crypto.load_private_key_from_path"></a>

#### load`_`private`_`key`_`from`_`path

```python
@classmethod
@abstractmethod
def load_private_key_from_path(cls,
                               file_name: str,
                               password: Optional[str] = None) -> EntityClass
```

Load a private key in hex format for raw private key and json format for encrypted private key from a file.

**Arguments**:

- `file_name`: the path to the hex/json file.
- `password`: the password to encrypt/decrypt the private key.

**Returns**:

the entity object.

<a id="aea.crypto.base.Crypto.entity"></a>

#### entity

```python
@property
def entity() -> EntityClass
```

Return an entity object.

**Returns**:

an entity object

<a id="aea.crypto.base.Crypto.private_key"></a>

#### private`_`key

```python
@property
@abstractmethod
def private_key() -> str
```

Return a private key.

**Returns**:

a private key string

<a id="aea.crypto.base.Crypto.public_key"></a>

#### public`_`key

```python
@property
@abstractmethod
def public_key() -> str
```

Return a public key.

**Returns**:

a public key string

<a id="aea.crypto.base.Crypto.address"></a>

#### address

```python
@property
@abstractmethod
def address() -> str
```

Return the address.

**Returns**:

an address string

<a id="aea.crypto.base.Crypto.sign_message"></a>

#### sign`_`message

```python
@abstractmethod
def sign_message(message: bytes, is_deprecated_mode: bool = False) -> str
```

Sign a message in bytes string form.

**Arguments**:

- `message`: the message to be signed
- `is_deprecated_mode`: if the deprecated signing is used

**Returns**:

signature of the message in string form

<a id="aea.crypto.base.Crypto.sign_transaction"></a>

#### sign`_`transaction

```python
@abstractmethod
def sign_transaction(transaction: JSONLike) -> JSONLike
```

Sign a transaction in dict form.

**Arguments**:

- `transaction`: the transaction to be signed

**Returns**:

signed transaction

<a id="aea.crypto.base.Crypto.load"></a>

#### load

```python
@classmethod
def load(cls, private_key_file: str, password: Optional[str] = None) -> str
```

Load private key from file.

**Arguments**:

- `private_key_file`: the file where the key is stored.
- `password`: the password to encrypt/decrypt the private key.

**Returns**:

private_key in hex string format

<a id="aea.crypto.base.Crypto.dump"></a>

#### dump

```python
def dump(private_key_file: str, password: Optional[str] = None) -> None
```

Dump private key to file.

**Arguments**:

- `private_key_file`: the file where the key is stored.
- `password`: the password to encrypt/decrypt the private key.

<a id="aea.crypto.base.Crypto.encrypt"></a>

#### encrypt

```python
@abstractmethod
def encrypt(password: str) -> str
```

Encrypt the private key and return in json.

**Arguments**:

- `password`: the password to decrypt.

**Returns**:

json string containing encrypted private key.

<a id="aea.crypto.base.Crypto.decrypt"></a>

#### decrypt

```python
@classmethod
@abstractmethod
def decrypt(cls, keyfile_json: str, password: str) -> str
```

Decrypt the private key and return in raw form.

**Arguments**:

- `keyfile_json`: json string containing encrypted private key.
- `password`: the password to decrypt.

**Returns**:

the raw private key.

<a id="aea.crypto.base.Helper"></a>

## Helper Objects

```python
class Helper(ABC)
```

Interface for helper class usable as Mixin for LedgerApi or as standalone class.

<a id="aea.crypto.base.Helper.is_transaction_settled"></a>

#### is`_`transaction`_`settled

```python
@staticmethod
@abstractmethod
def is_transaction_settled(tx_receipt: JSONLike) -> bool
```

Check whether a transaction is settled or not.

**Arguments**:

- `tx_receipt`: the receipt associated to the transaction.

**Returns**:

True if the transaction has been settled, False o/w.

<a id="aea.crypto.base.Helper.is_transaction_valid"></a>

#### is`_`transaction`_`valid

```python
@staticmethod
@abstractmethod
def is_transaction_valid(tx: JSONLike, seller: Address, client: Address,
                         tx_nonce: str, amount: int) -> bool
```

Check whether a transaction is valid or not.

**Arguments**:

- `tx`: the transaction.
- `seller`: the address of the seller.
- `client`: the address of the client.
- `tx_nonce`: the transaction nonce.
- `amount`: the amount we expect to get from the transaction.

**Returns**:

True if the random_message is equals to tx['input']

<a id="aea.crypto.base.Helper.get_contract_address"></a>

#### get`_`contract`_`address

```python
@staticmethod
@abstractmethod
def get_contract_address(tx_receipt: JSONLike) -> Optional[str]
```

Get the contract address from a transaction receipt.

**Arguments**:

- `tx_receipt`: the transaction digest

**Returns**:

the contract address if successful

<a id="aea.crypto.base.Helper.generate_tx_nonce"></a>

#### generate`_`tx`_`nonce

```python
@staticmethod
@abstractmethod
def generate_tx_nonce(seller: Address, client: Address) -> str
```

Generate a unique hash to distinguish transactions with the same terms.

**Arguments**:

- `seller`: the address of the seller.
- `client`: the address of the client.

**Returns**:

return the hash in hex.

<a id="aea.crypto.base.Helper.get_address_from_public_key"></a>

#### get`_`address`_`from`_`public`_`key

```python
@classmethod
@abstractmethod
def get_address_from_public_key(cls, public_key: str) -> str
```

Get the address from the public key.

**Arguments**:

- `public_key`: the public key

**Returns**:

str

<a id="aea.crypto.base.Helper.recover_message"></a>

#### recover`_`message

```python
@classmethod
@abstractmethod
def recover_message(cls,
                    message: bytes,
                    signature: str,
                    is_deprecated_mode: bool = False) -> Tuple[Address, ...]
```

Recover the addresses from the hash.

**Arguments**:

- `message`: the message we expect
- `signature`: the transaction signature
- `is_deprecated_mode`: if the deprecated signing was used

**Returns**:

the recovered addresses

<a id="aea.crypto.base.Helper.recover_public_keys_from_message"></a>

#### recover`_`public`_`keys`_`from`_`message

```python
@classmethod
@abstractmethod
def recover_public_keys_from_message(
        cls,
        message: bytes,
        signature: str,
        is_deprecated_mode: bool = False) -> Tuple[str, ...]
```

Get the public key used to produce the `signature` of the `message`

**Arguments**:

- `message`: raw bytes used to produce signature
- `signature`: signature of the message
- `is_deprecated_mode`: if the deprecated signing was used

**Returns**:

the recovered public keys

<a id="aea.crypto.base.Helper.get_hash"></a>

#### get`_`hash

```python
@staticmethod
@abstractmethod
def get_hash(message: bytes) -> str
```

Get the hash of a message.

**Arguments**:

- `message`: the message to be hashed.

**Returns**:

the hash of the message.

<a id="aea.crypto.base.Helper.is_valid_address"></a>

#### is`_`valid`_`address

```python
@classmethod
@abstractmethod
def is_valid_address(cls, address: Address) -> bool
```

Check if the address is valid.

**Arguments**:

- `address`: the address to validate

<a id="aea.crypto.base.Helper.load_contract_interface"></a>

#### load`_`contract`_`interface

```python
@classmethod
@abstractmethod
def load_contract_interface(cls, file_path: Path) -> Dict[str, str]
```

Load contract interface.

**Arguments**:

- `file_path`: the file path to the interface

**Returns**:

the interface

<a id="aea.crypto.base.LedgerApi"></a>

## LedgerApi Objects

```python
class LedgerApi(Helper, ABC)
```

Interface for ledger APIs.

<a id="aea.crypto.base.LedgerApi.api"></a>

#### api

```python
@property
@abstractmethod
def api() -> Any
```

Get the underlying API object.

This can be used for low-level operations with the concrete ledger APIs.
If there is no such object, return None.

<a id="aea.crypto.base.LedgerApi.get_balance"></a>

#### get`_`balance

```python
@abstractmethod
def get_balance(address: Address, raise_on_try: bool = False) -> Optional[int]
```

Get the balance of a given account.

This usually takes the form of a web request to be waited synchronously.

**Arguments**:

- `address`: the address.
- `raise_on_try`: whether the method will raise or log on error

**Returns**:

the balance.

<a id="aea.crypto.base.LedgerApi.get_state"></a>

#### get`_`state

```python
@abstractmethod
def get_state(callable_name: str,
              *args: Any,
              raise_on_try: bool = False,
              **kwargs: Any) -> Optional[JSONLike]
```

Call a specified function on the underlying ledger API.

This usually takes the form of a web request to be waited synchronously.

**Arguments**:

- `callable_name`: the name of the API function to be called.
- `args`: the positional arguments for the API function.
- `raise_on_try`: whether the method will raise or log on error
- `kwargs`: the keyword arguments for the API function.

**Returns**:

the ledger API response.

<a id="aea.crypto.base.LedgerApi.get_transfer_transaction"></a>

#### get`_`transfer`_`transaction

```python
@abstractmethod
def get_transfer_transaction(sender_address: Address,
                             destination_address: Address, amount: int,
                             tx_fee: int, tx_nonce: str,
                             **kwargs: Any) -> Optional[JSONLike]
```

Submit a transfer transaction to the ledger.

**Arguments**:

- `sender_address`: the sender address of the payer.
- `destination_address`: the destination address of the payee.
- `amount`: the amount of wealth to be transferred.
- `tx_fee`: the transaction fee.
- `tx_nonce`: verifies the authenticity of the tx
- `kwargs`: the keyword arguments.

**Returns**:

the transfer transaction

<a id="aea.crypto.base.LedgerApi.send_signed_transaction"></a>

#### send`_`signed`_`transaction

```python
@abstractmethod
def send_signed_transaction(tx_signed: JSONLike,
                            raise_on_try: bool = False) -> Optional[str]
```

Send a signed transaction and wait for confirmation.

Use keyword arguments for the specifying the signed transaction payload.

**Arguments**:

- `tx_signed`: the signed transaction
- `raise_on_try`: whether the method will raise or log on error

**Returns**:

tx_digest, if present

<a id="aea.crypto.base.LedgerApi.get_transaction_receipt"></a>

#### get`_`transaction`_`receipt

```python
@abstractmethod
def get_transaction_receipt(tx_digest: str,
                            raise_on_try: bool = False) -> Optional[JSONLike]
```

Get the transaction receipt for a transaction digest.

**Arguments**:

- `tx_digest`: the digest associated to the transaction.
- `raise_on_try`: whether the method will raise or log on error

**Returns**:

the tx receipt, if present

<a id="aea.crypto.base.LedgerApi.get_transaction"></a>

#### get`_`transaction

```python
@abstractmethod
def get_transaction(tx_digest: str,
                    raise_on_try: bool = False) -> Optional[JSONLike]
```

Get the transaction for a transaction digest.

**Arguments**:

- `tx_digest`: the digest associated to the transaction.
- `raise_on_try`: whether the method will raise or log on error

**Returns**:

the tx, if present

<a id="aea.crypto.base.LedgerApi.get_contract_instance"></a>

#### get`_`contract`_`instance

```python
@abstractmethod
def get_contract_instance(contract_interface: Dict[str, str],
                          contract_address: Optional[str] = None) -> Any
```

Get the instance of a contract.

**Arguments**:

- `contract_interface`: the contract interface.
- `contract_address`: the contract address.

**Returns**:

the contract instance

<a id="aea.crypto.base.LedgerApi.get_deploy_transaction"></a>

#### get`_`deploy`_`transaction

```python
@abstractmethod
def get_deploy_transaction(contract_interface: Dict[str, str],
                           deployer_address: Address,
                           raise_on_try: bool = False,
                           **kwargs: Any) -> Optional[JSONLike]
```

Get the transaction to deploy the smart contract.

**Arguments**:

- `contract_interface`: the contract interface.
- `deployer_address`: The address that will deploy the contract.
- `raise_on_try`: whether the method will raise or log on error
- `kwargs`: the keyword arguments.

**Returns**:

`tx`: the transaction dictionary.

<a id="aea.crypto.base.LedgerApi.update_with_gas_estimate"></a>

#### update`_`with`_`gas`_`estimate

```python
@abstractmethod
def update_with_gas_estimate(transaction: JSONLike) -> JSONLike
```

Attempts to update the transaction with a gas estimate

**Arguments**:

- `transaction`: the transaction

**Returns**:

the updated transaction

<a id="aea.crypto.base.LedgerApi.contract_method_call"></a>

#### contract`_`method`_`call

```python
@abstractmethod
def contract_method_call(contract_instance: Any, method_name: str,
                         **method_args: Any) -> Optional[JSONLike]
```

Call a contract's method

**Arguments**:

- `contract_instance`: the contract to use
- `method_name`: the contract method to call
- `method_args`: the contract call parameters

<a id="aea.crypto.base.LedgerApi.build_transaction"></a>

#### build`_`transaction

```python
@abstractmethod
def build_transaction(contract_instance: Any,
                      method_name: str,
                      method_args: Optional[Dict],
                      tx_args: Optional[Dict],
                      raise_on_try: bool = False) -> Optional[JSONLike]
```

Prepare a transaction

**Arguments**:

- `contract_instance`: the contract to use
- `method_name`: the contract method to call
- `method_args`: the contract parameters
- `tx_args`: the transaction parameters
- `raise_on_try`: whether the method will raise or log on error

<a id="aea.crypto.base.LedgerApi.get_transaction_transfer_logs"></a>

#### get`_`transaction`_`transfer`_`logs

```python
@abstractmethod
def get_transaction_transfer_logs(
        contract_instance: Any,
        tx_hash: str,
        target_address: Optional[str] = None) -> Optional[JSONLike]
```

Get all transfer events derived from a transaction.

**Arguments**:

- `contract_instance`: the contract
- `tx_hash`: the transaction hash
- `target_address`: optional address to filter transfer events to just those that affect it

<a id="aea.crypto.base.FaucetApi"></a>

## FaucetApi Objects

```python
class FaucetApi(ABC)
```

Interface for testnet faucet APIs.

<a id="aea.crypto.base.FaucetApi.get_wealth"></a>

#### get`_`wealth

```python
@abstractmethod
def get_wealth(address: Address, url: Optional[str] = None) -> None
```

Get wealth from the faucet for the provided address.

**Arguments**:

- `address`: the address.
- `url`: the url

**Returns**:

None

