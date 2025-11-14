// Last updated: 11/14/2025, 8:47:54 AM
function expect(val) {
    return {
        toBe: function(expected) {
            if (val === expected) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: function(expected) {
            if (val !== expected) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    };
}

// Example usage:
try {
    console.log(expect(5).toBe(5)); // true
    console.log(expect(5).notToBe(10)); // true
    console.log(expect(5).toBe(10)); // Throws "Not Equal"
} catch (error) {
    console.error(error.message);
}
