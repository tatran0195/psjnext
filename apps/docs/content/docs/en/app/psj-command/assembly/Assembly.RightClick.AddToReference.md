---
title: "Assembly.RightClick.AddToReference()"
description: "Add the current part to its Reference and use the added one as the current reference part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assembly > Right Click > Add To Reference"
---

## Description

Add the current part to its Reference and use the added one as the current reference part.

## Syntax

```psj
Assembly.RightClick.AddToReference(...)
```

## Inputs

### `crSrcPart` @type(Cursor) @required

- The source part which will be become reference for destination part.

### `crDestPart` @type(Cursor) @required

- The destination part.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

adding_status = Assembly.RightClick.AddToReference(crSrcPart=Part(1), 
                                                   crDestPart=Part(1))

JPT.Debugger(adding_status)
```
