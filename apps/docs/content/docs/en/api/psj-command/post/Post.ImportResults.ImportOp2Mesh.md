---
title: "Post.ImportResults.ImportOp2Mesh()"
description: "import Nastran op2 mesh"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Post > ImportResults > ImportOp2Mesh"
---

## Description

Import Nastran op2 mesh

## Syntax

```psj
Post.ImportResults.ImportOp2Mesh(strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0)
```

## Inputs

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlFilePaths`

- The file paths.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iImportType`

- The import type.

<!-- @since:5.0.1 @type:Double @optional @default:60.0 -->
### `dFaceAngle`

- The face angle.

<!-- @since:5.0.1 @type:Double @optional @default:60.0 -->
### `dEdgeAngle`

- The edge angle.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ImportOp2Mesh(strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0)
```
