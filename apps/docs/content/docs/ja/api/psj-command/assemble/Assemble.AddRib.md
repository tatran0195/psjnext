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

<!-- @since:5.0.1 @optional -->
### crPart

- Specify the part.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### veclPoints

- Specify the points.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dWidth

- Specify the width.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dDepth

- Specify the depth.
- The default value is 0.0.

## Return Code

_True_ if success, or _False_ if fail.

## Sample Code

```psj
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0025, 0.01, 0.005], dlLength=[0.005, 0.01, 0.002], strName="Cube _4", iPartColor=15429611)
result = Assemble.AddRib(crPart=Part(1), crlFaces=[Face(47)], dWidth=0.01)
print(result)
```
