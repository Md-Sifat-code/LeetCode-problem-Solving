var countSegments = function(s) {
    let segments = s.split(" ").filter(sifat => sifat !== "");
    return segments.length;
};
