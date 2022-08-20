# 0x00. AirBnB clone - The console

## Description
 This is a clone of the web appication AirBnb called HBnb. HBnb is a complete web application, integrating database storage, a back-end API and a front-end interface for the user. This part of the project only implements the back-end console. The back-end console `creates` the data model, `manage`(create, update, destroy, etc) objects, `store` and `persist` objects to a file(JSON file).

## Console
 The console is a command line interpreter that helps to manipulate data without a visual interface(pefect for development and debugging).

### Using the console
 The console can run both in interactie mode or non-interactive mode. To run the console in non-interactive mode, pipe any command(s) into the execution of the `console.py:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
and in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Testing
 A good program is one which has been tested with many different test cases. The python unittest package was used. To run the entire tests, execute the command:
```
$ python3 -m unittest discover tests
```
 Also, you can test for individual parts of the program by executing the command:
```
$ python3 -m unittest <file_name>(file_name can be found in the test folder
```

## Authors
* **Musa Oluwamayowa Micheal**
* **Ajimobi Oluwatosin Kareemat** 
