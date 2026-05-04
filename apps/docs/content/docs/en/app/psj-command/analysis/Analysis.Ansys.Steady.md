---
title: 'Analysis.Ansys.Steady()'
description: 'Export the Ansys Steady Static Heat Transfer solver file'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > Ansys > Steady'
---

## Description

Export the Ansys Steady Static Heat Transfer solver file

## Syntax

```psj
Analysis.Ansys.Steady(...)
```

## Inputs

### `strName` @type(String) @required

- The job name of Ansys analysis.

### `strAnsysJobName` @type(String) @default("Job1")

- The the name of Ansys Steady Static Heat Transfer analysis.

### `strJobName` @type(String) @default("")

- The description for new Ansys analysis.

### `ansysAnalysisBasic` @type(BASIC) @default(BASIC)

- The Ansys Analysis - Linear Static Structure input parameter.

### `bRunAPDL` @type(Boolean) @default(False)

- Enable/disalbe the option that running Ansys Parametric Design Language (APDL).

### `bWriteResultDB` @type(Boolean) @default(False)

- Enable/disalbe the option that write result database.

### `iLoadCaseId` @type(Integer) @default(0)

- The load case identify number .

### `ansysAnalysisSteadyStatic` @type(STEADY_STATIC) @default(STEADY_STATIC)

- The Ansys Analysis - Steady Static Heat Transfer input parameter.

### `strAnsysVersion` @type(String) @default("")

- The Ansys Version information.

### `strCommandLineOption` @type(String) @default("")

- The Command Line Option information.

### `bOutputSOLVE` @type(Boolean) @default(False)

- Enable/disalbe SOLVE command write out.

### `crEdit` @type(Cursor) @default(None)

- The editing ansys job.

### `strFileName` @type(String) @default("")

- The exporting path for .dat file.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-4}
Geometry.Part.Cube()

Analysis.Ansys.Steady("Job1", ansysAnalysisBasic=BASIC(dTimeStepSize=1.0, dMinTimeStep=1.0),
    iLoadCaseId=1, ansysAnalysisSteadyStatic=STEADY_STATIC(bSteadyStaticMemorySave=True), strFileName="D:/Job1.dat")
```
