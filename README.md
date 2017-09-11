# Recursion-in-Lambda-The-Y-combinator-
It allows you to implement recursion in a language that doesn't necessarily support recursion. 

What is Y combinator :

A Y-combinator is a "functional" (a function that operates on other functions) that enables recursion, when you can't refer to the function from within itself. In computer-science theory, it generalizes recursion, abstracting its implementation, and thereby separating it from the actual work of the function in question. The benefit of not needing a compile-time name for the recursive function is sort of a bonus.

Y f = λs.(f (s s)) λs.(f (s s))




Why its recursion ?

Answer :

X = (λx. f (x x))(λx. f (x x))
X = f (x x) [x := λx. f (x x)]
X = f ((λx. f (x x)) (λx. f (x x)))
X = f X
