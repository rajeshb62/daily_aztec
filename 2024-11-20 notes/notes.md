Fist audio transcript of today contains progress and 'what do' for today

what do for today:
1. interact with hardcoded aztec contract, send transactions with it via typescript script, interact with token contract already deployed. use aztec-wallet cli command where desired
2. rip out parts of the aztec silly wallet- currently hardcoded schnorr account in aztec-experiments

EOD notes:
completed aztec docs way of deployment of hardcoded contract. Deployment of token contract using the account and minting private balance, viewing private balance of it. 
Good use of end to end testing in yarn-project of aztec-packages for typescript bindings lead by docs
Good use of noir-projects.js in yarn-project which contains codegen, .ts files bindings for noir-projects in aztec-nr. But repo only has script that you can use to build codegen for all noir-projects rather than having the .ts files directly.