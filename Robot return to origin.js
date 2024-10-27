var judgeCircle = function(moves) {
    let vertical = 0; // Tracks 'U' and 'D' moves
    let horizontal = 0; // Tracks 'L' and 'R' moves

    for (let i = 0; i < moves.length; i++) {
        if (moves[i] === 'U') vertical += 1;
        else if (moves[i] === 'D') vertical -= 1;
        else if (moves[i] === 'L') horizontal += 1;
        else if (moves[i] === 'R') horizontal -= 1;
    }

    return vertical === 0 && horizontal === 0;
};