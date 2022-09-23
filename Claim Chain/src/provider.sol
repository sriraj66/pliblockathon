// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract ProviderModule{
    address provider=0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;

    struct Provider{
        string name;
        string hospital;
        string place;
        string country;
        string state;
        string city;
        uint256 pincode;
        string email;

        string ENT;
        string ED;
        string AT;
        string HI;

    }
    Provider user;
    bytes32 hash;
    event log(uint Bolck,uint TIME);


    modifier condition(){
        require(msg.sender == provider,"Provider Only Acessable!!");
        _;
    }
    function getData(string memory _name,string memory _hospital,string memory _place,string memory _contry,string memory _state,string memory _city,uint256 _pincode,string memory _email) public condition returns(bool){
        user.name = _name;
        user.hospital = _hospital;
        user.place = _place;
        user.country = _contry;
        user.state = _state;
        user.city = _city;
        user.pincode = _pincode;
        user.email = _email;
        return true;
    }

    function generateHash()public condition returns(bytes32){
        hash = keccak256(abi.encodePacked(user.name,user.hospital,user.place,user.country,user.state,user.city,uint256(user.pincode),user.email));
        
        return hash;
    }
}