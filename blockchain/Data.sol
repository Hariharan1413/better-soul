// SPDX-License-Identifier: MIT

pragma solidity >=0.5.0 < 0.9.0;

contract Records {
    struct Patient {
        string data;
        address id;
    }

    address[] public doctorList;

    mapping (address => Patient) patientInfo;
    uint numberOfPatients = 0;

    // modifier onlyDoctor() {
    //     for (uint i=0; i < doctorList.length; i++) {
    //         if (msg.sender == doctorList[i])
    //         require(msg.sender);
    //     }

    // }

    function getPatient(address _patientAddress) public view returns(address) {
        return _patientAddress;
    }

    function addPatient(string memory _data, address _patientAddress) public {
        Patient storage newPatient = patientInfo[numberOfPatients];
        numberOfPatients++;
        newPatient.id = _patientAddress;
        newPatient.data = _data;
    }
}