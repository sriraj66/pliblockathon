// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Insurance{
    address Provider=0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;

    struct Insure{
        string name;
        uint256 adhar_num;
        uint256 mobile;
        string email;
        string dob;
        string father_name;
        string mother_name;
        string place;
        string status;
        string spouse;
        string qulification;
        string pob;
        string pan;
        string occupation;
        uint256 anual_income;
        string emp;
        uint256 service;
    }
    bytes32 hash;
    bytes32 newhash;

    Insure user;
    modifier condition(){
        require(msg.sender==Provider,"only Provider can access!!");
        _;
    }
    event log(uint Bolck,uint TIME);
// string memory _occupation,uint256 _anual_income,string memory _emp,uint256 _service
// string memory _qulification,string memory _pob,string memory _pan
    function getData1(string memory _name,uint256 _adhar,uint256 _mobile,string memory _email,string memory _dob,string memory _father_name,string memory _mother_name, string memory _place,string memory _status,string memory _spouse)  public condition returns(bool){

        user.name=_name;
        user.adhar_num = _adhar;
        user.mobile = _mobile;
        user.email = _email;
        user.dob= _dob;
        user.father_name=_father_name;
        user.mother_name = _mother_name;
        user.place = _place;
        user.status = _status;
        user.spouse = _spouse;
        emit log(block.number,block.timestamp);
        return true;
    }
    function getData2(string memory _qulification,string memory _pob,string memory _pan,string memory _occupation,uint256 _anual_income,string memory _emp,uint256 _service) public condition returns(bool){
        user.qulification = _qulification;
        user.pob = _pob;
        user.pan = _pan;
        user.occupation = _occupation;
        user.anual_income = _anual_income;
        user.emp = _emp;
        user.service = _service;

        emit log(block.number,block.timestamp);

        return true;

    }

    function generateHash() public condition returns(bytes32){
        hash = keccak256(abi.encodePacked(user.name,uint256(user.adhar_num),uint256(user.mobile),user.email,user.dob,user.father_name,user.mother_name,user.pan,user.emp,user.spouse,user.status,user.service));
        newhash = keccak256(abi.encodePacked(bytes32(hash),user.qulification,user.pob,user.place,user.occupation));
        return hash;
    }

}