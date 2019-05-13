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

























