---
title: "Assembly.RightClick.UnSuppress()"
description: "Unsuppress part on Assembly tree"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assembly > Right Click > UnSuppress"
---

## Description

Unsuppress part on Assembly tree.

## Syntax

```psj
Assembly.RightClick.UnSuppress(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

## Return Code

_True_ if success, or _False_ if fail.

## Sample Code

```psj
Geometry.Part.Cube()
Assembly.RightClick.Suppress(crlParts=[Part(1)])
result = Assembly.RightClick.UnSuppress(crlParts=[Part(1)])
print(result)
```
