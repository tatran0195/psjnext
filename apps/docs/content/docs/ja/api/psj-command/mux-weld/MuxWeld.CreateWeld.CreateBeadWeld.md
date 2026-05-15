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

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify the edge.

<!-- @since:5.0.1 @required -->
### crlPrjtedEdge

- Specify the projected edge.

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the part.

<!-- @since:5.0.1 @required -->
### dTol

- Specify the tolerance.

<!-- @since:5.0.1 @required -->
### dRatio

- Specify the ratio.

<!-- @since:5.0.1 @required -->
### crRefElem

- Specify the reference element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.CreateWeld.CreateBeadWeld(crlEdges, crlPrjtedEdge, crlParts, dTol, dRatio, crRefElem)
```
