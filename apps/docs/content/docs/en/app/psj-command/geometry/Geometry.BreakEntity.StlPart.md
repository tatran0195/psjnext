---
title: "Geometry.BreakEntity.StlPart()"
description: "Break STL part entity"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Break Entity > STL Part"
---

## Description

This method separates the _STL_ parts into multiple bodies.

## Syntax

```psj
Geometry.BreakEntity.StlPart(crlParts, iMinNoOfFacet=0, iBreakMethod=0)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- STL parts to be separated.

### `iMinNoOfFacet` @type(Integer) @default(0)

- The minimum number of facets to be considered as an entity.

### `iBreakMethod` @type(Integer) @default(0)

- The break method.
- I&#x66;_&#x69;BreakMethod=0_, separating using the Face based method.
- I&#x66;_&#x69;BreakMethod=1_, separating using the Facet based method. This method separates on a facet basis, ignoring face configurations.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.BreakEntity.StlPart(crlParts=[Part(1)], iMinNoOfFacet=0, iBreakMethod=0)
```
