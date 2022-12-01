const fs = require("fs");
const { join } = require("path");

let elfs = [0];

fs.readFile(join(__dirname, "input.txt"), "utf8", (err, data) => {
	if (err) {
		console.log(err);
		return;
	}

	// Add the amount of calories for each elv togethre
	let i = 0;
	let splitData = data.split("\n");
	for (let j = 0; j < splitData.length; j++) {
		let data = splitData[j];

		if (data == "\r") {
			i++;
			elfs.push(0);
			continue;
		}

		elfs[i] += Number(data);
	}

	// Sort the array
	elfs = elfs.sort((a, b) => {
		return b - a;
	});

	// Print psrt 1
	console.log(
		"The elf carrying the most calories is carrying",
		elfs[0],
		"calories"
	);

	// Print part 2
	console.log(
		"The top three elfs combined carry",
		elfs[0] + elfs[1] + elfs[2],
		"calories"
	);
});
