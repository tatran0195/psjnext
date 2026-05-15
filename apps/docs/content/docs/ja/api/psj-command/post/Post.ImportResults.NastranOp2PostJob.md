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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### strlPaths

- Specify the paths.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the cursor of Result Nastran Op2 needs editing.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.NastranOp2PostJob(strName, strlPaths, crEdit=None)
```
