// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20 {
    function totalSupply() external view returns (uint);

    function balanceOf(address account) external view returns (uint);

    function transfer(address recipient, uint amount) external returns (bool);

    function allowance(address owner, address spender) external view returns (uint);

    function approve(address spender, uint amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint amount
    ) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint value);
    event Approval(address indexed owner, address indexed spender, uint value);
}

// token 1 with name comp163_1 and symbol comp1
contract token1 is IERC20 {
    // Specify the total supply of tokens
    uint public totalSupply = 100;
  
    // Create a mapping to keep track of balances
    mapping (address => uint) public balanceOf;
 
    // Create a mapping to keep track of allowances
    mapping (address => mapping(address => uint)) public allowance;

    // Specify the name of the token
    string public name = "comp163_1";

    // Specify the symbol of the token
    string public symbol = "comp1";

    // Specify the number of decimals for the token
    uint public decimals = 18;

    // Initialize the total supply and allocate all tokens to the contract creator
    constructor(){
        balanceOf[msg.sender] = totalSupply;
    }

    // Transfer tokens from the sender to the recipient, and emit the Transfer event
    function transfer(address recipient, uint amount) external returns (bool) {
        require(balanceOf[msg.sender] >= amount);
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
        
    }

    // Approve the spender to spend the specified amount of tokens on behalf of the owner, and emit the Approval event
    function approve(address spender, uint amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;

    }

    // Transfer tokens from the sender to the recipient, and emit the Transfer event
    function transferFrom(
        address sender,
        address recipient,
        uint amount
    ) external returns (bool) {
        require(balanceOf[sender] >= amount);
        require(allowance[sender][msg.sender] >= amount);
        balanceOf[sender] -= amount;
        allowance[sender][msg.sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(sender,recipient,amount);
        return true;
    }

    
    // Mint new tokens and allocate them to the message sender
    function mint(uint amount) external {
        balanceOf[msg.sender] += amount;
        totalSupply += amount;
        emit Transfer(address(0),msg.sender, amount);
   
    }

    // Burn tokens from the message sender
    function burn(uint amount) external {
        uint accountBalance = balanceOf[msg.sender];
        require(accountBalance >= amount,"ERC20: burn amount exceeds balance");
        balanceOf[msg.sender] -= amount ;
        totalSupply -= amount;
        emit Transfer(msg.sender,address(0), amount);
    }

}

// token 2 with name comp163_2 and symbol comp2
contract token2 is IERC20 {
    // Specify the total supply of tokens
    uint public totalSupply = 100;
  
    // Create a mapping to keep track of balances
    mapping (address => uint) public balanceOf;
 
    // Create a mapping to keep track of allowances
    mapping (address => mapping(address => uint)) public allowance;

    // Specify the name of the token
    string public name = "comp163_2";

    // Specify the symbol of the token
    string public symbol = "comp2";

    // Specify the number of decimals for the token
    uint public decimals = 18;

    // Initialize the total supply and allocate all tokens to the contract creator
    constructor(){
        balanceOf[msg.sender] = totalSupply;
    }

    // Transfer tokens from the sender to the recipient, and emit the Transfer event
    function transfer(address recipient, uint amount) external returns (bool) {
        require(balanceOf[msg.sender] >= amount);
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
        
    }

    // Approve the spender to spend the specified amount of tokens on behalf of the owner, and emit the Approval event
    function approve(address spender, uint amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;

    }

    // Transfer tokens from the sender to the recipient, and emit the Transfer event
    function transferFrom(
        address sender,
        address recipient,
        uint amount
    ) external returns (bool) {
        require(balanceOf[sender] >= amount);
        require(allowance[sender][msg.sender] >= amount);
        balanceOf[sender] -= amount;
        allowance[sender][msg.sender] -= amount;
        balanceOf[recipient] += amount;
        emit Transfer(sender,recipient,amount);
        return true;
    }

    
    // Mint new tokens and allocate them to the message sender
    function mint(uint amount) external {
        balanceOf[msg.sender] += amount;
        totalSupply += amount;
        emit Transfer(address(0),msg.sender, amount);
   
    }

    // Burn tokens from the message sender
    function burn(uint amount) external {
        uint accountBalance = balanceOf[msg.sender];
        require(accountBalance >= amount,"ERC20: burn amount exceeds balance");
        balanceOf[msg.sender] -= amount ;
        totalSupply -= amount;
        emit Transfer(msg.sender,address(0), amount);
    }

}
