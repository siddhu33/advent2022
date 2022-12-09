function rope(length) {
    let knots = [];
    for (let i = 0; i < length; i++) {
        knots.push([0, 0]);
    }
    return knots;
}

function move_rope(direction, rope) {
    new_head = step_head(direction, rope[0]);
    rope[0] = new_head;
    for (let idx = 1; idx < rope.length; idx++) {
        new_tail = step_tail(rope[idx - 1], rope[idx]);
        rope[idx] = new_tail;
    }
}

function step_head(direction, head) {
    if (direction === "U") {
        return [head[0], head[1] + 1];
    }
    else if (direction === "D") {
        return [head[0], head[1] - 1];
    }
    else if (direction === "R") {
        return [head[0] + 1, head[1]];
    }
    else if (direction === "L") {
        return [head[0] - 1, head[1]];
    }
}

function step_tail(new_head, tail) {
    const x_diff = new_head[0] - tail[0];
    const y_diff = new_head[1] - tail[1];
    if (Math.abs(x_diff) > 1 || Math.abs(y_diff) > 1) {
        if (x_diff === 0) {
            return [tail[0], tail[1] + y_diff / 2]
        } else if (y_diff === 0) {
            return [tail[0] + x_diff / 2, tail[1]]
        } else {
            let diff = [0, 0];
            if (Math.abs(x_diff) > 1 && Math.abs(y_diff) == 1) {
                diff = [x_diff / 2, y_diff]
            } else if (Math.abs(x_diff) === 1 && Math.abs(y_diff) > 1) {
                diff = [x_diff, y_diff / 2];
            } else if (Math.abs(x_diff) > 1 && Math.abs(y_diff) > 1) {
                diff = [x_diff / 2, y_diff / 2];
            }
            return [tail[0] + diff[0], tail[1] + diff[1]];
        }
    } else {
        return tail;
    }
}

const myRope = rope(10);
let start = -5;
labels = []
while (start < 5) {
    labels.push(start);
    start = start + 1;
}
const myChart = new Chart(document.getElementById('main'), {
    type: "scatter",
    data: {
        datasets: [{
            label: "Rope",
            data: myRope.map(knot => ({ x: knot[0], y: knot[1] }))
        }]
    },
    options: {
        scales: {
            y: {
                min: -15,
                max: 15
            },
            x: {
                min: -15,
                max: 15
            }
        }
    }
});

window.addEventListener("keydown", function (event) {
    if (event.defaultPrevented) {
        return; // Do nothing if the event was already processed
    }

    switch (event.key) {
        case "ArrowDown":
            move_rope("D", myRope);
            myChart.data.datasets[0].data = myRope.map(knot => ({ x: knot[0], y: knot[1] }))
            myChart.update()
            break;
        case "ArrowUp":
            move_rope("U", myRope);
            myChart.data.datasets[0].data = myRope.map(knot => ({ x: knot[0], y: knot[1] }))
            myChart.update()
            break;
        case "ArrowLeft":
            move_rope("L", myRope);
            myChart.data.datasets[0].data = myRope.map(knot => ({ x: knot[0], y: knot[1] }))
            myChart.update()
            break;
        case "ArrowRight":
            move_rope("R", myRope);
            myChart.data.datasets[0].data = myRope.map(knot => ({ x: knot[0], y: knot[1] }))
            myChart.update()
            break;
        default:
            return; // Quit when this doesn't handle the key event.
    }

    event.preventDefault();

}, true);
console.log("Loaded!");
