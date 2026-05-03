---
title: "Analysis.Ansys.LinearStatic()"
description: "Export the Ansys Linear Static Structural solver file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > Ansys > LinearStatic"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Export the Ansys Linear Static Structural solver file.

## Syntax

```psj
Analysis.Ansys.LinearStatic(...)
```

## Inputs

### `strJobName` @type(String) @required

- The job name of Ansys analysis.

### `iVersion` @type(Int) @default(0) @since(5.1.0)

- The version of this command.

### `strAnsysJobName` @type(String) @default("Job1")

- The the name of Ansys Linear Static Structural analysis.

### `strAnsysJobDescription` @type(String) @default("")

- The description for new Ansys analysis.

### `ansysAnalysisBasic` @type(BASIC) @default(BASIC)

- The Ansys Analysis - Linear Static input parameter.

### `bRunAPDL` @type(Boolean) @default(False)

- Enable/disalbe the option that running Ansys Parametric Design Language (APDL).

### `bWriteResultDB` @type(Boolean) @default(False)

- Enable/disalbe the option that write result database.

### `iLoadCaseId` @type(Integer) @default(0)

- The load case identify number.

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

Analysis.Ansys.LinearStatic(strJobName="Job1", iVersion=1, strAnsysJobName="Job1", ansysAnalysisBasic=BASIC(dTimeStepSize=1.0, dMinTimeStep=1.0), iLoadCaseId=1, strFileName="C:/temp/Job1.dat")
```
