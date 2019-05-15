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


