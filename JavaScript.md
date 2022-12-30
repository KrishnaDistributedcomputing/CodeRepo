## What are Native objects of javascripts

In JavaScript, native objects are objects that are built into the language and are always available for use. These objects are defined in the JavaScript specification and are implemented in JavaScript engines, such as the V8 engine used in Google Chrome and the Spider Monkey engine used in Mozilla Firefox.

Some examples of native objects in JavaScript include:

* Object: The base object type that provides a number of useful methods for working with objects, such as Object.create and Object.assign.
Array: An object type that represents an ordered collection of values. Arrays have a number of useful methods for working with their elements, such as push, pop, and slice.
* String: An object type that represents a sequence of characters. Strings have a number of useful methods for working with and manipulating their contents, such as split, substring, and toLowerCase.
* Number: An object type that represents numeric values.
* Boolean: An object type that represents a boolean value (true or false).
* Function: An object type that represents a function. Functions have a number of useful properties and methods, such as apply, bind, and call.

These are just a few examples of the many native objects that are available in JavaScript. You can find a complete list of native objects in the JavaScript specification or in the documentation for your JavaScript runtime.

### For example Number has number of predefined functions.

![image](https://user-images.githubusercontent.com/117572861/210025054-8bfd3fa6-295d-4e83-9bef-e2b20e5188cb.png)

## = Vs == Javascript Operator

In JavaScript, = is used for assignment, == is used for comparison, and === is used for strict comparison.

Here is an example of how these operators might be used:

 ```JS
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
