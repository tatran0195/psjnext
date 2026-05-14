---
title: "MeshCleanup.Element.SurfaceElement()"
description: "Change Topology Element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Element > SurfaceElement"
---

## Description

Change Topology Element

## Syntax

```psj
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilElement`

- The element.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilFace`

- The face.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilPart`

- The part.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCreateNewPart`

- The create new part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```
