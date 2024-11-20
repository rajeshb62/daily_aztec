plan of action:

1. examine aztec hardcoded schnorr account deployment sandbox and terminal logs using aztec-wallet get-tx (tx hash)
2. deploy accounts, tokens, mint public tokens, send some to aztec silly account, check balance public balance. examine tx, etc etc.
3. deploy hardcoded account using alicewallet initial account
4. understand public_key_x, public_key_y hardcoded in silly account. and rest of hardcoded account, which are the signing keys which are the encryption privacy keys
5. understand authwit and aztec libraries of aztec-nr from perspective of custom account creation.
6. rip out parts of silly aztec account to replace progressively with the silly account captured in this python file: [text](<../../../stuff/simplest auth scheme.ipynb>)

repo: aztec silly account current home: https://github.com/rajeshb62/aztec-experiment.git

claude urls:
https://claude.ai/chat/d289aa34-9732-49b5-b859-1d52c8c20ee0
deepdive into account nr code starting with authwit library: https://claude.ai/chat/a0ae69bb-7879-423d-9bf9-01e56c888a58
sandbox tx containing silly aztec account (hardcoded schnorr): 2b9f9abf45747cc2a9bb57d812a40c5efe9493df7efa8ca669945a2893eba7ab

Midday update:
*alicewallet use for deploying hardcoded account did not succeed
*deployment address of account contract is it's account contract address. how does it link to the private key? because it is deterministically created from private key and salt
*the public key in hardcoded account is signing public key (with corresponding private key kept secret?) so there are separate encryption public/private keys?