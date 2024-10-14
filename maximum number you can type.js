var canBeTypedWords = function(text, brokenLetters) {
    let parts = text.split(" ");
    let count =0;
    
    for(let i =0; i<parts.length;i++){
        let cantype = true;
        let x = parts[i]
        for(let j =0; j< brokenLetters.length;j++){
            if(x.includes(brokenLetters[j])){
                cantype = false;
                break;
            }
        }
        if(cantype){
            count++;
        }
    }
    return count;
};