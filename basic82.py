import json
import os
import random
import time

code: str = input("jsonlang\\basic82 manager> ")

def keys(data):
    for c in value[data]:
                            for k, v in c.items():
                                if k not in ALLOWED_KEYS:
                                    raise KeyError(f"Invalid Key: {key}")
                                if k == "output":
                                    print(v)
                                if k == "state":
                                    variables.append(v)
                                if k == "state(output)":
                                    print(variables[int(v)])
                                if k == "state(assign)":
                                    assigned[v[0]] = variables[int(v[1])]
                                if k == "state(output, values)":
                                    print(assigned[v])
                                if k == "state(input)":
                                    variables.append(input(v))
                                if k == "math(add)":
                                    variables.append(variables[int(v[0])] + variables[int(v[1])])
                                if k == "math(sub)":
                                    variables.append(variables[int(v[0])] - variables[int(v[1])])
                                if k == "math(mult)":
                                    variables.append(variables[int(v[0])] * variables[int(v[1])])
                                if k == "math(div)":
                                    variables.append(variables[int(v[0])] / variables[int(v[1])])
                                if k == "state(inc)":
                                    variables.append(assigned[v] + 1)
                                if k == "state(dec)":
                                    variables.append(assigned[v] - 1)
                                if k == "break":
                                    break
                                if k == "randint" and "randint : random" in included:
                                    variables.append(random.randint(v[0], v[1]))

with open(code ,"r") as file:
    data = json.load(file)
    variables = []
    assigned = {}
    group_on_call = {}
    included = []
    safety = []

    ALLOWED_KEYS = ["output", "state", "state(output)", "note", "state(assign)","state(output, values)",
                    "state(input)", "math(add)", "math(sub)", "math(mult)", "math(div)", "if", "state(inc)", "state(dec)",
                    "for", "for(inf)", "group", "call", "break", "randint", "pause", "pause(values)"]
    
    if "_include" in data:
        for include in data["_include"]:
            included.append(include)

    if "_safety" in data:
        for i in data["_safety"]:
            safety.append(i)


    if data["_version"] == "basic82" and "_start" in data:
        for cmd in data["_start"]:
            for key, value in cmd.items():
                if key not in ALLOWED_KEYS:
                    raise KeyError(f"Invalid Key: {key}")
                if key == "output":
                    print(value)
                if key == "state":
                    variables.append(value)
                if key == "state(output)":
                    print(variables[int(value)])
                if key == "state(assign)":
                    assigned[value[0]] = variables[int(value[1])]
                if key == "state(output, values)":
                    print(assigned[value])
                if key == "state(input)":
                    variables.append(input(value))
                if key == "math(add)":
                    variables.append(variables[int(value[0])] + variables[int(value[1])])
                if key == "math(sub)":
                    variables.append(variables[int(value[0])] - variables[int(value[1])])
                if key == "math(mult)":
                    variables.append(variables[int(value[0])] * variables[int(value[1])])
                if key == "math(div)":
                    variables.append(variables[int(value[0])] / variables[int(value[1])])
                if key == "state(inc)":
                    variables.append(assigned[value] + 1)
                if key == "state(dec)":
                    variables.append(assigned[value] - 1)
                if key == "randint" and "randint : random" in included:
                    variables.append(random.randint(value[0], value[1]))
                if key == "pause" and "pause : time" in included:
                    time.sleep(value)
                if key == "pause(values)" and "pause : time" in included:
                    time.sleep(assigned[value])
                if key == "clear" and "clear : os" in included:
                    os.system("cls")
                if key == "shutdown" and "shutdown : os" in included and "canShutdown":
                    os.system("shutdown /s /t 0")

                if key == "if":
                    if value["=="]:
                        keys("then")
                if key == "for":
                    for i in range(value["start"], value["stop"], value["step"]):
                        keys("do")
                if key == "for(inf)":
                    while True:
                        keys("do")
                if key == "group":
                        group_on_call[value["name"]] = value["onCall"]
                if key == "call":
                    if value in group_on_call:
                        for c in group_on_call[value]:
                            for k, v in c.items():
                                if k not in ALLOWED_KEYS:
                                    raise KeyError(f"Invalid Key: {key}")
                                if k == "output":
                                    print(v)
                                if k == "state":
                                    variables.append(v)
                                if k == "state(output)":
                                    print(variables[int(v)])
                                if k == "state(assign)":
                                    assigned[v[0]] = variables[int(v[1])]
                                if k == "state(output, values)":
                                    print(assigned[v])
                                if k == "state(input)":
                                    variables.append(input(v))
                                if k == "math(add)":
                                    variables.append(variables[int(v[0])] + variables[int(v[1])])
                                if k == "math(sub)":
                                    variables.append(variables[int(v[0])] - variables[int(v[1])])
                                if k == "math(mult)":
                                    variables.append(variables[int(v[0])] * variables[int(v[1])])
                                if k == "math(div)":
                                    variables.append(variables[int(v[0])] / variables[int(v[1])])
                                if k == "state(inc)":
                                    variables.append(assigned[v] + 1)
                                if k == "state(dec)":
                                    variables.append(assigned[v] - 1)
                                if k == "randint" and "randint : random" in included:
                                    variables.append(random.randint(v[0], v[1]))