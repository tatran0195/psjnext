---
title: "CmdShowPostContour()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Display result in contour

## Syntax

```psj
CmdShowPostContour(Cursor crPostJob,
	PostResultKey& resKey, PostDataOp& opOut,
	bool hasResult2, PostResultKey resKey2, PostDataOp opOut2,
	bool hasResult3, PostResultKey resKey3, PostDataOp opOut3,
	bool enableMidNode, bool bApplyAll)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Cursor of post job.

<!-- @since:5.0.1 -->
### 2. PostResultKey::int

Analysis type.

<!-- @since:5.0.1 -->
### 3. PostResultKey::int

Analysis ID.

<!-- @since:5.0.1 -->
### 4. PostResultKey::int

Result set

<!-- @since:5.1.0 -->
### 5. PostResultKey::int

Time step

<!-- @since:5.0.1 -->
### 6. PostResultKey::string

Name of result

<!-- @since:5.1.0 -->
### 7. PostResultKey::string

Name of component

<!-- @since:5.1.0 -->
### 8. PostResultKey::int

Position of result

<!-- @since:5.0.1 -->
### 9. PostDataOp::int

Display at

<!-- @since:5.0.1 -->
### 10. PostDataOp::int

Coordinate

<!-- @since:5.0.1 -->
### 11. PostDataOp::int

1D Data

<!-- @since:5.0.1 -->
### 12. PostDataOp::int

2D Data

<!-- @since:5.0.1 -->
### 13. PostDataOp::int

Conversion

<!-- @since:5.0.1 -->
### 14. PostDataOp::int

Display of connection

<!-- @since:5.1.0 -->
### 15. PostDataOp::int

Complex.

<!-- @since:5.1.0 -->
### 16. PostDataOp::double

Phase angle.

<!-- @since:5.1.0 -->
### 17. PostDataOp::int

Id of coordinate.

<!-- @since:5.1.0 -->
### 18. bool

Whether it uses 2nd result or not.

<!-- @since:5.0.1 -->
### 19. PostResultKey::int

Analysis type of 2nd result.

<!-- @since:5.0.1 -->
### 20. PostResultKey::int

Result set of 2nd result.

<!-- @since:5.1.0 -->
### 21. PostResultKey::int

Time step of 2nd result.

<!-- @since:5.0.1 -->
### 22. PostResultKey::string

Name of result of 2nd result.

<!-- @since:5.1.0 -->
### 23. PostResultKey::string

Name of component of 2nd result.

<!-- @since:5.1.0 -->
### 24. PostResultKey::int

Position of result of 2nd result.

<!-- @since:5.0.1 -->
### 25. PostDataOp::int

Display of 2nd result.

<!-- @since:5.0.1 -->
### 26. PostDataOp::int

Type of coordinate of 2nd result.

<!-- @since:5.0.1 -->
### 27. PostDataOp::int

1D data of 2nd result.

<!-- @since:5.0.1 -->
### 28. PostDataOp::int

2D data of 2nd result.

<!-- @since:5.0.1 -->
### 29. PostDataOp::int

Conversion of 2nd result.

<!-- @since:5.0.1 -->
### 30. PostDataOp::int

Display of connection of 2nd result.

<!-- @since:5.1.0 -->
### 31. PostDataOp::int

Complex of 2nd result.

<!-- @since:5.1.0 -->
### 32. PostDataOp::double

Phase angle of 2nd result.

<!-- @since:5.1.0 -->
### 33. PostDataOp::int

Id of coordinate of 2nd result.

<!-- @since:5.1.0 -->
### 34. bool

Whether it uses 3rd result or not.

<!-- @since:5.0.1 -->
### 35. PostResultKey::int

Analysis type of 3rd result.

<!-- @since:5.0.1 -->
### 36. PostResultKey::int

Result set of 3rd result.

<!-- @since:5.1.0 -->
### 37. PostResultKey::int

Time step of 3rd result.

<!-- @since:5.0.1 -->
### 38. PostResultKey::string

Name of result of 3rd result.

<!-- @since:5.1.0 -->
### 39. PostResultKey::string

Name of component of 3rd result.

<!-- @since:5.1.0 -->
### 40. PostResultKey::int

Position of result of 3rd result.

<!-- @since:5.0.1 -->
### 41. PostDataOp::int

Display of 3rd result.

<!-- @since:5.0.1 -->
### 42. PostDataOp::int

Type of coordinate of 3rd result.

<!-- @since:5.0.1 -->
### 43. PostDataOp::int

1D data of 3rd result.

<!-- @since:5.0.1 -->
### 44. PostDataOp::int

2D data of 3rd result.

<!-- @since:5.0.1 -->
### 45. PostDataOp::int

Conversion of 3rd result.

<!-- @since:5.0.1 -->
### 46. PostDataOp::int

Display of connection of 3rd result.

<!-- @since:5.1.0 -->
### 47. PostDataOp::int

Complex of 3rd result.

<!-- @since:5.1.0 -->
### 48. PostDataOp::double

Phase angle of 3rd result.

<!-- @since:5.1.0 -->
### 49. PostDataOp::int

Id of coordinate of 3rd result.

<!-- @since:5.0.1 -->
### 50. bool

Enables or not MidNode.

<!-- @since:5.1.0 -->
### 51. bool

Enalbes or not for all documents.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 5. PostResultKey::string

Name of result

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 7. PostResultKey::int

Position of result

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 8. PostDataOp::int

Display at

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 15. PostDataOp::double

Phase angle.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 16. PostDataOp::int

Id of coordinate.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 17. bool

Whether it uses 2nd result or not.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 18. PostResultKey::int

Analysis type of 2nd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 21. PostResultKey::string

Name of result of 2nd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 23. PostResultKey::int

Position of result of 2nd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 24. PostDataOp::int

Display of 2nd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 31. PostDataOp::double

Phase angle of 2nd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 32. PostDataOp::int

Id of coordinate of 2nd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 33. bool

Whether it uses 3rd result or not.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 34. PostResultKey::int

Analysis type of 3rd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 37. PostResultKey::string

Name of result of 3rd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 39. PostResultKey::int

Position of result of 3rd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 40. PostDataOp::int

Display of 3rd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 47. PostDataOp::double

Phase angle of 3rd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 48. PostDataOp::int

Id of coordinate of 3rd result.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 49. bool

Enables or not MidNode.

## Return Code

Nothing.

## Sample Code

```psj
CmdShowPostContour(183:1, {2, 0, 1, 1, Displacement, Translational, 1}, {1, 1, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)
```
