---
title: "Assembly.RightClick.Suppress()"
description: "Suppress part on Assembly tree"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assembly > Right Click > Suppress"
---

## Description

Suppress part on Assembly tree.

## Syntax

```psj
Assembly.RightClick.Suppress(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

## Return Code

_True_ if success, or _False_ if fail.

## Sample Code

```psj
Geometry.Part.Cube()
result = Assembly.RightClick.Suppress(crlParts=[Part(1)])
print(result)
```
