---
title: "Post.ImportResults.NastranOp2PostJob()"
description: "import Nastran op2 post job"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Post > ImportResults > NastranOp2PostJob"
---

## Description

Import Nastran op2 post job

## Syntax

```psj
Post.ImportResults.NastranOp2PostJob(strName, strlPaths, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlPaths`

- The paths.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The cursor of Result Nastran Op2 needs editing.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.NastranOp2PostJob(strName, strlPaths, crEdit=None)
```
