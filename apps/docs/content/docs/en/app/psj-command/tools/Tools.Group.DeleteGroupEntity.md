---
title: "Tools.Group.DeleteGroupEntity()"
description: "Delete Entity in Group"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Group > DeleteGroupEntity"
---

## Description

Delete Entity in Group

## Syntax

```psj
Tools.Group.DeleteGroupEntity(crlGroups)
```

## Inputs

### `crlGroups` @type(List\[Cursor]) @required

- The del group.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Group.DeleteGroupEntity(crlGroups)
```
