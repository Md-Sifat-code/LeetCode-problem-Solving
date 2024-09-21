var findContentChildren = function(g, s) {
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);

    let contentChildren = 0;
    let i = 0; 
    let j = 0; 
    while (i < g.length && j < s.length) {
        if (s[j] >= g[i]) { 
            contentChildren++;
            i++;
        }
        j++;
    }

    return contentChildren;
};