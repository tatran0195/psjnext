---
title: "JPT.Exec()"
description: "Run Jupiter macro"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Run Jupiter macro.

## Syntax

```psj
JPT.Exec(macroCommand)
```

## Inputs

<!-- @since:5.0.1 @required -->
### macroCommand

- Specify the macro command.

## Return Code

Based on the output of the inputted macro command.

## Sample Code

```psj {2,3}
# Create a cube and store its cursor
createdCube = JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], \
                        [10, 10, 10], "Cube _1", 12999622, 0:0)')
JPT.Debugger(createdCube) # Return a string object with value = 3:1
```
