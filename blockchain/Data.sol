// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SampleContract {
    
    struct Patient {
        string data;
        address id;
    }
    mapping (address => Patient) public myMap;

    function set(address _addr, string memory data) public {
        Patient storage newPatient = myMap[_addr];
        newPatient.id = _addr;
        newPatient.data = data;
    }
    
    function get(address _addr) public view returns (Patient memory) {
        return myMap[_addr];
    }
}