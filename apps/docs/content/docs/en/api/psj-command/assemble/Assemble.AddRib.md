---
title: "Assemble.AddRib()"
description: "Add the ribs to the body as a union part"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Add Rib"
macro _link: "[AddRib](../../macro/assemble/AddRib)"
---

## Description

Add the ribs to the body as a union part.

## Syntax

```psj
Assemble.AddRib(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPart`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Vector List @optional @default:[] -->
### `veclPoints`

- The points.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dWidth`

- The width.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDepth`

- The depth.

## Return Code

_True_ if success, or _False_ if fail.

## Sample Code

```psj
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0025, 0.01, 0.005], dlLength=[0.005, 0.01, 0.002], strName="Cube _4", iPartColor=15429611)
result = Assemble.AddRib(crPart=Part(1), crlFaces=[Face(47)], dWidth=0.01)
print(result)
```
