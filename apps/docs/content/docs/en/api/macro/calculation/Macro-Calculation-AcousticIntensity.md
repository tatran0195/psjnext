---
title: "AcousticIntensity()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Intensity is created from the sound pressure and particle velocity results.

## Syntax

```psj
AcousticIntensity(str strAnalysisName, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- The name of the analysis.

<!-- @since:5.1.0 -->
### 2. cursor

- A Cursor specifying the edit.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AcousticIntensity("MyAcousticIntensity", 0:0)
```
