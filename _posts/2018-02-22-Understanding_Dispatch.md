---
layout: post
title:  "Understanding Dispatch"
date:   2018-02-22 08:39:40 +0800
tags: 
    - Dispatch 
    - Dynamic-dispath 
    - telegram 
    - api 
    - ploymorhic
---


## Introduction

- <https://core.telegram.org/bots/api#getting-updates>
- <https://github.com/qd452/python-telegram-bot>
- <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot>

The dispatcher concept is introduced in the `python-telegram-bot` when I was trying to use it. This library provides a pure Python interface for the [Telegram Bot API](https://core.telegram.org/bots/api).

In addition to the **pure API implementation**, this library features a number of **high-level classes** to make the development of bots easy and straightforward. These classes are contained in the **`telegram.ext`** submodule.

So, basically, this `telegram.ext` is an extension added by the `python-telegram` developers. The default [Telegram Bot API](https://core.telegram.org/bots/api) didn't actually offer this high level class.

so I need to understand the implementation of the `telegram.ext`, and about the `dispatcher`, `updater` etc. 

**[todo]**:read the src code

## Dynamic Dispatch

<https://en.wikipedia.org/wiki/Dynamic_dispatch>

> In computer science, dynamic dispatch is the process of selecting which implementation of a **polymorphic** operation (method or function) to call at **run time**. It is commonly employed in, and considered a prime characteristic of, object-oriented programming (OOP) languages and systems.

## Polymorphism

> pol·y·mor·phism
The condition of occurring in several different forms.

### Polymorphism in C++

The reading: [THE C++ PROGRAMMING LANGUAGE (Special Edition) *by Bjame Stroustrup - the creator of C++*](https://www.amazon.com/Programming-Language-Special-3rd/dp/0201700735)

**In Page 1005, the index polymorphism** *(i use red tags in the book)*, which leads to 

- object, algorithm and polymorphic in page 63
- algorithm & container and polymorphism in page 520
- compile-time and run-time polymorphism, parametric in page 347 
- virtual function (like pass in python)

#### inheritance

Example is to define a `class Shape` (the superclass), and the subclass/derived class `class Circle` or `class Triangle`. `virtual` functions are defined in the superclass `Shape`.

The **programming paradigm** */ ˈpærədaɪm; ˋpærəˏdaɪm/ n*:


| decide which classes you want;<br>provide a full set of operations for each class;<br>make commonality explicit by using inheritance;   |
|-------------------|

> When a system is designed - and even when the requirements for the system are written - commonality must be actively sought.

> Class hierarchies and abstract classes ($2.5.4) complement each other instead of being mutually exclusive ($12.5).

#### Derived classes - virtual functions

```
class Employee {
    string first_name, family_name;
    short department;
    // ...
public:
    Employee(const string& name, int dept);
    virtual void print() const;
    // ...
};

void Employee::print() const
{
    cout << family_name << ´\t´ << department << ´\n´;
    // ...
}

class Manager : public Employee {
    set<Employee*> group;
    short level;
    // ...
public:
    Manager(const string& name, int dept, int lvl);
    void print() const;
    // ...
};

void Manager::print() const
{
    Employee::print();
    cout << "\tlevel " << level << ´\n´;
    // ...
}

void print_list(set<Employee*>& s)
{
    for (set<Employee*>::const_iterator p = s.begin(); p!=s.end(); ++p)// see §2.7.2
        (*p)->print();
}
```

For example:
```
int main()
{
    Employee e("Brown",1234);
    Manager m("Smith",1234,2);
    set<Employee*> empl;
    empl.push_front(&e); // see §2.5.4
    empl.push_front(&m);
    print_list(empl);
}
```

produced:

```
Smith 1234
    level 2
Brown 1234
```

Note that this will work even if `Employee::print_list()` was written and compiled before the specific derived class Manager was even conceived of!

**Getting ‘‘the right’’ behavior from Employee’s functions independently of exactly what kind of Employee is actually used is called *polymorphism*.**

A type with virtual functions is called a polymorphic type. To get polymorphic behavior in C++, the member functions called must be virtual and objects must be manipulated through pointers or references. When manipulating an object directly (rather than through a pointer or reference), its exact type is known by the compilation so that run-time polymorphism is not needed.

#### Templates - Parameterization and Inheritance

A template parameterizes the definition of a type or a function with another type. 

- Code implementing the template is identical for all parameter types, as is most code using the template. 
- An abstract class defines an interface. Much code for different implementations of the abstract class can be shared in class hierarchies, and most code using the abstract class doesn’t depend on its implementation. 

From a design perspective, the two approaches are so close that they deserve a common name. Since both allow an algorithm to be expressed once and applied to a variety of types, people sometimes **refer to both as polymorphic**. 

To distinguish them, 

- **what virtual functions provide is called run-time polymorphism,**
- **and what templates offer is called compile-time polymorphism or parametric polymorphism.**

So when do we choose to use a template and when do we rely on an abstract class? In either case, we manipulate objects that share a common set of operations. If no hierarchical relationship is required between these objects, they are best used as template arguments. If the actual types of these objects cannot be known at compile-time, they are best represented as classes derived from a common abstract class. If run-time efficiency is at a premium, that is, if inlining of operations is essential, a template should be used. This issue is discussed in greater detail in §24.4.1.




[back](../)