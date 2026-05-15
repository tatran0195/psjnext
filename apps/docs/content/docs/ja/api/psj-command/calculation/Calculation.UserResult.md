---
title: "Calculation.UserResult()"
description: "Any desired result can be created and added to the document by treating the results as variables and passing them to functions."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > UserResult"
macro _link: "[PostCreateUserResult](../../macro/calculation/ACCombinedAnimation)"
---

## Description

Any desired result can be created and added to the document by treating the results as variables and passing them to functions.

## Syntax

```psj
Calculation.UserResult(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crPostJob

- Specify the target post job.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### iResultVariableType

- Specify the result type to make a variable.
  - 0: Unknown
  - 1: Step
  - 2: Result
  - 3: Component
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### strResultName

- Specify the result name to make a variable.
- The default value is "Expr1".

<!-- @since:5.1.0 @optional -->
### iResultSet

- Specify the result set.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iTimeStep

- Specify the time step.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### listResultVariables

- Specify the attributes of the selected result to make a variable.
- The default value is RESULT\_VARIABLE().

<!-- @since:5.1.0 @optional -->
### bResultExpression

- Specify whether to use the expression to display the result.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bContourExpression

- Specify whether to use the expression to display the contour.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bVectorExpression

- Specify whether to use the expression to display the vector.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bDisplacementExpression

- Specify whether to use the expression to display the displacement.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iVectorType

- Specify the type to display the vector.
  - 0: Vector
  - 1: Magnitude and Direction
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strResultExpression

- Specify the calculation formula of the result used for the result display.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strContourExpression

- Specify the calculation formula for the result used for the contour display.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strVectorExpressionMagnitude

- Specify the calculation formula for the result used for the vector display in magnitude. This variable was used when iVectorType = 1.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strVectorExpressionX

- Specify the calculation formula for the result used for the vector display in X direction.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strVectorExpressionY

- Specify the calculation formula for the result used for the vector display in Y direction.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strVectorExpressionZ

- Specify the calculation formula for the result used for the vector display in Z direction.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strDisplacementExpressionX

- Specify the calculation formula of the result used for the deformation display in X direction.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strDisplacementExpressionY

- Specify the calculation formula of the result used for the deformation display in Y direction.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strDisplacementExpressionZ

- Specify the calculation formula of the result used for the deformation display in Z direction.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### bIncrementName

- Specify whether to input the increment name.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### strIncrementName

- Specify the increment name.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing user result item
  - If this parameter is used, the specified user result item will be modified.
  - If it is left None, a new user result item will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created user result item.

## Sample Code

```psj {6-16}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# User result
result = Calculation.UserResult(crPostJob=TSVPostJob(1), 
                                iResultVariableType=3, 
                                strResultName="Expr _1", 
                                iResultSet=2, 
                                listResultVariables=[RESULT _VARIABLE(crReferencePostJob=TSVPostJob(1), \
                                strName="C1", iAnalysisType=2, iResultSet=1, iTimeStep=1, iResultPos=1), \
                                RESULT _VARIABLE(crReferencePostJob=TSVPostJob(1), strName="C2", \
                                iAnalysisType=2, iResultSet=1, iTimeStep=1, iResultType=1, iResultPos=1)], 
                                bResultExpression=False, 
                                bContourExpression=True, 
                                strContourExpression="C1+C2")
JPT.Debugger(result)
```
