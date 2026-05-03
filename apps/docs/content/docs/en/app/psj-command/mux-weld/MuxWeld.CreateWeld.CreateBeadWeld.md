---
title: "MuxWeld.CreateWeld.CreateBeadWeld()"
description: "Create a bead weld."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MuxWeld > CreateWeld > CreateBeadWeld"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Create a bead weld."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a bead weld.

## Syntax

```psj
MuxWeld.CreateWeld.CreateBeadWeld(crlEdges, crlPrjtedEdge, crlParts, dTol, dRatio, crRefElem)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The edge.

### `crlPrjtedEdge` @type(List\[Cursor]) @required

- The projected edge.

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `dTol` @type(Double) @required

- The tolerance.

### `dRatio` @type(Double) @required

- The ratio.

### `crRefElem` @type(Cursor) @required

- The reference element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.CreateWeld.CreateBeadWeld(crlEdges, crlPrjtedEdge, crlParts, dTol, dRatio, crRefElem)
```
