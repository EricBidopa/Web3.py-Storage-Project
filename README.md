# Web3.py-Storage-Project
Simple Storage Project
#This is a Solidity smart contract called SimpleStorage. Let's break down what it does:

#Variables
favoriteNumber: A uint256 variable that stores a favorite number.
favoriteBool: A bool variable that stores a favorite boolean value.
People: A struct that contains a uint256 favorite number and a string name.
people: An array of People structs.
nameToFavoriteNumber: A mapping from string to uint256.
#Functions
store(uint256 _favoriteNumber): A function that takes a uint256 parameter _favoriteNumber
and stores it in the favoriteNumber variable.
retrieve(): A view function that returns the value stored in the favoriteNumber variable.
addPerson(string memory _name, uint256 _favoriteNumber): A function that creates a new People 
struct with the given _name and _favoriteNumber values, pushes it to the people array, and adds the 
_favoriteNumber value to the nameToFavoriteNumber mapping using _name as the key.
This contract essentially serves as a simple storage system that allows you to store and retrieve a 
single uint256 value and also store a list of People structs with their favorite numbers and names.
