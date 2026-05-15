---
title: "PostCreateUserResult()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create User Result.

## Syntax

```psj
PostCreateUserResult(cursor crTargetPostJob, int varType, string name, int resultSet, int timeStep, UserResultVar[] variables, bool useResultExp, bool useContourExp, bool useVectorExp, bool useDispExp, bool vectorType, string strResultExp, string strContourExp, string strVectorExpMag, string strVectorExps[0], string strVectorExps[1], string strVectorExps[2], string strDispExps[0], string strDispExps[1], string strDispExps[2], cursor Edit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. cursor

Post Job.

<!-- @since:5.0.1 -->
### 2. int

Variable type

<!-- @since:5.0.1 -->
### 3. string

Result Name.

<!-- @since:5.0.1 -->

#### 4. int

Result set.

<!-- @since:5.0.1 -->

#### 5. int

Time step.

<!-- @since:5.0.1 -->

#### 6. ResultVar\[]

Source results.
ResultVar contents are:

1. cursor - Post Job,
1. string - Name,
1. int - Step,
1. int - inc,
1. int - Result,
1. int - Component,
1. int - Location.

<!-- @since:5.0.1 -->

#### 7.bool

Result Exp. flag

<!-- @since:5.0.1 -->

#### 8. bool

Contour Exp. flag.

<!-- @since:5.0.1 -->

#### 9.bool

Vector Exp. flag.

<!-- @since:5.0.1 -->

#### 10. bool

Disp. Exp. flag.

<!-- @since:5.0.1 -->

#### 11. bool

Vector Type.

<!-- @since:5.0.1 -->

#### 12. string

Result Exp.

<!-- @since:5.0.1 -->

#### 13. string

Contour Exp.

<!-- @since:5.0.1 -->

#### 14. string

Vector Exp Magnitude.

<!-- @since:5.0.1 -->

#### 15. string

Vector Exp X.

<!-- @since:5.0.1 -->

#### 16. string

Vector Exp Y.

<!-- @since:5.0.1 -->

#### 17. string

Vector Exp Z.

<!-- @since:5.0.1 -->

#### 18. string

Disp Exps X.

<!-- @since:5.0.1 -->

#### 19. string

Disp Exps Y.

<!-- @since:5.0.1 -->

#### 20. string

Disp Exps Z.

<!-- @since:5.0.1 -->

#### 21. cursor

Edit

## Return Code

Nothing.

## Sample Code

```psj
PostCreateUserResult(183:1, 3, "Expr1", 2, 1, [[183:1, "C1", 1, 1, 1, 0, 1], [183:1, "C2", 1, 1, 1, 1, 1]], 0, 1, 0, 0, 0, "", "C1*C2", "", "", "", "", "", "", "", 0:0)
```
