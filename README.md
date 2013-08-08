# matsts — My Automatic TeST System

Script automates giving arguments to an any program. It uses testfile with specific syntax, wherein each line is a new test.
Each test will be expanded to 1 or many (if you use repeat function) argument lists and these lists will be given to your program.

All available external functions are defined in `matsts_foo.py`, and you can add your own functions in this file (and push ones in this repo if you want :) ). You may change syntax for functions in `matsts_parser.py`.

Using:  
```
matsts <exefile> <testfile>
```

## Example
If you have this testfile.matsts (github parser changed tabs into spaces.
It is important to use tabs for divide arguments):  
```
$repeat(4)	$rnd(-10,10)	abcd12345
$repeat(2)	1	2	3
arg1	arg2	arg3
```
Then command  
```
matsts myprogram testfile.matsts
```  
will be expanded into something like this:  
```
myprogram -4 abcd12345
myprogram 7 abcd12345
myprogram -10 abcd12345
myprogram 2 abcd12345
myprogram 1 2 3
myprogram 1 2 3
myprogram arg1 arg2 arg3
```

## Functions
### Built-in functions
* Repeat this test CNT times  
    ```
    $repeat(CNT)
    ```

### External functions
* Random integer in interval [MIN..MAX)  
    ```
    $rnd(MIN,MAX,STEP=1)
    ```
* Random float in interval [MIN..MAX)  
    ```
    $frnd(MIN=0,MAX=1)
    ```

### Argument types in functions
* int
* float
* string (quoted argument)
