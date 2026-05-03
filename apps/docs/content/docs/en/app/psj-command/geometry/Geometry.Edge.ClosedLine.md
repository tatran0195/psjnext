---
title: "Geometry.Edge.ClosedLine()"
description: "Imprint closed lines onto face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Closed Line"
macro_link: "[ImprintCloseLineS](../../macro/geometry/ImprintCloseLineS)"
---
<!-- REVIEW FLAGS — requires human review
   [param_rename_candidate] 'crlTargetFace' may be a rename of 'crlTargetsFace' (93% similar)
     context: {"from":"crlTargetsFace","to":"crlTargetFace","similarity":0.9285714285714286}
   [param_decorator_changed] Param 'veclPositions' @type changed from 'List[Vector]' to 'List[Position]' in v5.1.0
     context: {"param":"veclPositions","fromVersion":"5.0.1","toVersion":"5.1.0","fromType":"List[Vector]","toType":"List[Position]"}
   [param_removed_unexpectedly] Param 'iEnableBreakFace' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

This method imprints closed lines onto the given face.

## Syntax

```psj
Geometry.Edge.ClosedLine(...)
```

## Inputs

### `veclPositions` @type(List\[Position]) @required

- Points on the target faces.

### `crlTargetFace` @type(List\[Cursor]) @required @since(5.1.0)

- The target faces on which the edges are imprinted.

### `bBreakFace` @type(Boolean) @default(True) @since(5.1.0)

- Whether to break the given faces where possible.

### `crlTargetsFace` @type(List\[Cursor]) @required @deprecated @until(5.1.0)

- Faces to be imprinted.

### `iEnableBreakFace` @type(Integer) @default(1) @deprecated @until(5.1.0)

- Whether to break the given faces after the imprint operation. Possible values are 0 and 1.
- I&#x66;_&#x69;EnableBreakFace=0_, do not break given face where possible after the imprint operation.
- I&#x66;_&#x69;EnableBreakFace=1_, break given face where possible after the imprint operation.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3-7}
Geometry.Part.Cube()

closed_lines = Geometry.Edge.ClosedLine(veclPositions=[[0.0058, 0.0028, 0.01], 
                                        [0.0038, 0.0029, 0.01], 
                                        [0.0040, 0.0047, 0.01], 
                                        [0.0063, 0.0046, 0.01]],
                                         crlTargetsFace=[Face(26)])
JPT.Debugger(closed_lines)
```
