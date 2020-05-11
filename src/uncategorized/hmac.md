> Today I Learned (2018-01-23)

# What is HMAC?

## Definitions

### [HMAC](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)

- In [cryptography](https://en.wikipedia.org/wiki/Cryptography), a **keyed-hash message authentication code** (**HMAC**) is a specific type of [message authentication code](https://en.wikipedia.org/wiki/Message_authentication_code) (MAC) involving a [cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function) and a secret [cryptographic key](https://en.wikipedia.org/wiki/Cryptographic_key).
  -   MAC의 특정한 구현 방법
  -   어떤 hash function을 사용하느냐에 따라 HMAC-SHA1, HMAC-MD5 등으로 불린다.
- Pseudo Code

```
    Function hmac
       Inputs:
          key:        Bytes     array of bytes
          message:    Bytes     array of bytes to be hashed
          hash:       Function  the hash function to use (e.g. SHA-1)
          blockSize:  Integer   the block size of the underlying hash function (e.g. 64 bytes for SHA-1)
          outputSize: Integer   the output size of the underlying hash function (e.g. 20 bytes for SHA-1)
     
       Keys longer than blockSize are shortened by hashing them
       if (length(key) > blockSize) then
          key ← hash(key) //Key becomes outputSize bytes long
       
       Keys shorter than blockSize are padded to blockSize by padding with zeros on the right
       if (length(key) < blockSize) then
          key ← Pad(key, blockSize)  //pad key with zeros to make it blockSize bytes long
        
        o_key_pad = key xor [0x5c * blockSize]   //Outer padded key
        i_key_pad = key xor [0x36 * blockSize]   //Inner padded key
        
        return hash(o_key_pad ∥ hash(i_key_pad ∥ message)) //Where ∥ is concatenation
```
  - Blocksize is 64 (bytes) when using one of the following hash functions: SHA-1, MD5, RIPEMD-128/160.
  - Q. `0x5c` 와 `0x36` 는 어떻게 정해진 것인가?
    - 그냥. 사실 opad !=  ipad 이기만 하면 된다. [link](https://crypto.stackexchange.com/a/3006)

### [MAC](https://en.wikipedia.org/wiki/Message_authentication_code)

- In [cryptography](https://en.wikipedia.org/wiki/Cryptography), a **message authentication code** (**MAC**), sometimes known as a *tag*, is a short piece of information used to [authenticate a message](https://en.wikipedia.org/wiki/Message_authentication)—in other words, to confirm that the message came from the stated sender (its authenticity) and has not been changed. The MAC value protects both a message's [data integrity](https://en.wikipedia.org/wiki/Data_integrity) as well as its [authenticity](https://en.wikipedia.org/wiki/Message_authentication), by allowing verifiers (who also possess the secret key) to detect any changes to the message content.

  - 메시지를 인증하기 위해 사용되는 정보
  - 공유키를 사용한다 => *키 관리가 중요*
  - 메시지의 **무결성 Integrity**(메시지가 변경되지 않음)과 **인증 Authentication**(올바른 송신자에게서 받은 메세지임)을 보장하기 위해

- However, to allow the receiver to be able to detect [replay attacks](https://en.wikipedia.org/wiki/Replay_attack), the message itself must contain data that assures that this same message can only be sent once (e.g. time stamp, sequence number or use of a one-time MAC). Otherwise an attacker could – without even understanding its content – record this message and play it back at a later time, producing the same result as the original sender.

  - 취약점: replay attack에 노출될 수 있음. 이 문제는 메시지에 *한 번만 사용될 수 있는 메시지(예를 들면, 시간 값, 일련번호 등)* 를 포함시키는 것으로 해결 가능.


### Cryptographic hash functions

- SHA-1
- SHA-256
- MD-5




## Usage

### Python의 [hmac](https://docs.python.org/3.6/library/hmac.html) 내장 모듈

[**RFC 2104**](https://tools.ietf.org/html/rfc2104.html)를 토대로 구현했다고 합니다.

- hmac.**new**(*key*, *msg=None*, *digestmod=None*)
  - Return a new **HMAC** object. *key* is a bytes or bytearray object giving the secret key. If *msg* is present, the method call `update(msg)` is made. *digestmod* is the digest name, digest constructor or module for the HMAC object to use. It supports any name suitable to [`hashlib.new()`](https://docs.python.org/3.6/library/hashlib.html#hashlib.new) and defaults to the `hashlib.md5` constructor.
- HMAC.**update**(*msg*)
  - Update the HMAC object with *msg*. Repeated calls are equivalent to a single call with the concatenation of all the arguments: `m.update(a); m.update(b)` is equivalent to `m.update(a + b)`.
- HMAC.**digest**()
  - Return the digest of the bytes passed to the [`update()`](https://docs.python.org/3.6/library/hmac.html#hmac.HMAC.update) method so far. This bytes object will be the same length as the *digest_size* of the digest given to the constructor. It may contain non-ASCII bytes, including NUL bytes.

---

#### More - 읽을거리

- [패스워드 저장 알고리즘](http://d2.naver.com/helloworld/318732)
- [비밀번호 해시에 소금치기 - 바르게 쓰기](http://starplatina.tistory.com/entry/%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%ED%95%B4%EC%8B%9C%EC%97%90-%EC%86%8C%EA%B8%88%EC%B9%98%EA%B8%B0-%EB%B0%94%EB%A5%B4%EA%B2%8C-%EC%93%B0%EA%B8%B0)
