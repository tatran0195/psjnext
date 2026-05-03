---
title: "Post.ImportResults.ADVC2PostJob()"
description: "Post ImportResults ADVC2PostJob"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Post > ImportResults > ADVC2PostJob"
---

## Description

Post ImportResults ADVC2PostJob

## Syntax

```psj
Post.ImportResults.ADVC2PostJob(strName, strlResultFolderPaths, crEdit)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `strlResultFolderPaths` @type(List\[String]) @required

- The result folder paths.

### `crEdit` @type(Cursor) @required

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ADVC2PostJob(strName, strlResultFolderPaths, crEdit)
```
