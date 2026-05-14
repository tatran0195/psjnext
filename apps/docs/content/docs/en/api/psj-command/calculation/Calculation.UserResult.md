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

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crPostJob`

- The target post job.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iResultVariableType`

- The result type to make a variable.
  - 0: Unknown
  - 1: Step
  - 2: Result
  - 3: Component

<!-- @since:5.1.0 @type:String @optional @default:"Expr1" -->
### `strResultName`

- The result name to make a variable.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iResultSet`

- The result set.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTimeStep`

- The time step.

<!-- @since:5.1.0 @type:List[RESULT _VARIABLE] @optional @default:RESULT _VARIABLE() -->
### `listResultVariables`

- The attributes of the selected result to make a variable.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bResultExpression`

- Whether to use the expression to display the result.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bContourExpression`

- Whether to use the expression to display the contour.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bVectorExpression`

- Whether to use the expression to display the vector.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDisplacementExpression`

- Whether to use the expression to display the displacement.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iVectorType`

- The type to display the vector.
  - 0: Vector
  - 1: Magnitude and Direction

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strResultExpression`

- The calculation formula of the result used for the result display.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strContourExpression`

- The calculation formula for the result used for the contour display.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strVectorExpressionMagnitude`

- The calculation formula for the result used for the vector display in magnitude. This variable was used when iVectorType = 1.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strVectorExpressionX`

- The calculation formula for the result used for the vector display in X direction.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strVectorExpressionY`

- The calculation formula for the result used for the vector display in Y direction.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strVectorExpressionZ`

- The calculation formula for the result used for the vector display in Z direction.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strDisplacementExpressionX`

- The calculation formula of the result used for the deformation display in X direction.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strDisplacementExpressionY`

- The calculation formula of the result used for the deformation display in Y direction.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strDisplacementExpressionZ`

- The calculation formula of the result used for the deformation display in Z direction.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bIncrementName`

- Whether to input the increment name.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strIncrementName`

- The increment name.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing user result item
  - If this parameter is used, the specified user result item will be modified.
  - If it is left None, a new user result item will be created.

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
