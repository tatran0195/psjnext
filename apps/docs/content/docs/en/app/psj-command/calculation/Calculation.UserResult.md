---
title: "Calculation.UserResult()"
description: "Any desired result can be created and added to the document by treating the results as variables and passing them to functions."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > UserResult"
macro_link: "[PostCreateUserResult](../../macro/calculation/ACCombinedAnimation)"
---

## Description

Any desired result can be created and added to the document by treating the results as variables and passing them to functions.

## Syntax

```psj
Calculation.UserResult(...)
```

## Inputs

### `crPostJob` @type(Cursor) @default(None)

- The target post job.

### `iResultVariableType` @type(Integer) @default(1)

- The result type to make a variable.
  - 0: Unknown
  - 1: Step
  - 2: Result
  - 3: Component

### `strResultName` @type(String) @default("Expr1")

- The result name to make a variable.

### `iResultSet` @type(Integer) @default(1)

- The result set.

### `iTimeStep` @type(Integer) @default(1)

- The time step.

### `listResultVariables` @type(List\[RESULT\_VARIABLE]) @default(RESULT\_VARIABLE())

- The attributes of the selected result to make a variable.

### `bResultExpression` @type(Boolean) @default(True)

- Whether to use the expression to display the result.

### `bContourExpression` @type(Boolean) @default(False)

- Whether to use the expression to display the contour.

### `bVectorExpression` @type(Boolean) @default(False)

- Whether to use the expression to display the vector.

### `bDisplacementExpression` @type(Boolean) @default(False)

- Whether to use the expression to display the displacement.

### `iVectorType` @type(Integer) @default(0)

- The type to display the vector.
  - 0: Vector
  - 1: Magnitude and Direction

### `strResultExpression` @type(String) @default("")

- The calculation formula of the result used for the result display.

### `strContourExpression` @type(String) @default("")

- The calculation formula for the result used for the contour display.

### `strVectorExpressionMagnitude` @type(String) @default("")

- The calculation formula for the result used for the vector display in magnitude. This variable was used when iVectorType = 1.

### `strVectorExpressionX` @type(String) @default("")

- The calculation formula for the result used for the vector display in X direction.

### `strVectorExpressionY` @type(String) @default("")

- The calculation formula for the result used for the vector display in Y direction.

### `strVectorExpressionZ` @type(String) @default("")

- The calculation formula for the result used for the vector display in Z direction.

### `strDisplacementExpressionX` @type(String) @default("")

- The calculation formula of the result used for the deformation display in X direction.

### `strDisplacementExpressionY` @type(String) @default("")

- The calculation formula of the result used for the deformation display in Y direction.

### `strDisplacementExpressionZ` @type(String) @default("")

- The calculation formula of the result used for the deformation display in Z direction.

### `bIncrementName` @type(Boolean) @default(False)

- Whether to input the increment name.

### `strIncrementName` @type(String) @default("")

- The increment name.

### `crEdit` @type(Cursor) @default(None)

- An existing user result item
  - If this parameter is used, the specified user result item will be modified.
  - If it is left None, a new user result item will be created.

## Return Code

A _Cursor_ specifying the created user result item.

## Sample Code

```psj {6-16}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# User result
result = Calculation.UserResult(crPostJob=TSVPostJob(1), 
                                iResultVariableType=3, 
                                strResultName="Expr_1", 
                                iResultSet=2, 
                                listResultVariables=[RESULT_VARIABLE(crReferencePostJob=TSVPostJob(1), \
                                strName="C1", iAnalysisType=2, iResultSet=1, iTimeStep=1, iResultPos=1), \
                                RESULT_VARIABLE(crReferencePostJob=TSVPostJob(1), strName="C2", \
                                iAnalysisType=2, iResultSet=1, iTimeStep=1, iResultType=1, iResultPos=1)], 
                                bResultExpression=False, 
                                bContourExpression=True, 
                                strContourExpression="C1+C2")
JPT.Debugger(result)
```
