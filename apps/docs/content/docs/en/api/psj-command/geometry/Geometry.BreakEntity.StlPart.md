---
title: "Geometry.BreakEntity.StlPart()"
description: "Break STL part entity"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Break Entity > STL Part"
---

## Description

This method separates the _STL_ parts into multiple bodies.

## Syntax

```psj
Geometry.BreakEntity.StlPart(crlParts, iMinNoOfFacet=0, iBreakMethod=0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The STL parts to be separated.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMinNoOfFacet`

- The minimum number of facets to be considered as an entity.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBreakMethod`

- The break method.
- If _iBreakMethod=0_, separating using the Face based method.
- If _iBreakMethod=1_, separating using the Facet based method. This method separates on a facet basis, ignoring face configurations.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.BreakEntity.StlPart(crlParts=[Part(1)], iMinNoOfFacet=0, iBreakMethod=0)
```
