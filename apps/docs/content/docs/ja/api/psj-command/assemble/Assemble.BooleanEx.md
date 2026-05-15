---
title: "Assemble.BooleanEx()"
description: "Conduct a Boolean operation on selected bodies"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Boolean"
---

## Description

Conduct a Boolean operation on selected bodies.

## Syntax

```psj
Assemble.BooleanEx(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlTargetsParts

- Specify the target parts for boolean.

<!-- @since:5.0.1 @required -->
### strNameSuffix

- Specify the target parts suffix name for after boolean.

<!-- @since:5.0.1 @optional -->
### iBooleanType

- Specify the boolean operation type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bLeaveOriginalPart

- Specify keep original parts.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bImprintCrossLine

- Specify imprint cross line on original parts.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iTargetPart

- Specify the index of keep body.
- The default value is 0.

## Return Code

A _Cursor_ of body if success, or _None_ if fail.

## Sample Code

```psj {6,7}
cube1 = Geometry.Part.Cube(iPartColor=4934581)
cube2 = Geometry.Part.Cube(dlOrigin=[0.005, 0.005, 0.005], 
                           strName="Cube _2", 
                           iPartColor=6215639)

boolean _status = Assemble.BooleanEx([cube1, cube2], 
                                    iTargetPart=1)

JPT.Debugger(boolean _status)
```
