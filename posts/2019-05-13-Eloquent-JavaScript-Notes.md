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
  + `arr.indexOf(searchElement[, fromIndex])`
- `findIndex()` method returns the index of the first element in the array that satisfies the provided testing function. Otherwise, it returns -1, indicating that no element passed the test.
  + `arr.findIndex(callback(element[, index[, array]])[, thisArg])`
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
- `some` like `any` in python
  + `arr.some(callback(element[, index[, array]])[, thisArg])`
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

## Chapter 5. Higher-Order Functions

### Higher-order functions

Functions that operate on other functions, either by taking them as arguments or by returning them, are called higher-order functions. 

```js
let arr = [{name: "ltr", count: 3}, {name: "rtl", count: 9}]
arr = [{name: "ltr", count: 3}];
let r = arr.reduce((x,y) => x.count<y.count ? y : x).name; // NOTE: here .name is outside of the reduce. If inside reduce will cause that when the arr is only size one, it directly returns the first Object.
console.log(r);
```

use `reduce` to find the maximum
```python
from functools import reduce
a=[1,2,3,4,5,4,3]
m = reduce(lambda x,y: x if x>y else y, a)
```

Can use it to find the key with max value
```python
c = {'a': 5, 'e': 3, 'b': 3, 'd': 1, 't': 2}
r= reduce(lambda x,y: x if c[x]>c[y] else y, c)
assert r == 'a'
```
However, there are other ways, https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

### Strings and character codes

JavaScript strings are encoded as a sequence of 16-bit numbers. These are called code units.

**UTF-16** **UTF-8**

https://javarevisited.blogspot.com/2015/02/difference-between-utf-8-utf-16-and-utf.html
https://stackoverflow.com/questions/496321/utf-8-utf-16-and-utf-32

> 1) UTF16 is not fixed width. It uses 2 or 4 bytes. Only UTF32 is fixed-width and unfortunately no one uses it.  Also, worth knowing is that Java Strings are represented using UTF-16 bit characters, earlier they use USC2, which is fixed width. 
> 2) You might think that because UTF-8 take less bytes for many characters it would take less memory that UTF-16, well that really depends on what language the string is in. For non-European languages, UTF-8 requires more memory than UTF-16.
> 3) ASCII is strictly faster than multi-byte encoding scheme because less data to process = faster.
> 
> Summary:
> - UTF-8: Variable-width encoding, backwards compatible with ASCII.  ASCII characters (U+0000 to U+007F) take 1 byte, code points U+0080 to U+07FF take 2 bytes, code points U+0800 to U+FFFF take 3 bytes, code points U+10000 to U+10FFFF take 4 bytes.  Good for English text, not so good for Asian text.
> - UTF-16: Variable-width encoding.  Code points U+0000 to U+FFFF take 2 bytes, code points U+10000 to U+10FFFF take 4 bytes.  Bad for English text, good for Asian text.
> - UTF-32: Fixed-width encoding.  All code points take four bytes.  An enormous memory hog, but fast to operate on.  Rarely used.


- `charCodeAt` method gives you a code unit, not a full character code. 
- `codePointAt` method, added later, does give a full Unicode character.


### Flat Array

In Python, `[y for x in arr for y in x]`

In JS, see [Ref](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)

```js
let arrays = [[1, 2, 3], [4, 5], [6]];
let r = arrays.reduce((x,y) => x.concat(y));
let r2 = arrays.flat();
console.log(r);
console.log(r2);
```

## Chapter 6. The Secret Life of Objects

### Encapsulation

- The core idea in object-oriented programming is to divide programs into smaller pieces and make each piece responsible for managing its own state.

### Methods

Methods are nothing more than properties that hold function values.

When a function is called as a method—looked up as a property and immediately called, as in `object.method()`—the binding called `this` in its body automatically points at the object that it was called on.

Note the difference between the function defined with `function` keyword & Arrow function
```js
let func = x => console.log(`${this.foo} is ${x}`);
func(1);
let obj = {foo:'obj-1', func};
obj.func(1); 
func = function(x) { console.log(`${this.foo} is ${x}`) };
func(1);
obj = {foo:'obj-1', func};
obj.func(1);
// undefined is 1
// undefined is 1
// undefined is 1
// obj-1 is 1
```

- For normal function, each function has it own `this` binding (whose value depends on the way it is called); and it cannot refer to the `this` of the **wrapping scope**
- While for arrow function, they don't bind their own `this` but can see `this` binding of the scope around them.

```js
function normalize() {
  console.log(this.coords.map(n => n / this.length));
}
normalize.call({coords: [0, 2, 3], length: 5});
// → [0, 0.4, 0.6]
```

#### More about normal function and arrow function

[MDN Ref](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

```js
var elements = [
  'Hydrogen',
  'Helium',
  'Lithium',
  'Beryllium'
];

// When the only statement in an arrow function is `return`, we can remove `return` and remove
// the surrounding curly brackets
elements.map(element => element.length); // [8, 6, 7, 9]

elements.map(({ length }) => length); // [8, 6, 7, 9]
```

Conclusion from [this](https://www.codementor.io/dariogarciamoya/understanding-this-in-javascript-with-arrow-functions-gcpjwfyuc):

> arrow functions are the best choice when working with closures or callbacks, but not a good choice when working with class/object methods or constructors.

### Prototypes

In addition to objects' set of properties, most objects also have a *prototype*. A *prototype* is another object that is used as a fallback source of properties.

- `toString()` method returns a string representing the object.
  + like `__str__()` in Python
  + `Object.prototype.toString()`
  ```js
  function Dog(name) {
    this.name = name;
  }
  var dog1 = new Dog('Gabby');
  Dog.prototype.toString = function dogToString() {
    return '' + this.name;
  }
  console.log(dog1.toString());
  // expected output: "Gabby"
  ```
- `Object.getPrototypeOf()` method returns the prototype (i.e. the value of the internal `[[Prototype]]` property) of the specified object.
  ```js
  console.log(Object.getPrototypeOf(Math.max) ==
              Function.prototype); // -> true
  console.log(Object.getPrototypeOf(Math) == Object.prototype);  // -> true
  console.log(Object.getPrototypeOf([]) ==
              Array.prototype);  // -> true
  ```

- 这里注意: `Object.prototype.toString()` 和   `Object.getPrototyeOf()` 在使用时的区别.
- `Object.create()` method creates a new object, using an existing object as the prototype of the newly created object.
  + `Object.create(proto, [propertiesObject])`
  ```js
  let protoRabbit = {
      speak(line) {
      console.log(`The ${this.type} rabbit says '${line}'`);
    }
  };
  let killerRabbit = Object.create(protoRabbit);
  console.log(Object.getPrototypeOf(killerRabbit) === protoRabbit);
  killerRabbit.type = "killer";
  killerRabbit.speak("SKREEEE!");
  // → The killer rabbit says 'SKREEEE!'
  ```

### Classes

```js
let protoRabbit = {
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
};
function makeRabbit(type) {
  let rabbit = Object.create(protoRabbit);
  rabbit.type = type;
  return rabbit;
}
let weirdRabbit = makeRabbit("weird");
console.log(weirdRabbit);
console.log(typeof weirdRabbit);
weirdRabbit.speak('haha');
/*
{type: "weird"}
object
The weird rabbit says 'haha'
*/
```

use `new`

```js
function Rabbit(type) {
  this.type = type;
}
Rabbit.prototype.speak = function(line) {
  console.log(`The ${this.type} rabbit says '${line}'`);
};

let weirdRabbit = new Rabbit("weird");
console.log(weirdRabbit);
console.log(typeof weirdRabbit);
weirdRabbit.speak('haha');
/*
Rabbit{type: "weird"}
object
The weird rabbit says 'haha'
*/
```

- distinction between the way a prototype is associated with a **constructor** (through its `prototype` property) and the way objects have a prototype (which can be found with `Object.getPrototypeOf`). The actual prototype of a constructor is Function.prototype since constructors are functions.Its prototype property holds the prototype used for instances created through it.

```js
console.log(Object.getPrototypeOf(Rabbit) ==
            Function.prototype);
// → true
console.log(Object.getPrototypeOf(weirdRabbit) ==
            Rabbit.prototype);
// → true
```

- `getPrototypeOf()` very like `type()` in Python

### Class Notation

- **`constructor()`** is `__init__()` in python

```js
class Rabbit {
  constructor(type) {
    this.type = type;
  }
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
}

let killerRabbit = new Rabbit("killer");
let blackRabbit = new Rabbit("black");
```

- Class declarations currently allow only *methods*—properties that hold functions—to be added to the prototype. [TODO]

### Overriding derived properties

```js
console.log([1, 2].toString());
console.log(Array.prototype.toString.call([1,2]));
```

### Maps

- `let dct = new Map();`
- The methods `set`, `get`, and `has` are part of the interface of the Map object.
- `keys()` method returns a new `Iterator` object that contains the keys for each element in the Map object in insertion order. The same for `values()`
  ```js
  var map1 = new Map();

  map1.set('0', 'foo');
  map1.set(0, 'bar');

  var iterator1 = map1.keys();
  let a = iterator1.next().value;
  let b = iterator1.next().value;
  console.log(a);
  console.log(b);
  console.log(a===b);
  console.log("1"==1);
  /*
  > "0"
  > 0
  > false
  > true
  */
  ```

#### Compare with Object

Note for Object, the difference between `in` and `hasOwnPorperty()`
```js
let obj = {x:1};
console.log(obj.hasOwnProperty("x"));
console.log("x" in obj);
console.log(obj.hasOwnProperty("toString"));
console.log("toString" in obj);
console.log(Object.keys(obj));
console.log(Object.values(obj));
delete obj.x; // delete 
/*
true
true
false
true
["x"]
[1]
*/
```

while For Map

```js
console.log(dct.has("x"));
let dct = new Map([["x",1]]); // note: how to give initialize it during declaration
console.log(dct.has("x"));
console.log(Array.from(dct.keys())); // note: Array.from()
console.log(Array.from(dct.values())); // note: Array.from()
dct.delete("x") // delete
```
#### Polymorphism

```js
Rabbit.prototype.toString = function() {
  return `a ${this.type} rabbit`;
};
console.log(String(blackRabbit));
// → a black rabbit
```
### Symbols

- property names are strings, and can also be symbols. Symbols are values created with the Symbol function. 
- Unlike strings, newly created symbols are unique—you cannot create the same symbol twice.

```js
let sym = Symbol("name");
console.log(sym == Symbol("name"));
// → false
Rabbit.prototype[sym] = 55;
console.log(blackRabbit[sym]);
// → 55
```

### The iterator interface

**Iterable Object** has a method named with the `Symbol.iterator` symbol (a symbol value defined by the language, stored as a property of the `Symbol` function).

Note that the 
- `next`, `value`, and `done` property names are plain strings, not symbols. 
- Only `Symbol.iterator` is an actual symbol.

```js
let okIterator = "OK"[Symbol.iterator]();
console.log(okIterator.next());
// → {value: "O", done: false}
console.log(okIterator.next());
// → {value: "K", done: false}
console.log(okIterator.next());
// → {value: undefined, done: true}
```

iterator has a `next()` method which returns an object with two properties: `value`, the next value in the sequence; and `done`, which is true if the last value in the sequence has already been consumed. If `value` is present alongside `done`, it is the iterator's return value.

- if not end of iteration, `next()` should return `{value, done: false}`
- when the end, return `{done: true}`

More info about (**iterator**)[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators]

### Getters, setters, and statics

```js
class Temperature {
  constructor(celsius) {
    this.celsius = celsius;
  }
  get fahrenheit() {
    return this.celsius * 1.8 + 32;
  }
  set fahrenheit(value) {
    this.celsius = (value - 32) / 1.8;
  }

  static fromFahrenheit(value) {
    return new Temperature((value - 32) / 1.8);
  }
}

let temp = new Temperature(22);
console.log(temp.fahrenheit); // → 71.6
temp.fahrenheit = 86;
console.log(temp.celsius);  // → 30
let temp2 = Temperature.fromFahrenheit(71.6);
console.log(temp, temp2);  // → {celsius: 30} {celsius: 21.999999999999996}
console.log(temp2.celsius);  // → 21.999999999999996
```

- `get` is `@property` in python
- `set` is `@getter_func_name.setter` in python
- `static`
  + The `static` keyword defines a static method for a class. Static methods aren't called on instances of the class. Instead, they're called on the class itself. These are often utility functions, such as functions to create or clone objects.

### Inheritance

```js
class Child extends Parent {
  constructor(x) {
    super(x, x);
  }

  set(x,value) {
    super.set(x, value);
  }
}
```

- `extends`
- `super`

### The instanceof operator

Almost every object is an instance of `Object`

`console.log([1] instanceof Array); // true`















