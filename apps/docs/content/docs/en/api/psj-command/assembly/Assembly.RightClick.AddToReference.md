---
title: "Assembly.RightClick.AddToReference()"
description: "Add the current part to its Reference and use the added one as the current reference part"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assembly > Right Click > Add To Reference"
---

## Description

Add the current part to its Reference and use the added one as the current reference part.

## Syntax

```psj
Assembly.RightClick.AddToReference(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crSrcPart`

- The source part which will be become reference for destination part.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crDestPart`

- The destination part.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

adding _status = Assembly.RightClick.AddToReference(crSrcPart=Part(1), 
                                                   crDestPart=Part(1))

JPT.Debugger(adding _status)
```
