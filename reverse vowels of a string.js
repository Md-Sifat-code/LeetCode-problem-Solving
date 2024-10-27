var reverseVowels = function(s) {
    const vowels = "aeiouAEIOU";
    let start = 0;
    let end = s.length - 1;
    const arr = s.split('');

    while (start < end) {
        if (!vowels.includes(arr[start])) {
            start++;
            continue;
        }
        
        if (!vowels.includes(arr[end])) {
            end--;
            continue;
        }

        [arr[start], arr[end]] = [arr[end], arr[start]];
        start++;
        end--;
    }

    return arr.join('');
};
