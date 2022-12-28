In JavaScript, = is used for assignment, == is used for comparison, and === is used for strict comparison.

Here is an example of how these operators might be used:

```script
let x = 5; // assignment

if (x == 5) { // comparison
  console.log("x is equal to 5");
}

if (x === 5) { // strict comparison
  console.log("x is strictly equal to 5");
}
```
The difference between == and === is that == performs type coercion before making the comparison, while === does not. This means that == will consider two values equal if they have the same value after any necessary type conversions have been applied, while === will only consider two values equal if they have the same value and are of the same type.

 ```JS
console.log(1 == "1");  // true
console.log(1 === "1"); // false

console.log(null == undefined);  // true
console.log(null === undefined); // false
```
It is generally recommended to use === for comparisons in JavaScript, as it can help avoid unexpected behavior due to type coercion.
