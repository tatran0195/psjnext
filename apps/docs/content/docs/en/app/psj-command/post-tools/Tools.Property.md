---
title: "Tools.Property()"
description: "Lists all the information in the output for the selected entity."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Property"
macro_link: "[CmdPostProperty](../../macro/tools/CmdPostProperty)"
---

## Description

Lists all the information in the output for the selected entity.

## Syntax

```psj
Tools.Property(...)
```

## Inputs

### `crTarget` @type(Cursor) @required

- The target to output the information. The target can be Node or Solid element.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=1, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Show node properties
nodeProperty = Tools.Property(crTarget=Node(6699))
JPT.Debugger(nodeProperty)
```
