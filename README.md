How to use output: +## Core Features

-(in the start array) +### Output +To print text to the console: +json +{"output": "text that you want to output"} +

--{"output":"text that you want to output"} +### Variables (State) +Variables are stored in a list called the "state". Every time you add a value, it gets a numerical index (0, 1, 2, etc.). + +**Creating a variable:** +json +{"state": "value"}

-anything as the value will be shown in the console.
-
-
-How to create variables:
-
-```
-{"state":"value"}
+**Accessing by index:**
+```json
+{"state(output)": 0}
-everytime you use the state command, you get an index
--{"state":1}, {"note":"index = 0"}, -{"state":1}, {"note":"index = 1"}, -{"state":1}, {"note":"index = 2"} +**Assigning names:** +You can assign a name to a specific index to make it easier to use. +json +{"state": 10}, +{"state(assign)": ["myNumber", 0]}, +{"state(output, values)": "myNumber"}

-you can use that index number to assign a name to those variables and show it as output
+**User Input:**
+```json
+{"state(input)": "Enter your name: "}
+```

-```
-{"state":2},
-{"state(assign)":["name", 0]},
-{"state(output, values)":"name"}
+### Math
+Math operations perform calculations on existing state indices and append the result to the state list.
+```json
+{"math(add)": [0, 1]}  // Adds values at index 0 and 1
+{"math(sub)": [0, 1]}
+{"math(mult)": [0, 1]}
+{"math(div)": [0, 1]}
+Increment/Decrement: +Works on assigned variables. +json +{"state(inc)": "varName"} +{"state(dec)": "varName"} +

-more stuff: +### Flow Control

-- {"input":"whats your name? "} gives an index to user input just like the regular state -- {"state(output)":0} outputs a regular index without being assigned +If Statements: +```json +{"if": {"==": true, "then": [

{"output": "Condition is true"} +]}} +```
+For Loops: +```json +{"for": {"start": 0, "stop": 10, "step": 1, "do": [

{"output": "Looping..."} +]}} +```
-if statements: +Infinite Loops: +```json +{"for(inf)": {"do": [

{"output": "Forever"},
{"break": null} +]}} +``` +Use {"break": null} to exit a loop.
-where it says condition you have to add your own +### Groups (Functions) +You can define reusable blocks of code called groups.

-``` -{"if":{"==":"condition", "then":[

{"note":["code goes here only executed under a certain condition"]} -]}} +Define a Group: +```json +{"group": {
"name": "myFunction",
"onCall": [
plaintext
   {"output": "Function called!"}
] +}} +```
-for loops: +Call a Group: +json +{"call": "myFunction"} +

-``` -{"for":{"start":1, "stop":10, "step":1, "do":[

{"note":["code goes here"]} -]}} +## Modules and Safety +Basic 82 introduces _include and _safety arrays to manage powerful commands.
+### Includes +Add these strings to the _include array in your JSON file to enable specific commands: + +- "randint : random": Enables {"randint": [min, max]} (Adds result to state). +- "pause : time": Enables {"pause": seconds} and {"pause(values)": "varName"}. +- "clear : os": Enables {"clear": null} to clear the console. +- "shutdown : os": Enables {"shutdown": null}. + +### Safety +Some commands are restricted. Add these to the _safety array to allow them: + +- "canShutdown": Allows the shutdown command to actually turn off the computer. + +### Example Configuration +```json +{

"_version": "basic82",
"_include": ["randint : random", "pause : time", "clear : os"],
"_safety": [],
"_start": [

   {"clear": null},

   {"output": "Console cleared."}

] +} +-```