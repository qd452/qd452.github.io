---
layout: post
title:  "Eloquent JavaScript Notes"
date:   2019-05-13 23:58 +0800
categories: JavaScript notes JS 
---

## Table of Contents

{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

## Chapter 1. Values, Types, and Operators

### Arithmetic

```js
console.log(5/2);  // 2.5
console.log(5%2);  // 1
console.log(-1%3);  // -1, unlike in python, it will be 2
console.log(Math.floor(5/2));  // which is the same as // in python 
```

### Special Number

- `Infinity` 
- `-Infinity`
- `NaN`: `0/0`
    + `console.log(Infinity - Infinity);  // -> NaN`
    + `console.log(Infinity + Infinity); // -> Infinity`

### Strings

- newlines (the characters you get when you press enter) can be included without escaping only when the string is quoted with backticks (`) ?
- Backtick-quoted strings, usually called *template literals*. `` `i'm ${100 / 2}` `` will give " i'm 50"
    + ${}

### Unary Operators

- `typeof`: produces a **string value** naming the type of the value you give it
    ```js
    console.log(typeof 4.5)  // → number
    console.log(typeof 4.5 === "number"). // → true
    console.log(typeof "x") // → string
    ```

### Comparison

- uppercase letters are always “less” than lowercase ones, so "Z" < "a", which is according to ascii table i think.
- `console.log(NaN == NaN). // → false`

### Logical Operator

- `&&`
- `||`
- `!`
    + `console.log(!true) // -> false`
- `||` has the lowest precedence, then comes `&&`, then the comparison operators (``` > ```, ``==``, and so on), and then the rest.
    + `console.log(1 + 1 == 2 && 10 * 10 > 50) // -> true`
-  conditional operator (or sometimes just the ternary
    +  `console.log(true ? 1 : 2); // -> 1`

### Empty Values

- `null`
- `undefined`

`console.log(8 * null); // -> 0`
`console.log(8 * undefined); // -> NaN`
`console.log(typeof a ==='undefined'); // -> true`


### Automatic type conversion


the same as python
```js
console.log("5" - 1)
// → 4
console.log("5" + 1)
// → 51
console.log("five" * 2)
// → NaN
```

- when `null` or `undefined` occurs on either side of the operator, it produces true only if both sides are one of `null` or `undefined`.
    ```js
    console.log(null == undefined);
    // → true
    console.log(null == 0);
    // → false
    ```
- `===` and `!==`. The first tests whether a value is precisely equal to the other, and the second tests whether it is not precisely equal.

### Short-circuiting of logical operators

the same as python
```js
console.log(null || "user")
// → user
console.log("Agnes" && "user")
// → user
```
```py
a = "Agnes" and "user" # a="user"
a = "Agnes" or "user" # a="Agnes"
```


## Chapter 2. Program Structure

### Bindings

Binding, is variable

```js
let one = 1, two = 2;
```

### Binding Names

Binding name must not start with a digit. A binding name may include dollar signs ($) or underscores (_)

### The environment

The collection of bindings and their values that exist at a given time is called the environment. 

### Return Values

- `Math.max()` == max
- `Math.min()` == min
- `Math.pow(2, 3)` == 2**3
- `Number()` converts value to number. similar functions called `String` and `Boolean` that convert values to those Types
- `Number.isNaN` function returns true only if the argument it is given is NaN.

### While loops

a do loop always executes its body at least once
```js
let yourName;
do {
  yourName = prompt("Who are you?");
} while (!yourName);
console.log(yourName);
```

### Updating bindings succinctly

- `c += 1`, `c -= 1`
- `c++`, `c--`

### Switch

```js
switch (prompt("What is the weather like?")) {
  case "rainy":
    console.log("Remember to bring an umbrella.");
    break;
  case "sunny": # when case is 'sunny', it will execute until break
    console.log("Dress lightly."); // NOTE here don't have break
  case "cloudy":
    console.log("Go outside.");
    break;
  default:
    console.log("Unknown weather type!");
    break;
}
```

### Binding name Capitalization

- `fuzzyLittleTurtle`
- In a few cases, such as the `Number` function, the first letter of a binding is also capitalized. This was done to mark this function as a **constructor**. 

## Chapter 3. Functions

### Defining a function

```js
const foo = function(x) {
    return x * x;
};
```

A `return `keyword without an expression after it will cause the function to return `undefined`.

The `return` statement is affected by **Automatic semicolon insertion (ASI)**

```js
return
a+b;
```

is transformed by ASI into 
```js
return;
a+b;
```

### Bindings and scopes

- Bindings created for function parameters or declared inside a function can be referenced only in that function, so they are known as **local bindings**.

#### Good link to explain `var` VS `let` VS `const`


var VS let VS const

* var: 
  - function scoped
  - undefined when accessing a variable before it's declared

* let: 
  - block scoped
  - ReferenceError when accessing a variable before it's declared

* const:
  - block scoped
  - ReferenceError when accessing a variable before it's declared
  can't be reassigned

### Nested scope - lexical scoping

### Functions as values

### Declaration notation

```JavaScript
function foo(x) {
    return x * x;
} // very python style
```
GOOD THING about this Declaration is that the preceding code works, even though the function is defined *below* the code that uses it.

AND, in this case, no `;` is needed, while the others function Declaration needs.  

### Arrow Functions

```JavaScript
let foo = (x) => {
    return x * x;
};
const square1 = (x) => { return x * x; };
const square2 = x => x * x;
const bar = () => {console.log("bar"); };
```

### Optional Arguments

number of Arguments
- when pass too many, the extra ones are ignored
- when pass too few, the missing ones assigned with `undefined`

```js
const minus = (a,b) =>{
    if (b === undefined) return -a;
    else return a - b;
}
```

### Closure

- What happens to local bindings when the function call that created them is no longer active? -> Still alivce
- This feature—being able to reference a specific instance of a local binding in an enclosing scope—is called *closure*.

```js
function wrapValue(n) {
  let local = n;
  return () => local;
}

function multiplier(factor) {
  return number => number * factor;
}
```

## Chapter 4. Data Structures: Objects and Arrays

### Data set

### Properties

- Almost all JavaScript values have properties. The exceptions are `null` and `undefined`.

  ```js
  console.log(null.length); // TypeError: Cannot read property 'length' of null (line 1 in function eval)

  console.log(NaN.length); // undefined
  ```

- The elements in an array are stored as the array’s properties, using numbers as property names. 

### Methods

- Properties that contain functions are generally called methods of the value they belong to, as in “toUpperCase is a method of a string”

#### Array Common Methods

- `Array​.prototype​.includes()` determines whether an array includes a certain value among its entries, returning true or false as appropriate.
- `push` is `append`
- `pop()` is `pop()`
- `shift()` is `pop(0)`. For `shift`, if array is empty, return `undefined`. For python, it will raise `IndexError: pop from empty list`
- When creating a 1D array of length N filled with 0:
  ```js
  let N = 3;
  let dp = Array(N).fill(0);
  console.log(dp); // -> Array [0, 0, 0]
  ```
- `fill(value[, start[, end]])`
- When creating a 2D array of length M*N, filled with 0:
  ```js
  let M=2, N=4;
  let dp = Array.from(Array(M), () => new Array(N).fill(0));
  console.log(dp);
  // -> Array [Array [0, 0, 0, 0], Array [0, 0, 0, 0]]
  ```

- `Array.from()` method creates a new, shallow-copied Array instance from an array-like or iterable object.
  + Convert string to array
    * `Array.from('foo')` will yield `Array ["f", "o", "o"]`
    * while `Array('foo')` will yield `Array ["foo"]`
- `indexOf()` is `index()`. It return the first index at which the given element can be found in the array. However
  + For `indexOf`, return -1 if not found
  + For `index` in Py, raise `ValueError`
- `a.reverse()` is `a[::-1]` in Python
- `arr.slice([begin[, end]])` is the array indexing, like `a[begin:end]` in Python
  + `arr.slice()` is `arr[:]`
- To sort array in ascending order
  + `a.sort((x,y)=>x-y);` 
  + `a.sort()` in Python
- Insert at the beginning, if `a=[3,4,5]`
  + `a.unshift(4,5)` will return 5, which is the new length of array after `unshift`; and now the array becomes `[4,5,3,4,5[`
  + `a.insert(0,5); a.insert(0,4)` in python, or `[4,5] + arr`
- `splice`
  + `var arrDeletedItems = array.splice(start[, deleteCount[, item1[, item2[, ...]]]])`
  + delete by index, for example `idx=2`
    * `arr.splice(2,1)`
    * while in python, its more straightforward, `del arr[2]`
  + insert item at certain index, for example `idx=4, val-5`
    * `arr.splice(4,0,5)`
    * while in python, just use `arr.insert(4,5)`
- `concat`
  + `a = b.concat(c);`
  + `a = b + c` in python
  + Note in JS, for string, can directly use `+` to concat strings. But cannot use `+` to concat array
    ```js
    let a1 = [1,2], a2 = [3,4];
    console.log(a1+a2); // -> "1,23,4"
    ```
- Note, in JS, index can also be negative, which is the same as in Python.


### Objects

- Objects are created in the same way as `dictionary` in python. BUT property names no need to add "" unless it contains space.
- Each property has a name followed by a colon and a value.
- `delete` remove the named property of Object
- `in` tells you whether that object has a property with that name
- `Object.keys()` and `Object.values()`

```js
let obj = {x: 0, y: 0, z: 2};
console.log(Object.keys(obj));  // → ["x", "y", "z"]
console.log(Object.values(obj));  // → [0, 0, 2]
```

- `Object.assign()` like `update` in Python
-  If you evaluate `typeof []`, it produces "object"

### Mutability

- numbers, strings, and Booleans, are all immutable

### Strings and their properties

- Values of type string, number, and Boolean are **not objects**, and though the language doesn’t complain if you try to set new properties on them, it doesn’t actually store those properties. As mentioned earlier, such values are **immutable** and cannot be changed.
  ```js
  let kim = "Kim";
  kim.age = 88;
  console.log(kim.age);
  // → undefined
  ```
- `slice()`
- `indexOf()`
- `trim()` is `strip()`
- `trimEnd()` or `trimRight()` is `rstrip()`
- `trimStart()` or `trimLeft()` is `lstrip()`
- `padStart()`
  + `str.padStart(targetLength [, padString])`
- `split()`  is the same as in python
- `repeat(N)`, in python `*N`
  + `let a = 'a'; a.repeat(3);` results `"aaa"`
  + in py, `a='a'; a*3` results the same

### Rest parameters

- When such a function is called, the rest parameter is bound to an array containing all further arguments.
- It is the same as `*args` in Python

```js
let numbers = [5, 1, 7];
console.log(Math.max(...numbers));  // -> 7
console.log(Math.max(numbers));  // -> NaN
```

### The Math object

- `Math.sqrt()`
- `Math.random()` from [0,1)
- `Math.floor()`, `Math.ceil()`, `Math.round`, `Math.abs()`

### Destructuring assignment

The **destructuring assignment** syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment

#### Array destructuring

```js
var x = [1, 2, 3, 4, 5];
var [y, z] = x;
// y=1, z=2
```

while in Python

```py
x = [1, 2, 3, 4, 5]
y, z, *_ = x
# y=1, z=2
# y,z = x will raise ValueError: too many values to unpack (expected 2)
```

1. default value

```js
var a, b;
[a=5, b=7] = [1];
// a=1, b=7
```

2. swapping values

`[a, b] = [b, a];`

3. ignoring some values

```js
var x = [1,2,3,4];
var [m, ,n] = x;
console.log(m, n); // 1, 3
```
Note, here is equivalent to `m, _, n, *_ = x` in Python. Note `m, *_, n = x`!!

4. get second last element from array

```js
const [x] = arr.slice(-2);
```

5. Assigning the rest of an array to a variable

```js
var x = [1,2,3,4];
var [a, ...b] = x;
console.log(a, b); // 1, [2, 3, 4]
```

#### Object destructuring

1. basic assignment

```js
var o = {p: 42, q: true};
var {p, q} = o;
```

2. assignment to new variable names

```js
var o = {p: 42, q: true};
var {p: foo, q: bar} = o;
console.log(foo, bar); // -> 42, true
```

3. Setting a function parameter's default value

ES2015 version
```js
function drawES2015Chart({size = 'big', coords = {x: 0, y: 0}, radius = 25} = {}) {
  console.log(size, coords, radius);
  // do some chart drawing
}

drawES2015Chart({
  coords: {x: 18, y: 30},
  radius: 30
});
```

4. Unpacking fields from objects passed as function parameter
[TODO]

5. Computed object property names and destructuring

```js
let key = 'z';
let {[key]: foo} = {z: 'bar'};
console.log(foo); // "bar"
```

### JSON

- object to JSON: `JSON.stringify()`, equivalent to `json.dumps()` in python
- JSON to object: `JSON.parse()`, equivalent to `json.loads()` in python


























