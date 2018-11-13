<div align="center">
  <h1>tibc</h1>

  <a href="https://travis-ci.org/manparvesh/tibc/builds" target="_blank"><img src="https://img.shields.io/travis-ci/manparvesh/tibc.svg?style=for-the-badge" alt="Build Status"></a> 
  <a href="https://manparvesh.mit-license.org/" target="_blank"><img src="https://img.shields.io/badge/license-MIT-blue.svg?longCache=true&style=for-the-badge" alt="License"></a> 
  <a href="https://codecov.io/gh/manparvesh/tibc" target="_blank"><img src="https://img.shields.io/codecov/c/github/manparvesh/tibc/master.svg?style=for-the-badge" alt="Coverage"></a>
  <p>A tiny blockchain implementation in Python</p>
</div>

## Features
- Simple but complete implementation of a blockchain
- Implementation of proof of work.

## How to use
```python
from tibc import Blockchain

block_one_transactions = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
block_two_transactions = {"sender": "Bob", "receiver": "Cole", "amount": "25"}
block_three_transactions = {"sender": "Alice", "receiver": "Cole", "amount": "35"}
fake_transactions = {"sender": "Bob", "receiver": "Cole, Alice", "amount": "25"}

blockchain = Blockchain()
blockchain.print_blocks()

blockchain.add_block(block_one_transactions)
blockchain.add_block(block_two_transactions)
blockchain.add_block(block_three_transactions)
blockchain.print_blocks()
blockchain.validate_chain() # returns true

blockchain.chain[2].transactions = fake_transactions
blockchain.validate_chain() # returns false, since the contents are changed
```

## LICENSE

```
MIT License

Copyright (c) 2018 Man Parvesh Singh Randhawa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

