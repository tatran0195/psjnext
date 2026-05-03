---
title: "MeshCleanup.Element.SurfaceElement()"
description: "Change Topology Element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Element > SurfaceElement"
---

## Description

Change Topology Element

## Syntax

```psj
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```

## Inputs

### `ilElement` @type(List\[Integer]) @default(\[])

- The element.

### `ilFace` @type(List\[Integer]) @default(\[])

- The face.

### `ilPart` @type(List\[Integer]) @default(\[])

- The part.

### `iCreateNewPart` @type(Integer) @default(0)

- The create new part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```
