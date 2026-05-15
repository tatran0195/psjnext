---
title: "Post.ImportResults.ADVC2PostJob()"
description: "Post ImportResults ADVC2PostJob"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Post > ImportResults > ADVC2PostJob"
---

## Description

Post ImportResults ADVC2PostJob

## Syntax

```psj
Post.ImportResults.ADVC2PostJob(strName, strlResultFolderPaths, crEdit)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### strlResultFolderPaths

- Specify the result folder paths.

<!-- @since:5.0.1 @required -->
### crEdit

- Specify the edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ADVC2PostJob(strName, strlResultFolderPaths, crEdit)
```
