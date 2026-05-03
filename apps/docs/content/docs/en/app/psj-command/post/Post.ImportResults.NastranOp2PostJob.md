---
title: "Post.ImportResults.NastranOp2PostJob()"
description: "import Nastran op2 post job"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Post > ImportResults > NastranOp2PostJob"
---

## Description

Import Nastran op2 post job

## Syntax

```psj
Post.ImportResults.NastranOp2PostJob(strName, strlPaths, crEdit=None)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `strlPaths` @type(List\[String]) @required

- The paths.

### `crEdit` @type(Cursor) @default(None)

- The cursor of Result Nastran Op2 needs editing.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.NastranOp2PostJob(strName, strlPaths, crEdit=None)
```
