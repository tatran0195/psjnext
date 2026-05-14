---
title: "MuxWeld.CreateWeld.CreateBeadWeld()"
description: "Create a bead weld."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MuxWeld > CreateWeld > CreateBeadWeld"
---

## Description

Create a bead weld.

## Syntax

```psj
MuxWeld.CreateWeld.CreateBeadWeld(crlEdges, crlPrjtedEdge, crlParts, dTol, dRatio, crRefElem)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The edge.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlPrjtedEdge`

- The projected edge.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Double @required -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Double @required -->
### `dRatio`

- The ratio.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crRefElem`

- The reference element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.CreateWeld.CreateBeadWeld(crlEdges, crlPrjtedEdge, crlParts, dTol, dRatio, crRefElem)
```
