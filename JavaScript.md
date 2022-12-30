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

![image](https://user-images.githubusercontent.com/117572861/210025185-c00150d5-fe93-4acd-8bd4-7b6eff0c03f7.png)

![image](https://user-images.githubusercontent.com/117572861/210025326-09d33e8d-4681-4d09-a80c-6a98a34f93cb.png)

![image](https://user-images.githubusercontent.com/117572861/210025338-fc1ed154-2d69-4664-b7bc-038c39e8855b.png)


### Here is an example of using the String object in JavaScript:
```JS
// Create a new string object
const str = new String('hello world');
```
```JS
// Use the toUpperCase method to convert the string to uppercase
const uppercaseStr = str.toUpperCase();
```

```JS
// Print the original and uppercase strings to the console
console.log(str); // Outputs: "hello world"
console.log(uppercaseStr); // Outputs: "HELLO WORLD"
```

To test this example in a browser, you can open the JavaScript console in your browser and paste the code there. When you run the code, it will create a new String object called str with the value 'hello world', and then use the toUpperCase method to convert the string to uppercase. Finally, it will print the original and uppercase strings to the console.

You should see the following output in the console:

```JS
"hello world"
"HELLO WORLD"
```

### What are the native objects in HTML 

In HTML (HyperText Markup Language), native objects are objects that are built into the language and are always available for use when writing HTML documents. These objects are defined in the HTML specification and are implemented in web browsers, such as Google Chrome, Mozilla Firefox, and Safari.

Some examples of native objects in HTML include:

* Document: The root object of the HTML document. It represents the entire HTML document and provides methods and properties for accessing and manipulating the document's content and structure.
* Element: An object that represents an HTML element in the document. Elements have properties and methods for accessing and modifying their attributes, content, and style.
* NodeList: An object that represents a list of nodes (elements, text, comments, etc.) in the document. NodeLists have methods for accessing and manipulating their elements, such as item and forEach.
* Event: An object that represents an event that has occurred in the document, such as a mouse click or a key press. Events have properties and methods for accessing and handling the event data.

These are just a few examples of the many native objects that are available in HTML. You can find a complete list of native objects in the HTML specification or in the documentation for your web browser.


### Sample HTML Code 

```HTML
<!DOCTYPE html>
<html>
<head>
  <title>My HTML Page</title>
</head>
<body>
  <h1>Hello World!</h1>
  <p>Click the button below to change the text of the heading:</p>
  <button id="btn">Change Heading</button>
  <script>
    // Get a reference to the button element
    const btn = document.getElementById('btn');

    // Add an event listener to the button that changes the text of the heading
    btn.addEventListener('click', () => {
      const h1 = document.querySelector('h1');
      h1.textContent = 'Text Changed!';
    });
  </script>
</body>
</html>
```
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
