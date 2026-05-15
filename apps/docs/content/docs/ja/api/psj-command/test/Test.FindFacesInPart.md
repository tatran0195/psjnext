---
title: "Test.FindFacesInPart()"
description: "Find faces in part by typical description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Test > FindFacesInPart"
---

## Description

Find faces in part by typical description

## Syntax

```psj
Test.FindFacesInPart(crPart, strIdentical)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crPart

- Specify the part.

<!-- @since:5.0.1 @required -->
### strIdentical

- Specify the identical.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.FindFacesInPart(crPart, strIdentical)
```
