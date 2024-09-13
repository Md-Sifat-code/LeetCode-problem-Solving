var addDigits = function(num) {
    let main = num.toString().split('');
    while (main.length > 1) {
        let sum = 0;
        for (let i = 0; i < main.length; i++) {
            sum += parseInt(main[i]);
        }
        main = sum.toString().split('');
    }

    return parseInt(main[0]);
};