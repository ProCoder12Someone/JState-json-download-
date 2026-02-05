import json

code: str = input("jsonlang\\basic81 manager> ")

with open(code ,"r") as file:
    data = json.load(file)
    vars = []
    assigned = {}

    ALLOWED_KEYS = ["output", "state", "state(output)", "note", "state(assign)","state(output, values)",
                    "state(input)", "math(add)", "math(sub)", "math(mult)", "math(div)", "if", "state(inc)", "state(dec)",
                    "for"]

    if data["_version"] == "basic81" and "_start" in data:
        for cmd in data["_start"]:
            for key, value in cmd.items():
                if key not in ALLOWED_KEYS:
                    raise KeyError(f"Invalid Key: {key}")
                if key == "output":
                    print(value)
                if key == "state":
                    vars.append(value)
                if key == "state(output)":
                    print(vars[int(value)])
                if key == "state(assign)":
                    assigned[value[0]] = vars[int(value[1])]
                if key == "state(output, values)":
                    print(assigned[value])
                if key == "state(input)":
                    vars.append(input(value))
                if key == "math(add)":
                    vars.append(vars[int(value[0])] + vars[int(value[1])])
                if key == "math(sub)":
                    vars.append(vars[int(value[0])] - vars[int(value[1])])
                if key == "math(mult)":
                    vars.append(vars[int(value[0])] * vars[int(value[1])])
                if key == "math(div)":
                    vars.append(vars[int(value[0])] / vars[int(value[1])])  
                if key == "state(inc)":
                    vars.append(assigned[value] + 1)
                if key == "state(dec)":
                    vars.append(assigned[value] - 1)
                if key == "if":
                    if value["=="] == True: 
                        for c in value["then"]:
                            for k, v in c.items():
                                if k not in ALLOWED_KEYS:
                                    raise KeyError(f"Invalid Key: {key}")
                                if k == "output":
                                    print(v)
                                if k == "state":
                                    vars.append(v)
                                if k == "state(output)":
                                    print(vars[int(v)])
                                if k == "state(assign)":
                                    assigned[v[0]] = vars[int(v[1])]
                                if k == "state(output, values)":
                                    print(assigned[v])
                                if k == "state(input)":
                                    vars.append(input(v))
                                if k == "math(add)":
                                    vars.append(vars[int(v[0])] + vars[int(v[1])])
                                if k == "math(sub)":
                                    vars.append(vars[int(v[0])] - vars[int(v[1])])
                                if k == "math(mult)":
                                    vars.append(vars[int(v[0])] * vars[int(v[1])])
                                if k == "math(div)":
                                    vars.append(vars[int(v[0])] / vars[int(v[1])])  
                                if k == "state(inc)":
                                    vars.append(assigned[v] + 1)
                                if k == "state(dec)":
                                    vars.append(assigned[v] - 1)
                if key == "for":
                    for i in range(value["start"], value["stop"], value["step"]):
                        for c in value["do"]:
                            for k, v in c.items():
                                if k not in ALLOWED_KEYS:
                                    raise KeyError(f"Invalid Key: {key}")
                                if k == "output":
                                    print(v)
                                if k == "state":
                                    vars.append(v)
                                if k == "state(output)":
                                    print(vars[int(v)])
                                if k == "state(assign)":
                                    assigned[v[0]] = vars[int(v[1])]
                                if k == "state(output, values)":
                                    print(assigned[v])
                                if k == "state(input)":
                                    vars.append(input(v))
                                if k == "math(add)":
                                    vars.append(vars[int(v[0])] + vars[int(v[1])])
                                if k == "math(sub)":
                                    vars.append(vars[int(v[0])] - vars[int(v[1])])
                                if k == "math(mult)":
                                    vars.append(vars[int(v[0])] * vars[int(v[1])])
                                if k == "math(div)":
                                    vars.append(vars[int(v[0])] / vars[int(v[1])])  
                                if k == "state(inc)":
                                    vars.append(assigned[v] + 1)
                                if k == "state(dec)":
                                    vars.append(assigned[v] - 1)