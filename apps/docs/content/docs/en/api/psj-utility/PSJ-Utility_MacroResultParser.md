---
title: "JPT.MacroResultParser()"
description: "Splitting the returned value from an executed macro to a list of strings"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Splitting the returned value from an executed macro to a _List of Strings_.

## Syntax

```psj
JPT.MacroResultParser(returnedMacroString, listOfStringPattern)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `returnedMacroString`

- The returned value from the executed macro.

<!-- @since:5.0.1 @type:List[String] @required -->
### `listOfStringPattern`

- The pattern splitting from the returned MacroString.
  - The output list requiring the below values:
    - string
    - cursor
    - cursor\_pair
    - list\_number
    - list\_cursor\_pair
    - list\_cursor
    - list\_list\_cursor
    - list\_string
    - vector3d
    - number

## Return Code

A _List_ split from the returned value from an executed macro containing strings.

## Sample Code

```psj {45}
"""
Structure: JPT.MacroResultParser(input _string, arg _pattern)

Supporting type for arg _pattern:
"string",
"cursor",
"cursor _pair",
"list _cursor _pair",
"list _cursor",
"list _list _cursor",
"list _string",
"vector3d",
"list _number",
"number"
"""

print(__doc__)

import re

Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube _4", iPartColor=7463537)
Geometry.Part.Cube(dlOrigin=[0.03, 0.01, 0.0], strName="Cube _5", iPartColor=7434735)
Geometry.Part.Cube(dlOrigin=[0.03, 0.02, 0.0], strName="Cube _6", iPartColor=14903267)
Geometry.Part.Cube(dlOrigin=[0.03, 0.03, 0.0], strName="Cube _7", iPartColor=15658599)
Geometry.Part.Cube(dlOrigin=[0.02, 0.03, 0.0], strName="Cube _8", iPartColor=7961077)
Geometry.Part.Cube(dlOrigin=[0.01, 0.03, 0.0], strName="Cube _9", iPartColor=7829501)
Geometry.Part.Cube(dlOrigin=[0.0, 0.03, 0.0], strName="Cube _10", iPartColor=11842649)
Geometry.Part.Cube(dlOrigin=[0.0, 0.02, 0.0], strName="Cube _11", iPartColor=14968422)
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube _12", iPartColor=6250447)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], strName="Cube _13", iPartColor=12734402)
Geometry.Part.Cube(dlOrigin=[0.02, 0.01, 0.0], strName="Cube _14", iPartColor=16579696)
Geometry.Part.Cube(dlOrigin=[0.02, 0.02, 0.0], strName="Cube _15", iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.01, 0.02, 0.0], strName="Cube _18", iPartColor=13787489)

select _contact _face = JPT.Exec('FindContactPairsDynamic([{}], 0, 0, 0.001, 1, 1, 0.001)'.\
                            format(", ".join([("3:" + str(_.id)) for _ in JPT.GetAllParts()])))

arg _pattern = ["number",
               "list _string",
               "list _list _cursor",
               "list _list _cursor"]
list _args = JPT.MacroResultParser(select _contact _face, arg _pattern)
JPT.Debugger(list _args)

print(
    f"Finding status : \
        {'Found contacts' if list _args[1]!=[] and list _args[1]!=[] else 'This model does not have contact'}"
)

number _of _matching = len((re.sub("\]|\[", "", list _args[1]).strip().split(",")))
print(f"Number of contacts: {number _of _matching}")

JPT.Exec('FindContact({0}, {1}, {2}, [{3}], [{4}], [{5}], [{6}], [{7}], \
                      [{8}], [{9}], [{10}])'.\
          format(list _args[1],
                 list _args[2],
                 list _args[3],
                 ",".join(["1" for _ in range(number _of _matching)]),
                 ",".join(["0.001" for _ in range(number _of _matching)]),
                 ",".join(["1.79769e+308" for _ in range(number _of _matching)]),
                 ",".join(["0" for _ in range(number _of _matching)]),
                 ",".join(["65280" for _ in range(number _of _matching)]),
                 ",".join(["0:0" for _ in range(number _of _matching)]),
                 ",".join(["0:0" for _ in range(number _of _matching)]),
                 ",".join(["0:0" for _ in range(number _of _matching)])))
```
