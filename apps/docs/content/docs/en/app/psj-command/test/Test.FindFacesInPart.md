---
title: "Test.FindFacesInPart()"
description: "Find faces in part by typical description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Test > FindFacesInPart"
---

## Description

Find faces in part by typical description

## Syntax

```psj
Test.FindFacesInPart(crPart, strIdentical)
```

## Inputs

### `crPart` @type(Cursor) @required

- The part.

### `strIdentical` @type(String) @required

- The identical.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.FindFacesInPart(crPart, strIdentical)
```
