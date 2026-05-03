---
title: "Analysis.LSDYNAJob()"
description: "Create LS-Dyna Analysis Job"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > LSDYNAJob"
---

## Description

Create LS-Dyna Analysis Job.

## Syntax

```psj
Analysis.LSDYNAJob(...)
```

## Inputs

### `crEdit` @type(Cursor) @default(None)

- The existed analysis job to modify it instead of creating a new ones.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Analysis.LSDYNAJob()
```
