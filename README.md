# Recursion-in-Lambda-The-Y-combinator-
It allows you to implement recursion in a language that doesn't necessarily support recursion. 

What is Y combinator :

A Y-combinator is a "functional" (a function that operates on other functions) that enables recursion, when you can't refer to the function from within itself. In computer-science theory, it generalizes recursion, abstracting its implementation, and thereby separating it from the actual work of the function in question. The benefit of not needing a compile-time name for the recursive function is sort of a bonus.

Y f = λs.(f (s s)) λs.(f (s s))




Why its recursion ?

Answer :

If we pass a function itself as its argument then what happens :

- X = (λx. f (x x))(λx. f (x x))
- X = f (x x) [x := λx. f (x x)]
- X = f ((λx. f (x x)) (λx. f (x x)))
- X = f X

Given this, we can build a function that returns a fixed-point for any function f by taking the function in as an argument:
λf. (λx. f (x x))(λx. f (x x))
And that right there is the Y combinator. It’s a function that will return a fixed-point for any input function f. Let’s call it Y. For any function f, Yf is a fixed-point of f. That is, f(Yf) is equivalent to Yf. In fact, another name for the Y combinator is the fixed-point combinator for this reason.
