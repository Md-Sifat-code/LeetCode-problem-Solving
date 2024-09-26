function reverseStr(s, k) {
    let result = "";
    
    for (let i = 0; i < s.length; i += 2 * k) {
        let part = s.slice(i, i + 2 * k);
        let reversedPart = part.slice(0, k).split('').reverse().join('');
        result += reversedPart + part.slice(k);
    }
    
    return result;
}