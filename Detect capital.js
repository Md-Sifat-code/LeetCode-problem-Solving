var detectCapitalUse = function(word) {
    let charecter ='';
    let count  = 0;
    for( let i = 0; i<word.length; i++){
        charecter = word.charAt(i);
        if(charecter == charecter.toUpperCase()){
            count++;
        }
    }
    if (count === word.length || count === 0 || (count === 1 && word.charAt(0) === word.charAt(0).toUpperCase())) {
        return true;
    } else {
        return false;
    }
};