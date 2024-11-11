var findJudge = function(n, trust) {
    let trustScores = Array(n + 1).fill(0);

    for (let i = 0; i < trust.length; i++) {
        trustScores[trust[i][0]]--;
        trustScores[trust[i][1]]++;
    }

    for (let i = 1; i <= n; i++) {
        if (trustScores[i] === n - 1) {
            return i;
        }
    }

    return -1;
};
