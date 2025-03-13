const fs = require("fs");

console.log("---Part 1---");

let result = 0;

let input = JSON.parse(fs.readFileSync("./input.txt").toString());

result = addNumbers(input);

function addNumbers(input) {
	console.log(input);
	let value = 0;

	// Array
	if (Array.isArray(input)) {
		for (let i = 0; i < input.length; i++) {
			let elem = input[i];

			if (!Number.isFinite(elem)) {
				value += addNumbers(elem);
				continue;
			}

			value += elem;
		}
		return value;
	}

	for (key in input) {
		if (!Number.isFinite(input[key])) {
			value += addNumbers(input[key]);
			continue;
		}
		value += input[key];
	}

	return value;
}

console.log("Result: " + result);
