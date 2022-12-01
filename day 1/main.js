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

	// Printing the elf with the most calories
	let most = 0;
	elfs.forEach((elf) => {
		if (elf > most) {
			most = elf;
		}
	});

	console.log(
		"The elf carrying the most calories is carrying " + most + " calories"
	);
});
