---
title: "MaterialInfo()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the information in the materials

## Syntax

```psj
MaterialInfo(String MatName,String Info Type)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Material Name

<!-- @since:5.0.1 -->
### 2. String

Info Type (DENSITY or YOUNGMODULUES or POISSONRATIO)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MaterialInfo("Structural _Steel","DENSITY")
```

or

```psj
MaterialInfo("Structural _Steel","YOUNGMODULUES")
```
