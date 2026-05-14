---
title: Material Unit Types
id: material-unit-types
---

This is an enumeration type represents type of Material Unit in Jupiter.

They used as _JPT.UnitType.KeyName_ to specify unit for material.

Here are the _UnitType_ and _KeyName_.

<details>

Available units for length.

<summary> **`LengthUnit`** </summary>

| ID | Key Name   | Usage                     | Description |
| -- | ---------- | ------------------------- | ----------- |
| 0  | Length\_mm | JPT.LengthUnit.Length\_mm | $mm$        |
| 1  | Length\_m  | JPT.LengthUnit.Length\_m  | $m$         |
| 2  | Length\_ft | JPT.LengthUnit.Length\_ft | $ft$        |
| 3  | Length\_in | JPT.LengthUnit.Length\_in | $in$        |
| 4  | Length\_cm | JPT.LengthUnit.Length\_cm | $cm$        |

</details>

<details>

Available units for time.

<summary> **`TimeUnit`** </summary>

| ID | Key Name  | Usage                  | Description |
| -- | --------- | ---------------------- | ----------- |
| 0  | Time\_s   | JPT.TimeUnit.Time\_s   | $s$         |
| 1  | Time\_min | JPT.TimeUnit.Time\_min | $min$       |
| 2  | Time\_h   | JPT.TimeUnit.Time\_h   | $h$         |

</details>

<details>

Available units for mass.

<summary> **`MassUnit`** </summary>

| ID | Key Name        | Usage                        | Description   |
| -- | --------------- | ---------------------------- | ------------- |
| 0  | Mass\_t         | JPT.MassUnit.Mass\_t         | $t$           |
| 1  | Mass\_kg        | JPT.MassUnit.Mass\_kg        | $kg$          |
| 2  | Mass\_kgfs2\_mm | JPT.MassUnit.Mass\_kgfs2\_mm | $kgf\*s^2/mm$ |
| 3  | Mass\_slug      | JPT.MassUnit.Mass\_slug      | $slug$        |
| 4  | Mass\_lbfs2\_in | JPT.MassUnit.Mass\_lbfs2\_in | $lbf\*s^2/in$ |
| 5  | Mass\_lb        | JPT.MassUnit.Mass\_lb        | $lb$          |
| 6  | Mass\_g         | JPT.MassUnit.Mass\_g         | $g$           |

</details>

<details>

Available units for force.

<summary> **`ForceUnit`** </summary>

| ID | Key Name   | Usage                    | Description |
| -- | ---------- | ------------------------ | ----------- |
| 0  | Force\_N   | JPT.ForceUnit.Force\_N   | $N$         |
| 1  | Force\_mN  | JPT.ForceUnit.Force\_mN  | $mN$        |
| 2  | Force\_kN  | JPT.ForceUnit.Force\_kN  | $kN$        |
| 3  | Force\_kgf | JPT.ForceUnit.Force\_kgf | $kgf$       |
| 4  | Force\_lbf | JPT.ForceUnit.Force\_lbf | $lbf$       |
| 5  | Force\_tf  | JPT.ForceUnit.Force\_tf  | $tf$        |

</details>

<details>

Available units for angle.

<summary> **`AngleUnit`** </summary>

| ID | Key Name      | Usage                       | Description |
| -- | ------------- | --------------------------- | ----------- |
| 0  | Angle\_rad    | JPT.AngleUnit.Angle\_rad    | $deg$       |
| 1  | Angle\_degree | JPT.AngleUnit.Angle\_degree | $rad$       |

</details>

<details>

Available units for temperature.

<summary> **`TemperatureUnit`** </summary>

| ID | Key Name          | Usage                                 | Description |
| -- | ----------------- | ------------------------------------- | ----------- |
| 0  | Temperature\_K    | JPT.TemperatureUnit.Temperature\_K    | $K$         |
| 1  | Temperature\_degC | JPT.TemperatureUnit.Temperature\_degC | $deg C$     |
| 2  | Temperature\_degF | JPT.TemperatureUnit.Temperature\_degF | $deg F$     |

</details>

<details>

Available units for Area.

<summary> **`AreaUnit`** </summary>

| ID | Key Name  | Usage                  | Description |
| -- | --------- | ---------------------- | ----------- |
| 0  | Area\_mm2 | JPT.AreaUnit.Area\_mm2 | $mm^2$      |
| 1  | Area\_m2  | JPT.AreaUnit.Area\_m2  | $m^2$       |
| 2  | Area\_ft2 | JPT.AreaUnit.Area\_ft2 | $ft^2$      |
| 3  | Area\_in2 | JPT.AreaUnit.Area\_in2 | $in^2$      |
| 4  | Area\_cm2 | JPT.AreaUnit.Area\_cm2 | $cm^2$      |

</details>

<details>

Available units for Volume.

<summary> **`VolumeUnit`** </summary>

| ID | Key Name    | Usage                      | Description |
| -- | ----------- | -------------------------- | ----------- |
| 0  | Volume\_mm3 | JPT.VolumeUnit.Volume\_mm3 | $mm^3$      |
| 1  | Volume\_m3  | JPT.VolumeUnit.Volume\_m3  | $m^3$       |
| 2  | Volume\_ft3 | JPT.VolumeUnit.Volume\_ft3 | $ft^3$      |
| 3  | Volume\_in3 | JPT.VolumeUnit.Volume\_in3 | $in^3$      |
| 4  | Volume\_cm3 | JPT.VolumeUnit.Volume\_cm3 | $cm^3$      |

</details>

<details>

Available units for Velocity.

<summary> **`VelocityUnit`** </summary>

| ID | Key Name        | Usage                            | Description |
| -- | --------------- | -------------------------------- | ----------- |
| 0  | Velocity\_mm\_s | JPT.VelocityUnit.Velocity\_mm\_s | $s$         |
| 1  | Velocity\_m\_s  | JPT.VelocityUnit.Velocity\_m\_s  | $m/s$       |
| 2  | Velocity\_ft\_s | JPT.VelocityUnit.Velocity\_ft\_s | $ft/s$      |
| 3  | Velocity\_in\_s | JPT.VelocityUnit.Velocity\_in\_s | $in/s$      |

</details>

<details>

Available units for Acceleration.

<summary> **`AccelerationUnit`** </summary>

| ID | Key Name             | Usage                                     | Description |
| -- | -------------------- | ----------------------------------------- | ----------- |
| 0  | Acceleration\_mm\_s2 | JPT.AccelerationUnit.Acceleration\_mm\_s2 | $s$         |
| 1  | Acceleration\_m\_s2  | JPT.AccelerationUnit.Acceleration\_m\_s2  | $m/s$       |
| 2  | Acceleration\_ft\_s2 | JPT.AccelerationUnit.Acceleration\_ft\_s2 | $ft/s$      |
| 3  | Acceleration\_in\_s2 | JPT.AccelerationUnit.Acceleration\_in\_s2 | $in/s$      |
| 4  | Acceleration\_g      | JPT.AccelerationUnit.Acceleration\_g      | $g$         |
| 5  | Acceleration\_Gal    | JPT.AccelerationUnit.Acceleration\_Gal    | $Gal$       |

</details>

<details>

Available units for rotational velocity.

<summary> **`RotateVeloUnit`** </summary>

| ID | Key Name           | Usage                                 | Description |
| -- | ------------------ | ------------------------------------- | ----------- |
| 0  | RotateVelo\_rad\_s | JPT.RotateVeloUnit.RotateVelo\_rad\_s | $rad/s$     |
| 1  | RotateVelo\_deg\_s | JPT.RotateVeloUnit.RotateVelo\_deg\_s | $deg/s$     |
| 2  | RotateVelo\_rpm    | JPT.RotateVeloUnit.RotateVelo\_rpm    | $rpm$       |

</details>

<details>

Available units for rotational acceleration.

<summary> **`RotateAccUnit`** </summary>

| ID | Key Name           | Usage                                | Description |
| -- | ------------------ | ------------------------------------ | ----------- |
| 0  | RotateAcc\_rad\_s2 | JPT.RotateAccUnit.RotateAcc\_rad\_s2 | $rad/s^2$   |
| 1  | RotateAcc\_deg\_s2 | JPT.RotateAccUnit.RotateAcc\_deg\_s2 | $deg/s^2$   |

</details>

<details>

Available units for moment.

<summary> **`MomentUnit`** </summary>

| ID | Key Name      | Usage                        | Description |
| -- | ------------- | ---------------------------- | ----------- |
| 0  | Moment\_Nmm   | JPT.MomentUnit.Moment\_Nmm   | $N\*mm$     |
| 1  | Moment\_Nm    | JPT.MomentUnit.Moment\_Nm    | $N\*m$      |
| 2  | Moment\_mNmm  | JPT.MomentUnit.Moment\_mNmm  | $mN\*mm$    |
| 3  | Moment\_kgfmm | JPT.MomentUnit.Moment\_kgfmm | $kgf\*mm$   |
| 4  | Moment\_lbfft | JPT.MomentUnit.Moment\_lbfft | $lbf\*ft$   |
| 5  | Moment\_lbfin | JPT.MomentUnit.Moment\_lbfin | $lbf\*in$   |
| 6  | Moment\_kgfcm | JPT.MomentUnit.Moment\_kgfcm | $tf\*m$     |

</details>

<details>

Available units for pressure.

<summary> **`PressureUnit`** </summary>

| ID | Key Name           | Usage                               | Description |
| -- | ------------------ | ----------------------------------- | ----------- |
| 0  | Pressure\_MPa      | JPT.PressureUnit.Pressure\_MPa      | $MPa$       |
| 1  | Pressure\_Pa       | JPT.PressureUnit.Pressure\_Pa       | $Pa$        |
| 2  | Pressure\_kPa      | JPT.PressureUnit.Pressure\_kPa      | $kPa$       |
| 3  | Pressure\_kgf\_mm2 | JPT.PressureUnit.Pressure\_kgf\_mm2 | $kgf/mm^2$  |
| 4  | Pressure\_lbf\_ft2 | JPT.PressureUnit.Pressure\_lbf\_ft2 | $lbf/ft^2$  |
| 5  | Pressure\_lbf\_in2 | JPT.PressureUnit.Pressure\_lbf\_in2 | $lbf/in^2$  |
| 6  | Pressure\_tf\_m2   | JPT.PressureUnit.Pressure\_tf\_m2   | $tf/m^2$    |
| 7  | Pressure\_GPa      | JPT.PressureUnit.Pressure\_GPa      | $GPa$       |

</details>

<details>

Available units for density.

<summary> **`DensityUnit`** </summary>

| ID | Key Name            | Usage                | Description |
| -- | ------------------- | -------------------- | ----------- |
| 0  | Density\_t\_mm3     | Density\_t\_mm3      | $$          |
| 1  | Density\_kg\_m3     | Density\_kg\_m3      | $$          |
| 2  | Density\_kg\_mm3    | Density\_kg\_mm3     | $$          |
| 3  | Density\_kgfs2\_mm4 | Density\_kgfs2\_mm$$ |             |
| 4  | Density\_slug\_ft3  | Density\_slug\_ft3   | $$          |
| 5  | Density\_lbfs2\_in4 | Density\_lbfs2\_in4  | $$          |

</details>

<details>

Available units for stiffness.

<summary> **`StiffnessUnit`** </summary>

| ID | Key Name           | Usage                                | Description |
| -- | ------------------ | ------------------------------------ | ----------- |
| 0  | Stiffness\_N\_mm   | JPT.StiffnessUnit.Stiffness\_N\_mm   | $mm$        |
| 1  | Stiffness\_N\_m    | JPT.StiffnessUnit.Stiffness\_N\_m    | $N/m$       |
| 2  | Stiffness\_mN\_mm  | JPT.StiffnessUnit.Stiffness\_mN\_mm  | $mN/mmn$    |
| 3  | Stiffness\_kgf\_mm | JPT.StiffnessUnit.Stiffness\_kgf\_mm | $kgf/mm$    |
| 4  | Stiffness\_lbf\_ft | JPT.StiffnessUnit.Stiffness\_lbf\_ft | $lbf/ft$    |
| 5  | Stiffness\_lbf\_in | JPT.StiffnessUnit.Stiffness\_lbf\_in | $lbf/in$    |

</details>

<details>

Available units for rotational stiffness.

<summary> **`RotateStiffUnit`** </summary>

| ID | Key Name                | Usage                                       | Description   |
| -- | ----------------------- | ------------------------------------------- | ------------- |
| 0  | RotateStiff\_Nmm\_rad   | JPT.RotateStiffUnit.RotateStiff\_Nmm\_rad   | $N\*mm/rad$   |
| 1  | RotateStiff\_Nm\_rad    | JPT.RotateStiffUnit.RotateStiff\_Nm\_rad    | $N\*m/rad$    |
| 2  | RotateStiff\_mNmm\_rad  | JPT.RotateStiffUnit.RotateStiff\_mNmm\_rad  | $mN\*mm/rad$  |
| 3  | RotateStiff\_kgfmm\_rad | JPT.RotateStiffUnit.RotateStiff\_kgfmm\_rad | $kgf\*mm/rad$ |
| 4  | RotateStiff\_lbfft\_rad | JPT.RotateStiffUnit.RotateStiff\_lbfft\_rad | $lbf\*ft/rad$ |
| 5  | RotateStiff\_lbfin\_rad | JPT.RotateStiffUnit.RotateStiff\_lbfin\_rad | $lbf\*in/rad$ |
| 6  | RotateStiff\_Nmm\_deg   | JPT.RotateStiffUnit.RotateStiff\_Nmm\_deg   | $\N\*mm/deg$  |
| 7  | RotateStiff\_mNmm\_deg  | JPT.RotateStiffUnit.RotateStiff\_mNmm\_deg  | $\mN\*mm/deg$ |

</details>

<details>

Available units for damping coefficient.

<summary> **`DampCoefUnit`** </summary>

Available units for rotational stiffness.

| ID | Key Name           | Usage                               | Description |
| -- | ------------------ | ----------------------------------- | ----------- |
| 1  | DampCoef\_Ns\_mm   | JPT.DampCoefUnit.DampCoef\_Ns\_mm   | $N\*s/mm$   |
| 2  | DampCoef\_Ns\_m    | JPT.DampCoefUnit.DampCoef\_Ns\_m    | $N\*s/m$    |
| 3  | DampCoef\_mNs\_mm  | JPT.DampCoefUnit.DampCoef\_mNs\_mm  | $mN\*s/mm$  |
| 4  | DampCoef\_kgfs\_mm | JPT.DampCoefUnit.DampCoef\_kgfs\_mm | $kgf\*s/mm$ |
| 5  | DampCoef\_lbfs\_ft | JPT.DampCoefUnit.DampCoef\_lbfs\_ft | $lbf\*s/ft$ |
| 6  | DampCoef\_lbfs\_in | JPT.DampCoefUnit.DampCoef\_lbfs\_in | $lbf\*s/in$ |

</details>

<details>

Available units for rotational damping coefficient.

<summary> **`RotateDampCoefUnit`** </summary>

| ID | Key Name                    | Usage                                              | Description                        |
| -- | --------------------------- | -------------------------------------------------- | ---------------------------------- |
| 0  | RotateDampCoef\_Nmms\_rad   | JPT.RotateDampCoefUnit.RotateDampCoef\_Nmms\_rad   | $&#x4E;_&#x6D;&#x6D;_&#x73;/rad$   |
| 1  | RotateDampCoef\_Nms\_rad    | JPT.RotateDampCoefUnit.RotateDampCoef\_Nms\_rad    | $&#x4E;_&#x6D;&#x6D;_&#x73;/rad$   |
| 2  | RotateDampCoef\_mNmms\_rad  | JPT.RotateDampCoefUnit.RotateDampCoef\_mNmms\_rad  | $m&#x4E;_&#x6D;&#x6D;_&#x73;/rad$  |
| 3  | RotateDampCoef\_kgfmms\_rad | JPT.RotateDampCoefUnit.RotateDampCoef\_kgfmms\_rad | $kg&#x66;_&#x6D;&#x6D;_&#x73;/rad$ |
| 4  | RotateDampCoef\_lbffts\_rad | JPT.RotateDampCoefUnit.RotateDampCoef\_lbffts\_rad | $lb&#x66;_&#x66;&#x74;_&#x73;/rad$ |
| 5  | RotateDampCoef\_lbfins\_rad | JPT.RotateDampCoefUnit.RotateDampCoef\_lbfins\_rad | $lb&#x66;_&#x69;&#x6E;_&#x73;/rad$ |
| 6  | RotateDampCoef\_Nmms\_deg   | JPT.RotateDampCoefUnit.RotateDampCoef\_Nmms\_deg   | $&#x4E;_&#x6D;&#x6D;_&#x73;/deg$   |
| 7  | RotateDampCoef\_mNmms\_deg  | JPT.RotateDampCoefUnit.RotateDampCoef\_mNmms\_deg  | $m&#x4E;_&#x6D;&#x6D;_&#x73;/deg$  |

</details>

<details>

Available units for elastic modulus.

<summary> **`ModulusUnit`** </summary>

| ID | Key Name          | Usage                             | Description |
| -- | ----------------- | --------------------------------- | ----------- |
| 0  | Modulus\_N\_mm2   | JPT.ModulusUnit.Modulus\_N\_mm2   | $N/mm^2$    |
| 1  | Modulus\_N\_m2    | JPT.ModulusUnit.Modulus\_N\_m2    | $N/m^2$     |
| 2  | Modulus\_mN\_mm2  | JPT.ModulusUnit.Modulus\_mN\_mm2  | $mN/mm^2$   |
| 3  | Modulus\_kgf\_mm2 | JPT.ModulusUnit.Modulus\_kgf\_mm2 | $kgf/mm^2$  |
| 4  | Modulus\_lbf\_ft2 | JPT.ModulusUnit.Modulus\_lbf\_ft2 | $lbf/ft^2$  |
| 5  | Modulus\_lbf\_in2 | JPT.ModulusUnit.Modulus\_lbf\_in2 | $lbf/in^2$  |

</details>

<details>

Available units for energy.

<summary> **`EnergyUnit`** </summary>

| ID | Key Name      | Usage                        | Description |
| -- | ------------- | ---------------------------- | ----------- |
| 1  | Energy\_mJ    | JPT.EnergyUnit.Energy\_mJ    | $mJ$        |
| 2  | Energy\_J     | JPT.EnergyUnit.Energy\_J     | $J$         |
| 3  | Energy\_miuJ  | JPT.EnergyUnit.Energy\_miuJ  | $miuJ$      |
| 4  | Energy\_kCal  | JPT.EnergyUnit.Energy\_kCal  | $kcal$      |
| 5  | Energy\_ftlbf | JPT.EnergyUnit.Energy\_ftlbf | $ft\*lbf$   |
| 6  | Energy\_inlbf | JPT.EnergyUnit.Energy\_inlbf | $in\*lbf$   |
| 7  | Energy\_kJ    | JPT.EnergyUnit.Energy\_kJ    | $kJ$        |
| 8  | Energy\_cal   | JPT.EnergyUnit.Energy\_cal   | $cal$       |

</details>

<details>

Available units for power.

<summary> **`PowerUnit`** </summary>

| ID | Key Name        | Usage                         | Description |
| -- | --------------- | ----------------------------- | ----------- |
| 0  | Power\_mW       | JPT.PowerUnit.Power\_mW       | $mW$        |
| 1  | Power\_W        | JPT.PowerUnit.Power\_W        | $W$         |
| 2  | Power\_miuW     | JPT.PowerUnit.Power\_miuW     | $miuW$      |
| 3  | Power\_kcal\_s  | JPT.PowerUnit.Power\_kcal\_s  | $kcal/s$    |
| 4  | Power\_ftlbf\_s | JPT.PowerUnit.Power\_ftlbf\_s | $ft\*lbf/s$ |
| 5  | Power\_inlbf\_s | JPT.PowerUnit.Power\_inlbf\_s | $in\*lbf/s$ |

</details>

<details>

Available units for coefficient of linear expansion

<summary> **`ThermalExCoefUnit`** </summary>

| ID | Key Name                   | Usage                                            | Description |
| -- | -------------------------- | ------------------------------------------------ | ----------- |
| 0  | ThermalExCoe&#x66;_&#x4B;_ | JPT.ThermalExCoefUnit.ThermalExCoe&#x66;_&#x4B;_ | $/K$        |

</details>

<details>

Available units for thermal conductivity

<summary> **`ThermalConductUnit`** </summary>

| ID | Key Name                   | Usage                                             | Description                  |
| -- | -------------------------- | ------------------------------------------------- | ---------------------------- |
| 0  | ThermalConduct\_mW\_mmK    | JPT.ThermalConductUnit.ThermalConduct\_mW\_mmK    | $mW/mm\*K$                   |
| 1  | ThermalConduct\_W\_mK      | JPT.ThermalConductUnit.ThermalConduct\_W\_mK      | $W/m\*K$                     |
| 2  | ThermalConduct\_miuW\_mmK  | JPT.ThermalConductUnit.ThermalConduct\_miuW\_mmK  | $miuW/mm\*K$                 |
| 3  | ThermalConduct\_kcal\_mmhK | JPT.ThermalConductUnit.ThermalConduct\_kcal\_mmhK | $kcal/m&#x6D;_&#x68;_&#x4B;$ |
| 4  | ThermalConduct\_lbf\_sK    | JPT.ThermalConductUnit.ThermalConduct\_lbf\_sK    | $lbf/s\*K$                   |

</details>

<details>

Available units for Convection coefficient

<summary> **`HeatTransCoefUnit`** </summary>

| ID | Key Name                   | Usage                                            | Description                  |
| -- | -------------------------- | ------------------------------------------------ | ---------------------------- |
| 1  | HeatTransCoef\_mW\_mm2K    | JPT.HeatTransCoefUnit.HeatTransCoef\_mW\_mm2K    | $mW/mm\*K$                   |
| 2  | HeatTransCoef\_W\_m2K      | JPT.HeatTransCoefUnit.HeatTransCoef\_W\_m2K      | $W/m\*K$                     |
| 3  | HeatTransCoef\_miuW\_mm2K  | JPT.HeatTransCoefUnit.HeatTransCoef\_miuW\_mm2K  | $miuW/mm\*K$                 |
| 4  | HeatTransCoef\_kcal\_mm2hK | JPT.HeatTransCoefUnit.HeatTransCoef\_kcal\_mm2hK | $kcal/m&#x6D;_&#x68;_&#x4B;$ |
| 5  | HeatTransCoef\_lbf\_ftsK   | JPT.HeatTransCoefUnit.HeatTransCoef\_lbf\_ftsK   | $lbf/f&#x74;_&#x73;_&#x4B;$  |
| 6  | HeatTransCoef\_lbf\_insK   | JPT.HeatTransCoefUnit.HeatTransCoef\_lbf\_insK   | $lbf/i&#x6E;_&#x73;_&#x4B;$  |

</details>

<details>

Available units for specific heat.

<summary> **`SpecificHeatUnit`** </summary>

| ID | Key Name                   | Usage                                           | Description                         |
| -- | -------------------------- | ----------------------------------------------- | ----------------------------------- |
| 0  | SpecificHeat\_mJ\_tK       | JPT.SpecificHeatUnit.SpecificHeat\_mJ\_tK       | $mJ/t\*K$                           |
| 1  | SpecificHeat\_J\_kgK       | JPT.SpecificHeatUnit.SpecificHeat\_J\_kgK       | $J/kg\*K$                           |
| 2  | SpecificHeat\_miuJ\_kgK    | JPT.SpecificHeatUnit.SpecificHeat\_miuJ\_kgK    | $miuJ/kg\*K$                        |
| 3  | SpecificHeat\_kcal\_kgK    | JPT.SpecificHeatUnit.SpecificHeat\_kcal\_kgK    | $kcal/kg\*K$                        |
| 4  | SpecificHeat\_ftlbf\_slugK | JPT.SpecificHeatUnit.SpecificHeat\_ftlbf\_slugK | $f&#x74;_&#x6C;bf/slu&#x67;_&#x4B;$ |
| 5  | SpecificHeat\_in2\_s2K     | JPT.SpecificHeatUnit.SpecificHeat\_in2\_s2K     | $in^2/s^2\*K$                       |

</details>

<details>

Available units for heat flux.

<summary> **`HeatFluxUnit`** </summary>

| ID | Key Name             | Usage                                 | Description    |
| -- | -------------------- | ------------------------------------- | -------------- |
| 0  | HeatFlux\_mW\_mm2    | JPT.HeatFluxUnit.HeatFlux\_mW\_mm2    | $mW/mm^2$      |
| 1  | HeatFlux\_W\_m2      | JPT.HeatFluxUnit.HeatFlux\_W\_m2      | $W/m^2$        |
| 2  | HeatFlux\_miuW\_mm2  | JPT.HeatFluxUnit.HeatFlux\_miuW\_mm2  | $miuW/mm^2$    |
| 3  | HeatFlux\_kcal\_mm2h | JPT.HeatFluxUnit.HeatFlux\_kcal\_mm2h | $kcal/mm^2\*h$ |
| 4  | HeatFlux\_lbf\_fts   | JPT.HeatFluxUnit.HeatFlux\_lbf\_fts   | $lbf/ft\*s$    |
| 5  | HeatFlux\_lbf\_ins   | JPT.HeatFluxUnit.HeatFlux\_lbf\_ins   | $lbf/in\*s$    |

</details>

<details>

Available units for heat generation.

<summary> **`HeatGenerationUnit`** </summary>

| ID | Key Name                   | Usage                                             | Description     |
| -- | -------------------------- | ------------------------------------------------- | --------------- |
| 1  | HeatGeneration\_mW\_mm3    | JPT.HeatGenerationUnit.HeatGeneration\_mW\_mm3    | $mW/mm^3$       |
| 2  | HeatGeneration\_W\_m3      | JPT.HeatGenerationUnit.HeatGeneration\_W\_m3      | $W/m^3$         |
| 3  | HeatGeneration\_miuW\_mm3  | JPT.HeatGenerationUnit.HeatGeneration\_miuW\_mm3  | $miuW/mm^3$     |
| 4  | HeatGeneration\_kcal\_mm3h | JPT.HeatGenerationUnit.HeatGeneration\_kcal\_mm3h | $kcal//mm^3\*h$ |
| 5  | HeatGeneration\_lbf\_ft2s  | JPT.HeatGenerationUnit.HeatGeneration\_lbf\_ft2s  | $lbf/ft^2\*s$   |
| 6  | HeatGeneration\_lbf\_in2s  | JPT.HeatGenerationUnit.HeatGeneration\_lbf\_in2s  | $lbf/in^2\*s$   |

</details>

<details>

Available units for linear density.

<summary> **`MassPerLengthUnit`** </summary>

| ID | Key Name                  | Usage                                           | Description |
| -- | ------------------------- | ----------------------------------------------- | ----------- |
| 0  | MassPerLength\_t\_mm      | JPT.MassPerLengthUnit.MassPerLength\_t\_mm      | $$          |
| 1  | MassPerLength\_kg\_m      | JPT.MassPerLengthUnit.MassPerLength\_kg\_m      | $$          |
| 2  | MassPerLength\_kg\_mm     | JPT.MassPerLengthUnit.MassPerLength\_kg\_mm     | $$          |
| 3  | MassPerLength\_kgfs2\_mm2 | JPT.MassPerLengthUnit.MassPerLength\_kgfs2\_mm2 | $$          |
| 4  | MassPerLength\_slug\_ft   | JPT.MassPerLengthUnit.MassPerLength\_slug\_ft   | $$          |
| 5  | MassPerLength\_lbfs2\_in2 | JPT.MassPerLengthUnit.MassPerLength\_lbfs2\_in2 | $$          |

</details>

<details>

Available units for surface density.

<summary> **`MassPerAreaUnit`** </summary>

| ID | Key Name                | Usage                                       | Description |
| -- | ----------------------- | ------------------------------------------- | ----------- |
| 0  | MassPerArea\_t\_mm2     | JPT.MassPerAreaUnit.MassPerArea\_t\_mm2     | $$          |
| 1  | MassPerArea\_kg\_m2     | JPT.MassPerAreaUnit.MassPerArea\_kg\_m2     | $$          |
| 2  | MassPerArea\_kg\_mm2    | JPT.MassPerAreaUnit.MassPerArea\_kg\_mm2    | $$          |
| 3  | MassPerArea\_kgfs2\_mm3 | JPT.MassPerAreaUnit.MassPerArea\_kgfs2\_mm3 | $$          |
| 4  | MassPerArea\_slug\_ft2  | JPT.MassPerAreaUnit.MassPerArea\_slug\_ft2  | $$          |
| 5  | MassPerArea\_lbfs2\_in3 | JPT.MassPerAreaUnit.MassPerArea\_lbfs2\_in3 | $$          |

</details>

<details>

Available units for moment of inertia (area).

<summary> **`AreaMomentInertiaUnit`** </summary>

| ID | Key Name               | Usage                                            | Description |
| -- | ---------------------- | ------------------------------------------------ | ----------- |
| 0  | AreaMomentInertia\_mm4 | JPT.AreaMomentInertiaUnit.AreaMomentInertia\_mm4 | $mm^4$      |
| 1  | AreaMomentInertia\_m4  | JPT.AreaMomentInertiaUnit.AreaMomentInertia\_m4  | $m^4$       |
| 2  | AreaMomentInertia\_ft4 | JPT.AreaMomentInertiaUnit.AreaMomentInertia\_ft4 | $ft^4$      |
| 3  | AreaMomentInertia\_in4 | JPT.AreaMomentInertiaUnit.AreaMomentInertia\_in4 | $in^4$      |
| 4  | AreaMomentInertia\_cm4 | JPT.AreaMomentInertiaUnit.AreaMomentInertia\_cm4 | $cm^4$      |

</details>

<details>

Available units for torsional rigidity.

<summary> **`TorsionalConstUnit`** </summary>

| ID | Key Name            | Usage                                      | Description |
| -- | ------------------- | ------------------------------------------ | ----------- |
| 0  | TorsionalConst\_mm4 | JPT.TorsionalConstUnit.TorsionalConst\_mm4 | $mm^4$      |
| 1  | TorsionalConst\_m4  | JPT.TorsionalConstUnit.TorsionalConst\_m4  | $m^4$       |
| 2  | TorsionalConst\_ft4 | JPT.TorsionalConstUnit.TorsionalConst\_ft4 | $ft^4$      |
| 3  | TorsionalConst\_in4 | JPT.TorsionalConstUnit.TorsionalConst\_in4 | $in^4$      |
| 4  | TorsionalConst\_cm4 | JPT.TorsionalConstUnit.TorsionalConst\_cm4 | $cm^4$      |

</details>

<details>

Available units for warping factor.

<summary> **`WarpCoefUnit`** </summary>

| ID | Key Name      | Usage                          | Description |
| -- | ------------- | ------------------------------ | ----------- |
| 0  | WarpCoef\_mm6 | JPT.WarpCoefUnit.WarpCoef\_mm6 | $mm^6$      |
| 1  | WarpCoef\_m6  | JPT.WarpCoefUnit.WarpCoef\_m6  | $m^6$       |
| 2  | WarpCoef\_ft6 | JPT.WarpCoefUnit.WarpCoef\_ft6 | $ft^6$      |
| 3  | WarpCoef\_in6 | JPT.WarpCoefUnit.WarpCoef\_in6 | $in^6$      |
| 4  | WarpCoef\_cm6 | JPT.WarpCoefUnit.WarpCoef\_cm6 | $cm^6$      |

</details>

<details>

Available units for mass moment of inertia per unit length.

<summary> **`MassMomentInertiaPerLengthUnit`** </summary>

| ID | Key Name                           | Usage                                                                 | Description |
| -- | ---------------------------------- | --------------------------------------------------------------------- | ----------- |
| 0  | MassMomentInertiaPerLength\_tmm    | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength\_tmm    | $t\*mm$     |
| 1  | MassMomentInertiaPerLength\_kgm    | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength\_kgm    | $kg\*m$     |
| 2  | MassMomentInertiaPerLength\_kgmm   | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength\_kgmm   | $kg\*mm$    |
| 3  | MassMomentInertiaPerLength\_kgfs2  | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength\_kgfs2  | $kgf\*s^2$  |
| 4  | MassMomentInertiaPerLength\_slugft | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength\_slugft | $slug\*ft$  |
| 5  | MassMomentInertiaPerLength\_lbfs2  | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength\_lbfs2  | $lbf\*s^2$  |

</details>

<details>

<summary> **`MomentInertiaUnit`** </summary>

Available units for inertia (Area) moment.

| ID | Key Name               | Usage                                        | Description                      |
| -- | ---------------------- | -------------------------------------------- | -------------------------------- |
| 0  | MomentInertia\_tmm2    | JPT.MomentInertiaUnit.MomentInertia\_tmm2    | $t\*mm^2$                        |
| 1  | MomentInertia\_kgm2    | JPT.MomentInertiaUnit.MomentInertia\_kgm2    | $kg\*m^2$                        |
| 2  | MomentInertia\_kgmm2   | JPT.MomentInertiaUnit.MomentInertia\_kgmm2   | $kg\*mm^2$                       |
| 3  | MomentInertia\_kgfmms2 | JPT.MomentInertiaUnit.MomentInertia\_kgfmms2 | $kg&#x66;_&#x6D;&#x6D;_&#x73;^2$ |
| 4  | MomentInertia\_slugft2 | JPT.MomentInertiaUnit.MomentInertia\_slugft2 | $slug\*ft^2$                     |
| 5  | MomentInertia\_lbfins2 | JPT.MomentInertiaUnit.MomentInertia\_lbfins2 | $lb&#x66;_&#x69;&#x6E;_&#x73;^2$ |

</details>

<details>

Available units for stress.

<summary> **`StressUnit`** </summary>

| ID | Key Name        | Usage                          | Description |
| -- | --------------- | ------------------------------ | ----------- |
| 0  | Stress\_N\_mm2  | JPT.StressUnit.Stress\_N\_mm2  | $mm^2$      |
| 1  | Stress\_N\_m2   | JPT.StressUnit.Stress\_N\_m2   | $N/m^2$     |
| 2  | Stress\_mN\_mm2 | JPT.StressUnit.Stress\_mN\_mm2 | $mN/mm^2$   |

</details>

<details>

Available units for strain.

<summary> **`StrainUnit`** </summary>

| ID | Key Name     | Usage                       | Description |
| -- | ------------ | --------------------------- | ----------- |
| 0  | Strain\_Null | JPT.StrainUnit.Strain\_Null |             |

</details>

<details>

Available units for strain energy.

<summary> **`StrainEnergyUnit`** </summary>

| ID | Key Name          | Usage                                  | Description |
| -- | ----------------- | -------------------------------------- | ----------- |
|    | StrainEnergy\_Nm  | JPT.StrainEnergyUnit.StrainEnergy\_Nm  | $N-m$       |
|    | StrainEnergy\_Nmm | JPT.StrainEnergyUnit.StrainEnergy\_Nmm | $N-mm$      |

</details>

<details>

Available units for thermal energy.

<summary> **`ThermalEnergyUnit`** </summary>

| ID | Key Name           | Usage                                    | Description |
| -- | ------------------ | ---------------------------------------- | ----------- |
| 0  | ThermalEnergy\_J   | JPT.ThermalEnergyUnit.ThermalEnergy\_J   | $J$         |
| 1  | ThermalEnergy\_cal | JPT.ThermalEnergyUnit.ThermalEnergy\_cal | $mJ$        |
| 2  | ThermalEnergy\_mJ  | JPT.ThermalEnergyUnit.ThermalEnergy\_mJ  | $cal$       |

</details>

<details>

Available units for frequency.

<summary> **`FrequencyUnit`** </summary>

| ID | Key Name      | Usage                           | Description |
| -- | ------------- | ------------------------------- | ----------- |
| 0  | Frequency\_hz | JPT.FrequencyUnit.Frequency\_hz | $Hz$        |

</details>

<details>

Available units for volume energy density.

<summary> **`VolumeEnergyDensityUnit`** </summary>

| ID | Key Name                     | Usage                                                    | Description |
| -- | ---------------------------- | -------------------------------------------------------- | ----------- |
| 0  | VolumeEnergyDensity\_J\_m3   | JPT.VolumeEnergyDensityUnit.VolumeEnergyDensity\_J\_m3   | $J/mm^3$    |
| 1  | VolumeEnergyDensity\_J\_mm3  | JPT.VolumeEnergyDensityUnit.VolumeEnergyDensity\_J\_mm3  | $J/m^3$     |
| 2  | VolumeEnergyDensity\_mJ\_mm3 | JPT.VolumeEnergyDensityUnit.VolumeEnergyDensity\_mJ\_mm3 | $mJ/mm^3$   |

</details>

<details>

Available units for electrical resistivity.

<summary> **`ElectricalResistivityUnit`** </summary>

| ID | Key Name                       | Usage  | Description |
| -- | ------------------------------ | ------ | ----------- |
| 0  | ElectricalResistivity\_Ohm\_m  | Ohm-m  |             |
| 1  | ElectricalResistivity\_Ohm\_mm | Ohm-mm |             |

</details>

<details>

Available units for stress reciprocal.

<summary> **`StressReciprocalUnit(temp) `** </summary>

</details>

<details>

Available units for thermal radiation.

<summary> **`ThermalRadiationUnit`** </summary>

| ID | Key Name                       | Usage                                                   | Description |
| -- | ------------------------------ | ------------------------------------------------------- | ----------- |
| 0  | ThermalRadiation\_W\_m2K4      | JPT.ThermalRadiationUnit.ThermalRadiation\_W\_m2K4      | $mm^2/N$    |
| 1  | ThermalRadiation\_mW\_mm2K4    | JPT.ThermalRadiationUnit.ThermalRadiation\_mW\_mm2K4    | $m^2/N$     |
| 2  | ThermalRadiation\_kcal\_smm2K4 | JPT.ThermalRadiationUnit.ThermalRadiation\_kcal\_smm2K4 | $mm^2/mN$   |

</details>

<details>

Available units for displacement.

<summary> **`DisplacementUnit`** </summary>

| ID | Key Name         | Usage                             | Description |
| -- | ---------------- | --------------------------------- | ----------- |
| 0  | Displacement\_mm | JPT.Displacement.Displacement\_mm | $mm$        |
| 1  | Displacement\_m  | JPT.Displacement.Displacement\_m  | $m          |
| 2  | Displacement\_ft | JPT.Displacement.Displacement\_ft | $ft$        |
| 3  | Displacement\_in | JPT.Displacement.Displacement\_in | $in$        |
| 4  | Displacement\_cm | JPT.Displacement.Displacement\_cm | $cm$        |

</details>

<details>

Available units for energy density.

<summary> **`EnergyDensityUnit`** </summary>

| ID | Key Name                 | Usage                                          | Description |
| -- | ------------------------ | ---------------------------------------------- | ----------- |
| 0  | EnergyDensity\_J\_m3     | JPT.EnergyDensityUnit.EnergyDensity\_J\_m3     | $mJ/mm^3$   |
| 1  | EnergyDensity\_mJ\_mm3   | JPT.EnergyDensityUnit.EnergyDensity\_mJ\_mm3   | $J/m^3$     |
| 2  | EnergyDensity\_Kcal\_mm3 | JPT.EnergyDensityUnit.EnergyDensity\_Kcal\_mm3 | $Kcal/mm^3$ |

</details>

<details>

Available units for temperature gradient.

<summary> **`TemperatureGradientUnit`** </summary>

| ID | Key Name                   | Usage                                                  | Description |
| -- | -------------------------- | ------------------------------------------------------ | ----------- |
| 0  | TemperatureGradient\_K\_m  | JPT.TemperatureGradientUnit.TemperatureGradient\_K\_m  | $K/m$       |
| 1  | TemperatureGradient\_K\_mm | JPT.TemperatureGradientUnit.TemperatureGradient\_K\_mm | $K/mm$      |

</details>

<details>

Available units for current.

<summary> **`CurrentUnit`** </summary>

| ID | Key Name    | Usage                       | Description |
| -- | ----------- | --------------------------- | ----------- |
| 0  | Current\_A  | JPT.CurrentUnit.Current\_A  | $A$         |
| 1  | Current\_mA | JPT.CurrentUnit.Current\_mA | $mA$        |
| 2  | Current\_uA | JPT.CurrentUnit.Current\_uA | $uA$        |
| 3  | Current\_kA | JPT.CurrentUnit.Current\_kA | $kA$        |

</details>

<details>

Available units for voltage.

<summary> **`VoltageUnit`** </summary>

| ID | Key Name    | Usage                       | Description |
| -- | ----------- | --------------------------- | ----------- |
| 0  | Voltage\_V  | JPT.VoltageUnit.Voltage\_V  | $V$         |
| 1  | Voltage\_mV | JPT.VoltageUnit.Voltage\_mV | $mV$        |
| 2  | Voltage\_uV | JPT.VoltageUnit.Voltage\_uV | $uV$        |
| 3  | Voltage\_kV | JPT.VoltageUnit.Voltage\_kV | $kV$        |

</details>
