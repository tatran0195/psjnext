---
title: "Assemble.BooleanEx()"
description: "Conduct a Boolean operation on selected bodies"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assemble > Boolean"
---

## Description

Conduct a Boolean operation on selected bodies.

## Syntax

```psj
Assemble.BooleanEx(...)
```

## Inputs

### `crlTargetsParts` @type(List\[Cursor]) @required

- The target parts for boolean.

### `strNameSuffix` @type(String) @required

- The target parts suffix name for after boolean.

### `iBooleanType` @type(Integer) @default(0)

- The boolean operation type.

### `bLeaveOriginalPart` @type(Boolean) @default(False)

- Enable/disalbe the option that keep original parts.

### `bImprintCrossLine` @type(Boolean) @default(False)

- Enable/disalbe the option that imprint cross line on original parts.

### `iTargetPart` @type(Integer) @default(0)

- The index of keep body.

## Return Code

A _Cursor_ of body if success, or _None_ if fail.

## Sample Code

```psj {6,7}
cube1 = Geometry.Part.Cube(iPartColor=4934581)
cube2 = Geometry.Part.Cube(dlOrigin=[0.005, 0.005, 0.005], 
                           strName="Cube_2", 
                           iPartColor=6215639)

boolean_status = Assemble.BooleanEx([cube1, cube2], 
                                    iTargetPart=1)

JPT.Debugger(boolean_status)
```
