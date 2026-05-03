---
title: "Geometry.Face.Elements()"
description: "Create faces from the selected elements"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Face > Elements"
macro_link: "[CreateFaceByElem](../../macro/geometry/CreateFaceByElem)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create faces from the selected elements.

## Syntax

```psj
Geometry.Face.Elements(...)
```

## Inputs

### `crlElems` @type(List\[Cursor]) @required

- The surface elements to be moved to the new surface.

### `bSharedFace` @type(Boolean) @default(False)

- Whether to create a shared face. I&#x66;_&#x62;SharedFace=True_, th&#x65;_&#x63;rlElem&#x73;_&#x61;rgument must specify shared elements.

## Return Code

A _List of Cursor_ specifying the new created faces.

## Sample Code

```psj {3,4,5,6,7,8,9,10}
Geometry.Part.Cube()

created_face = Geometry.Face.Elements(crlElems=[Elem(1008,
                                                    1007,
                                                    989,
                                                    990,
                                                    1005,
                                                    1006,
                                                    988,
                                                    987)])

JPT.Debugger(created_face)
```
