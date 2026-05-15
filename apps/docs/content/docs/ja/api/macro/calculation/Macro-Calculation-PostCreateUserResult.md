---
title: "PostCreateUserResult()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Read the result and create a new result by using the result in Jupiter as a variable.

## Syntax

```psj
PostCreateUserResult(cursor crTargetPostJob, int iResultVarType, str strName, int iResultSet, int iTimeStep, list listResultVariables, bool bUseResultExpression, bool bUseContourExpression, bool bUseVectorExpression, bool bUseDisplacementExpression, int iVectorType, str strResultExpression, str strContourExpression, str strVectorExpressionMagnitude, str strVectorExpression0, str strVectorExpression1, str strVectorExpression2, str strDisplacementExpression0, str strDisplacementExpression1, str strDisplacementExpression2, bool bIncrementName, str strIncrementName, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

- A Cursor specifying the target post job.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying the result type to make a variable.

<!-- @since:5.1.0 -->
### 3. str

- A String specifying the result name to make a variable.

<!-- @since:5.1.0 -->
### 4. int

- An Integer specifying the result set.

<!-- @since:5.1.0 -->
### 5. int

- An Integer specifying the time step.

<!-- @since:5.1.0 -->
### 6. list

- A List of RESULT\_VARIABLE specifying the attributes of the selected result to make a variable.

<!-- @since:5.1.0 -->
### 7. bool

- A Boolean specifying whether to use the expression to display the result.

<!-- @since:5.1.0 -->
### 8. bool

- A Boolean specifying whether to use the expression to display the contour.

<!-- @since:5.1.0 -->
### 9. bool

- A Boolean specifying whether to use the expression to display the vector.

<!-- @since:5.1.0 -->
### 10. bool

- A Boolean specifying whether to use the expression to display the displacement.

<!-- @since:5.1.0 -->
### 11. int

- An Integer specifying the type to display the vector.

<!-- @since:5.1.0 -->
### 12. str

- A String specifying the calculation formula of the result used for the result display.

<!-- @since:5.1.0 -->
### 13. str

- A String specifying the calculation formula for the result used for the contour display.

<!-- @since:5.1.0 -->
### 14. str

- A String specifying the calculation formula for the result used for the vector display in magnitude. This variable was used when iVectorType = 1.

<!-- @since:5.1.0 -->
### 15. str

- A String specifying the calculation formula for the result used for the vector display in X direction.

<!-- @since:5.1.0 -->
### 16. str

- A String specifying the calculation formula for the result used for the vector display in Y direction.

<!-- @since:5.1.0 -->
### 17. str

- A String specifying the calculation formula for the result used for the vector display in Z direction.

<!-- @since:5.1.0 -->
### 18. str

- A String specifying the calculation formula of the result used for the deformation display in X direction.

<!-- @since:5.1.0 -->
### 19. str

- A String specifying the calculation formula of the result used for the deformation display in Y direction.

<!-- @since:5.1.0 -->
### 20. str

- A String specifying the calculation formula of the result used for the deformation display in Z direction.

<!-- @since:5.1.0 -->
### 21. bool

- A Boolean specifying whether to input the increment name.

<!-- @since:5.1.0 -->
### 22. str

- A String specifying the increment name.

<!-- @since:5.1.0 -->
### 23. cursor

- A Cursor specifying an existing user result item

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostCreateUserResult(183:1, 3, "Expr _1", 2, 1, [[183:1, "C1", 2, 1, 1, 0, 1], [183:1, "C2", 2, 1, 1, 1, 1]], 0, 1, 0, 0, 0, "", "C1+C2", "", "", "", "", "", "", "", 0, "", 0:0)
```
