/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    argumentList = [...args]
    return argumentList.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
