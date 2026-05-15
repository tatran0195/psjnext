---
title: "CmdSetPostUnit()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set post unit in Preference.

## Syntax

```psj
CmdSetPostUnit(int[] origUnit, int[] currUnit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. origUnit::int

Force

<!-- @since:5.0.1 -->
### 2. origUnit::int

Angle

<!-- @since:5.0.1 -->
### 3. origUnit::int

Temperature

<!-- @since:5.0.1 -->
### 4. origUnit::int

Moment

<!-- @since:5.0.1 -->
### 5. origUnit::int

Energy

<!-- @since:5.0.1 -->
### 6. origUnit::int

Power

<!-- @since:5.0.1 -->
### 7. origUnit::int

Displacement

<!-- @since:5.0.1 -->
### 8. origUnit::int

Stress

<!-- @since:5.0.1 -->
### 9. origUnit::int

Velocity

<!-- @since:5.0.1 -->
### 10. origUnit::int

Acceleration

<!-- @since:5.0.1 -->
### 11. origUnit::int

Angle Velocity

<!-- @since:5.0.1 -->
### 12. origUnit::int

Angle Acceleration

<!-- @since:5.0.1 -->
### 13. origUnit::int

Energy Density

<!-- @since:5.0.1 -->
### 14. origUnit::int

Temperature Gradient

<!-- @since:5.0.1 -->
### 15. origUnit::int

HeatFlux

<!-- @since:5.0.1 -->
### 16. currUnit::int

Force

<!-- @since:5.0.1 -->
### 17. currUnit::int

Angle

<!-- @since:5.0.1 -->
### 18. currUnit::int

Temperature

<!-- @since:5.0.1 -->
### 19. currUnit::int

Moment

<!-- @since:5.0.1 -->
### 20. currUnit::int

Energy

<!-- @since:5.0.1 -->
### 21. currUnit::int

Power

<!-- @since:5.0.1 -->
### 22. currUnit::int

Displacement

<!-- @since:5.0.1 -->
### 23. currUnit::int

Stress

<!-- @since:5.0.1 -->
### 24. currUnit::int

Velocity

<!-- @since:5.0.1 -->
### 25. currUnit::int

Acceleration

<!-- @since:5.0.1 -->
### 26. currUnit::int

Angle Velocity

<!-- @since:5.0.1 -->
### 27. currUnit::int

Angle Acceleration

<!-- @since:5.0.1 -->
### 28. currUnit::int

Energy Density,

<!-- @since:5.0.1 -->
### 29. currUnit::int

Temperature Gradient,

<!-- @since:5.0.1 -->
### 30. currUnit::int

Heat Flux

## Return Code

Nothing.

## Sample Code

```psj
CmdSetPostUnit([0, 0, 1, 3, 2, 2, 2, 2, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 3, 2, 2, 2, 2, 1, 1, 0, 0, 1, 1, 1])
```
