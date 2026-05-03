---
title: "Assemble.AddRib()"
description: "Add the ribs to the body as a union part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assemble > Add Rib"
macro_link: "[AddRib](../../macro/assemble/AddRib)"
---

## Description

Add the ribs to the body as a union part.

## Syntax

```psj
Assemble.AddRib(...)
```

## Inputs

### `crPart` @type(Cursor) @default(None)

- The part.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `veclPoints` @type(Vector List) @default(\[])

- The points.

### `dWidth` @type(Double) @default(0.0)

- The width.

### `dDepth` @type(Double) @default(0.0)

- The depth.

## Return Code

_True_ if success, or _False_ if fail.

## Sample Code

```psj
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0025, 0.01, 0.005], dlLength=[0.005, 0.01, 0.002], strName="Cube_4", iPartColor=15429611)
result = Assemble.AddRib(crPart=Part(1), crlFaces=[Face(47)], dWidth=0.01)
print(result)
```
