# Caching

## Background Context
In this project, you learn different caching algorithms.

## Resources, Read or watch:


- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_in_first_out_(FIFO))
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_in_first_out_(LIFO)_or_First_in_last_out_(FILO))
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU))
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most-recently-used_(MRU))
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_frequently_used_(LFU))

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:


## General
```Bash
What a caching system is
What FIFO means
What LIFO means
What LRU means
What MRU means
What LFU means
What the purpose of a caching system
What limits a caching system have
```

#### Requirements

* Python Scripts

    * All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
    * All your files should end with a new line
    * The first line of all your files should be exactly #!/usr/bin/env python3
    * A README.md file, at the root of the folder of the project, is mandatory
    * Your code should use the pycodestyle style (version 2.5)

    * All your files must be executable
    * The length of your files will be tested using wc
    * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    * A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

## More Info
Parent class BaseCaching
All your classes must inherit from [BaseCaching](https://github.com/madmeal1/holbertonschool-web_back_end/tree/main/caching/base_caching.py) defined here :