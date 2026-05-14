---
title: "JPT.GetAllSolverJobs()"
description: "Get all the information of solver jobs."
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all the information of solver jobs (job name, steps, job description).

## Syntax

```psj
JPT.GetAllSolverJobs()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[SolverJobVector](../data-type/psj-utility/pre-utility/built-in-types/SolverJobVector)_ object or _List of [DSolverJob](../data-type/psj-utility/pre-utility/built-in-types/DSolverJob)_ objects containing all the information of all the jobs.

## Sample Code

```psj {7}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\JtdbSample\\Get _Infor _Part _Sample.jtdb"
FileMenu.LoadJTDB(strFileName=samplePath)
JPT.ViewFitToModel()

# Get the information of all solver jobs
listJobs = JPT.GetAllSolverJobs()
JPT.Debugger(listJobs) #size = 3

# Declare job variables
ADVC _Job = listJobs[0]
Abaqus _Job = listJobs[1]
Nastran _Job = listJobs[2]

# Access Name/Step/Description of ADVC Job
JPT.Debugger(ADVC _Job)
JPT.Debugger(ADVC _Job.name)
JPT.Debugger(ADVC _Job.jobDescription)
for step in ADVC _Job.jobSteps:
    JPT.Debugger(step)

# Access Name/Step/Description of Abaqus Job
JPT.Debugger(Abaqus _Job)
JPT.Debugger(Abaqus _Job.name)
JPT.Debugger(Abaqus _Job.jobDescription)
for step in Abaqus _Job.jobSteps:
    JPT.Debugger(step)

# Access Name/Step/Description of Nastran Job
JPT.Debugger(Nastran _Job)
JPT.Debugger(Nastran _Job.name)
JPT.Debugger(Nastran _Job.jobSteps) #size = 0, Nastran does not have steps
JPT.Debugger(Nastran _Job.jobDescription)
```
