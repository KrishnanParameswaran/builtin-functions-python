### filter()

filter() method filters each element in the given iterable with the given function. It tests each element with the function and outputs those that satisy the condition in function

Syntax: filter(func, iter)

func: it is the function to which filter passes each element of given iterable  
iter: it is the iterable which is to be filtered  

-> The result of filter() function can be passed to list() and set()  
-> Can use lambda expressions along with filter()  
-> An iterable is something that can be looped over and its definition requires implementation of __iter__() and __next__() methods  
-> An iterator is an object that remembers its state and is created by applying the iter() method on the iterable. The next value in the iteration can be obtained using next() method  

Executing instructions: 
1) Fork the repository
2) Create a local copy of the repo
3) Navigate into the directory containing filter_lambda.py from terminal or command line
4) Ensure to have python installed and is added to system path
5) Execute using this command: python filter_lambda.py


https://www.geeksforgeeks.org/filter-in-python/, http://book.pythontips.com/en/latest/map_filter.html, https://www.programiz.com/python-programming/methods/built-in/filter, https://www.w3schools.com/python/python_iterators.asp, https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration