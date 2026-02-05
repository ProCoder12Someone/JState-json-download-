# JState-json-download-
this is how to use JState basic 81 and every other version (will update once there are new versions)
(please do not use this for anything serious it will not work)

Steps to get started:

- download the version you want from here, just copy+paste the code in the version in a .py file 

- make a new json file

- in the json file add this code, change the _version to the version you have.
  anything in the _start array will run but you can't run code outside of that.

```
{
    "_version":"basic81",
    "_start":[

    ]
}
```

How to use output:

(in the start array)

```
{"output":"text that you want to output"}
```

anything as the value will be shown in the console.


How to create variables:

```
{"state":"value"}
```

everytime you use the ```state``` command, you get an index 

```
{"state":1}, {"note":"index = 0"},
{"state":1}, {"note":"index = 1"},
{"state":1}, {"note":"index = 2"}
```

you can use that index number to assign a name to those variables and show it as output

```
{"state":2},
{"state(assign)":["name", 0]},
{"state(output, values)":"name"}
```


more stuff:

- {"input":"whats your name? "} gives an index to user input just like the regular state
- {"state(output)":0} outputs a regular index without being assigned


if statements:

where it says condition you have to add your own

```
{"if":{"==":"condition", "then":[
    {"note":["code goes here only executed under a certain condition"]}
]}}

for loops:

```
{"for":{"start":1, "stop":10, "step":1, "do":[
    {"note":["code goes here"]}
]}}
```
