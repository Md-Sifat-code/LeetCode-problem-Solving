var isSubsequence = function(s, t) {
    let i =0;
    if(s.length==0 && t.length==0){
        return true;
    }
    for(let j =0; j<t.length;j++){
        if(s[i]==t[j]){
            i++
        }
        if(i==s.length){
            return true;
        }
    }
    return false;
};
//  this is a java script problem