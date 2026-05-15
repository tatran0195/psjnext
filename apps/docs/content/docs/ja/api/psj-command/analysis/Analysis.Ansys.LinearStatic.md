---
title: "Analysis.Ansys.LinearStatic()"
description: "Export the Ansys Linear Static Structural solver file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Ansys > LinearStatic"
---

## Description

Export the Ansys Linear Static Structural solver file.

## Syntax

```psj
Analysis.Ansys.LinearStatic(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strJobName

- Specify the job name of Ansys analysis.

<!-- @since:5.1.0 @optional -->
### iVersion

- Specify the version of this command.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strAnsysJobName

- Specify the the name of Ansys Linear Static Structural analysis.
- The default value is "Job1".

<!-- @since:5.0.1 @optional -->
### strAnsysJobDescription

- Specify the description for new Ansys analysis.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### ansysAnalysisBasic

- Specify the Ansys Analysis - Linear Static input parameter.
- The default value is [BASIC](./../../data-type/psj-command/parameter-types/BASIC).

<!-- @since:5.0.1 @optional -->
### bRunAPDL

- Specify running Ansys Parametric Design Language (APDL).
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bWriteResultDB

- Specify write result database.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iLoadCaseId

- Specify the load case identify number.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strAnsysVersion

- Specify the Ansys Version information.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### strCommandLineOption

- Specify the Command Line Option information.
- The default value is "".

### `bOutputSOLVE`

- A _Boolean_ enable/disalbe SOLVE command write out.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the editing ansys job.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### strFileName

- Specify the exporting path for .dat file.
- The default value is "".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-4}
Geometry.Part.Cube()

Analysis.Ansys.LinearStatic(strJobName="Job1", iVersion=1, strAnsysJobName="Job1", ansysAnalysisBasic=BASIC(dTimeStepSize=1.0, dMinTimeStep=1.0), iLoadCaseId=1, strFileName="C:/temp/Job1.dat")
```
