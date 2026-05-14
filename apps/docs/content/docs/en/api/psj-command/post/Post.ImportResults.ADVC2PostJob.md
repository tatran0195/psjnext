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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlResultFolderPaths`

- The result folder paths.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ADVC2PostJob(strName, strlResultFolderPaths, crEdit)
```
