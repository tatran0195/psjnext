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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargetsParts`

- The target parts for boolean.

<!-- @since:5.0.1 @type:String @required -->
### `strNameSuffix`

- The target parts suffix name for after boolean.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBooleanType`

- The boolean operation type.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bLeaveOriginalPart`

- The enable/disalbe the option that keep original parts.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bImprintCrossLine`

- The enable/disalbe the option that imprint cross line on original parts.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTargetPart`

- The index of keep body.

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
