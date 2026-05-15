---
title: "Analysis.LSDYNAJob()"
description: "Create LS-Dyna Analysis Job"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > LSDYNAJob"
---

## Description

Create LS-Dyna Analysis Job.

## Syntax

```psj
Analysis.LSDYNAJob(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the existed analysis job to modify it instead of creating a new ones.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Analysis.LSDYNAJob()
```
