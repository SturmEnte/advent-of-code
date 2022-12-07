const fs = require('fs');
const { join } = require('path');

let tree = {};
let path = [];

fs.readFile(join(__dirname, 'input.txt'), 'utf8', (err, data) => {
    if (err) {
        console.log(err);
        return;
    }

    data.split('\r\n').forEach((line) => {
        let split = line.split(' ');

        if (line.startsWith('$')) {
            if (split[1] == 'cd') {
                cd(split[2]);
            }
            return;
        }

        let name = split[1];
        if (split[0] == 'dir') {
            return;
        }

        let size = Number(split[0]);
        let copy = path;
        copy.push(name);
        tree = set(copy, size, tree);
    });

    console.log(tree);
});

function cd(newPath) {
    if (newPath == '..') {
        path.pop();
    } else if (newPath != '/') {
        path.push(newPath);
    }
}

// Recursion
function get(path, obj) {
    let c = path.shift();
    let b = obj[c];

    if (path.length == 0) {
        return b;
    }

    return x(path, b);
}

function set(path, val, obj) {
    let c = path.shift();
    let b = obj[c];

    if (!b) {
        b = {};
    }

    if (path.length == 0) {
        obj[c] = val;
        return obj;
    }

    obj[c] = set(path, val, b);
    return obj;
}