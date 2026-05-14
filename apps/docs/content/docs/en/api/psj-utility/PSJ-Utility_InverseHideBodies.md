---
title: "JPT.InverseHideBodies()"
description: "Show the part having the inputted ID only"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show the part having the inputted ID only.

## Syntax

```psj
JPT.InverseHideBodies(partID)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `partID`

- The ID of the part which will be shown only.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {12}
# Prepare model
Geometry.Part.Cube(strName="Cube _11", iPartColor=11842649)
Geometry.Part.Cube(strName="Cube _12", iPartColor=14968422)
Geometry.Part.Cube(strName="Cube _13", iPartColor=6250447)
Geometry.Part.Cube(strName="Cube _14", iPartColor=12734402)
Geometry.Part.Cube(strName="Cube _15", iPartColor=16579696)

# Show the part with ID = 3 only (Cube _13)
selAllParts = JPT.GetAllParts()
showPart = selAllParts[2].id
JPT.Debugger(selAllParts[2])
JPT.InverseHideBodies(showPart)
```
