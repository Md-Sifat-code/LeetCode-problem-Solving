var countNodes = function(root) {
    if (root === null) {
        return 0;
    }
    return 1 + countNodes(root.left) + countNodes(root.right);
};
