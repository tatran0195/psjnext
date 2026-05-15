---
title: "FindFacesInPart()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Find Faces in a Part.

## Syntax

```psj
FindFacesInPart(Cursor crTargetPart, string strTargetPartString)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Target part cursor (3:Part ID)

<!-- @since:5.0.1 -->
### 2. String

Finding Target(MaxXFACE,MinXFACE,MaxYFACE,MinYFACE,MaxZFACE,MinZFACE)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
JPT.Exec('FindFacesInPart(3:3, "MaxZFACE")')
```
