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

| ID  | Key Name  | Usage                    | Description |
| --- | --------- | ------------------------ | ----------- |
| 0   | Length_mm | JPT.LengthUnit.Length_mm | $mm$        |
| 1   | Length_m  | JPT.LengthUnit.Length_m  | $m$         |
| 2   | Length_ft | JPT.LengthUnit.Length_ft | $ft$        |
| 3   | Length_in | JPT.LengthUnit.Length_in | $in$        |
| 4   | Length_cm | JPT.LengthUnit.Length_cm | $cm$        |

</details>

<details>

Available units for time.

<summary> **`TimeUnit`** </summary>

| ID  | Key Name | Usage                 | Description |
| --- | -------- | --------------------- | ----------- |
| 0   | Time_s   | JPT.TimeUnit.Time_s   | $s$         |
| 1   | Time_min | JPT.TimeUnit.Time_min | $min$       |
| 2   | Time_h   | JPT.TimeUnit.Time_h   | $h$         |

</details>

<details>

Available units for mass.

<summary> **`MassUnit`** </summary>

| ID  | Key Name      | Usage                      | Description  |
| --- | ------------- | -------------------------- | ------------ |
| 0   | Mass_t        | JPT.MassUnit.Mass_t        | $t$          |
| 1   | Mass_kg       | JPT.MassUnit.Mass_kg       | $kg$         |
| 2   | Mass_kgfs2_mm | JPT.MassUnit.Mass_kgfs2_mm | $kgf*s^2/mm$ |
| 3   | Mass_slug     | JPT.MassUnit.Mass_slug     | $slug$       |
| 4   | Mass_lbfs2_in | JPT.MassUnit.Mass_lbfs2_in | $lbf*s^2/in$ |
| 5   | Mass_lb       | JPT.MassUnit.Mass_lb       | $lb$         |
| 6   | Mass_g        | JPT.MassUnit.Mass_g        | $g$          |

</details>

<details>

Available units for force.

<summary> **`ForceUnit`** </summary>

| ID  | Key Name  | Usage                   | Description |
| --- | --------- | ----------------------- | ----------- |
| 0   | Force_N   | JPT.ForceUnit.Force_N   | $N$         |
| 1   | Force_mN  | JPT.ForceUnit.Force_mN  | $mN$        |
| 2   | Force_kN  | JPT.ForceUnit.Force_kN  | $kN$        |
| 3   | Force_kgf | JPT.ForceUnit.Force_kgf | $kgf$       |
| 4   | Force_lbf | JPT.ForceUnit.Force_lbf | $lbf$       |
| 5   | Force_tf  | JPT.ForceUnit.Force_tf  | $tf$        |

</details>

<details>

Available units for angle.

<summary> **`AngleUnit`** </summary>

| ID  | Key Name     | Usage                      | Description |
| --- | ------------ | -------------------------- | ----------- |
| 0   | Angle_rad    | JPT.AngleUnit.Angle_rad    | $deg$       |
| 1   | Angle_degree | JPT.AngleUnit.Angle_degree | $rad$       |

</details>

<details>

Available units for temperature.

<summary> **`TemperatureUnit`** </summary>

| ID  | Key Name         | Usage                                | Description |
| --- | ---------------- | ------------------------------------ | ----------- |
| 0   | Temperature_K    | JPT.TemperatureUnit.Temperature_K    | $K$         |
| 1   | Temperature_degC | JPT.TemperatureUnit.Temperature_degC | $deg C$     |
| 2   | Temperature_degF | JPT.TemperatureUnit.Temperature_degF | $deg F$     |

</details>

<details>

Available units for Area.

<summary> **`AreaUnit`** </summary>

| ID  | Key Name | Usage                 | Description |
| --- | -------- | --------------------- | ----------- |
| 0   | Area_mm2 | JPT.AreaUnit.Area_mm2 | $mm^2$      |
| 1   | Area_m2  | JPT.AreaUnit.Area_m2  | $m^2$       |
| 2   | Area_ft2 | JPT.AreaUnit.Area_ft2 | $ft^2$      |
| 3   | Area_in2 | JPT.AreaUnit.Area_in2 | $in^2$      |
| 4   | Area_cm2 | JPT.AreaUnit.Area_cm2 | $cm^2$      |

</details>

<details>

Available units for Volume.

<summary> **`VolumeUnit`** </summary>

| ID  | Key Name   | Usage                     | Description |
| --- | ---------- | ------------------------- | ----------- |
| 0   | Volume_mm3 | JPT.VolumeUnit.Volume_mm3 | $mm^3$      |
| 1   | Volume_m3  | JPT.VolumeUnit.Volume_m3  | $m^3$       |
| 2   | Volume_ft3 | JPT.VolumeUnit.Volume_ft3 | $ft^3$      |
| 3   | Volume_in3 | JPT.VolumeUnit.Volume_in3 | $in^3$      |
| 4   | Volume_cm3 | JPT.VolumeUnit.Volume_cm3 | $cm^3$      |

</details>

<details>

Available units for Velocity.

<summary> **`VelocityUnit`** </summary>

| ID  | Key Name      | Usage                          | Description |
| --- | ------------- | ------------------------------ | ----------- |
| 0   | Velocity_mm_s | JPT.VelocityUnit.Velocity_mm_s | $s$         |
| 1   | Velocity_m_s  | JPT.VelocityUnit.Velocity_m_s  | $m/s$       |
| 2   | Velocity_ft_s | JPT.VelocityUnit.Velocity_ft_s | $ft/s$      |
| 3   | Velocity_in_s | JPT.VelocityUnit.Velocity_in_s | $in/s$      |

</details>

<details>

Available units for Acceleration.

<summary> **`AccelerationUnit`** </summary>

| ID  | Key Name           | Usage                                   | Description |
| --- | ------------------ | --------------------------------------- | ----------- |
| 0   | Acceleration_mm_s2 | JPT.AccelerationUnit.Acceleration_mm_s2 | $s$         |
| 1   | Acceleration_m_s2  | JPT.AccelerationUnit.Acceleration_m_s2  | $m/s$       |
| 2   | Acceleration_ft_s2 | JPT.AccelerationUnit.Acceleration_ft_s2 | $ft/s$      |
| 3   | Acceleration_in_s2 | JPT.AccelerationUnit.Acceleration_in_s2 | $in/s$      |
| 4   | Acceleration_g     | JPT.AccelerationUnit.Acceleration_g     | $g$         |
| 5   | Acceleration_Gal   | JPT.AccelerationUnit.Acceleration_Gal   | $Gal$       |

</details>

<details>

Available units for rotational velocity.

<summary> **`RotateVeloUnit`** </summary>

| ID  | Key Name         | Usage                               | Description |
| --- | ---------------- | ----------------------------------- | ----------- |
| 0   | RotateVelo_rad_s | JPT.RotateVeloUnit.RotateVelo_rad_s | $rad/s$     |
| 1   | RotateVelo_deg_s | JPT.RotateVeloUnit.RotateVelo_deg_s | $deg/s$     |
| 2   | RotateVelo_rpm   | JPT.RotateVeloUnit.RotateVelo_rpm   | $rpm$       |

</details>

<details>

Available units for rotational acceleration.

<summary> **`RotateAccUnit`** </summary>

| ID  | Key Name         | Usage                              | Description |
| --- | ---------------- | ---------------------------------- | ----------- |
| 0   | RotateAcc_rad_s2 | JPT.RotateAccUnit.RotateAcc_rad_s2 | $rad/s^2$   |
| 1   | RotateAcc_deg_s2 | JPT.RotateAccUnit.RotateAcc_deg_s2 | $deg/s^2$   |

</details>

<details>

Available units for moment.

<summary> **`MomentUnit`** </summary>

| ID  | Key Name     | Usage                       | Description |
| --- | ------------ | --------------------------- | ----------- |
| 0   | Moment_Nmm   | JPT.MomentUnit.Moment_Nmm   | $N*mm$      |
| 1   | Moment_Nm    | JPT.MomentUnit.Moment_Nm    | $N*m$       |
| 2   | Moment_mNmm  | JPT.MomentUnit.Moment_mNmm  | $mN*mm$     |
| 3   | Moment_kgfmm | JPT.MomentUnit.Moment_kgfmm | $kgf*mm$    |
| 4   | Moment_lbfft | JPT.MomentUnit.Moment_lbfft | $lbf*ft$    |
| 5   | Moment_lbfin | JPT.MomentUnit.Moment_lbfin | $lbf*in$    |
| 6   | Moment_kgfcm | JPT.MomentUnit.Moment_kgfcm | $tf*m$      |

</details>

<details>

Available units for pressure.

<summary> **`PressureUnit`** </summary>

| ID  | Key Name         | Usage                             | Description |
| --- | ---------------- | --------------------------------- | ----------- |
| 0   | Pressure_MPa     | JPT.PressureUnit.Pressure_MPa     | $MPa$       |
| 1   | Pressure_Pa      | JPT.PressureUnit.Pressure_Pa      | $Pa$        |
| 2   | Pressure_kPa     | JPT.PressureUnit.Pressure_kPa     | $kPa$       |
| 3   | Pressure_kgf_mm2 | JPT.PressureUnit.Pressure_kgf_mm2 | $kgf/mm^2$  |
| 4   | Pressure_lbf_ft2 | JPT.PressureUnit.Pressure_lbf_ft2 | $lbf/ft^2$  |
| 5   | Pressure_lbf_in2 | JPT.PressureUnit.Pressure_lbf_in2 | $lbf/in^2$  |
| 6   | Pressure_tf_m2   | JPT.PressureUnit.Pressure_tf_m2   | $tf/m^2$    |
| 7   | Pressure_GPa     | JPT.PressureUnit.Pressure_GPa     | $GPa$       |

</details>

<details>

Available units for density.

<summary> **`DensityUnit`** </summary>

| ID  | Key Name          | Usage              | Description |
| --- | ----------------- | ------------------ | ----------- |
| 0   | Density_t_mm3     | Density_t_mm3      | $$          |
| 1   | Density_kg_m3     | Density_kg_m3      | $$          |
| 2   | Density_kg_mm3    | Density_kg_mm3     | $$          |
| 3   | Density_kgfs2_mm4 | Density_kgfs2_mm$$ |             |
| 4   | Density_slug_ft3  | Density_slug_ft3   | $$          |
| 5   | Density_lbfs2_in4 | Density_lbfs2_in4  | $$          |

</details>

<details>

Available units for stiffness.

<summary> **`StiffnessUnit`** </summary>

| ID  | Key Name         | Usage                              | Description |
| --- | ---------------- | ---------------------------------- | ----------- |
| 0   | Stiffness_N_mm   | JPT.StiffnessUnit.Stiffness_N_mm   | $mm$        |
| 1   | Stiffness_N_m    | JPT.StiffnessUnit.Stiffness_N_m    | $N/m$       |
| 2   | Stiffness_mN_mm  | JPT.StiffnessUnit.Stiffness_mN_mm  | $mN/mmn$    |
| 3   | Stiffness_kgf_mm | JPT.StiffnessUnit.Stiffness_kgf_mm | $kgf/mm$    |
| 4   | Stiffness_lbf_ft | JPT.StiffnessUnit.Stiffness_lbf_ft | $lbf/ft$    |
| 5   | Stiffness_lbf_in | JPT.StiffnessUnit.Stiffness_lbf_in | $lbf/in$    |

</details>

<details>

Available units for rotational stiffness.

<summary> **`RotateStiffUnit`** </summary>

| ID  | Key Name              | Usage                                     | Description    |
| --- | --------------------- | ----------------------------------------- | -------------- |
| 0   | RotateStiff_Nmm_rad   | JPT.RotateStiffUnit.RotateStiff_Nmm_rad   | $N*mm/rad$     |
| 1   | RotateStiff_Nm_rad    | JPT.RotateStiffUnit.RotateStiff_Nm_rad    | $N*m/rad$      |
| 2   | RotateStiff_mNmm_rad  | JPT.RotateStiffUnit.RotateStiff_mNmm_rad  | $mN*mm/rad$    |
| 3   | RotateStiff_kgfmm_rad | JPT.RotateStiffUnit.RotateStiff_kgfmm_rad | $kgf*mm/rad$   |
| 4   | RotateStiff_lbfft_rad | JPT.RotateStiffUnit.RotateStiff_lbfft_rad | $lbf*ft/rad$   |
| 5   | RotateStiff_lbfin_rad | JPT.RotateStiffUnit.RotateStiff_lbfin_rad | $lbf\*in/rad\$ |
| 6   | RotateStiff_Nmm_deg   | JPT.RotateStiffUnit.RotateStiff_Nmm_deg   | $\N*mm/deg$    |
| 7   | RotateStiff_mNmm_deg  | JPT.RotateStiffUnit.RotateStiff_mNmm_deg  | $\mN*mm/deg$   |

</details>

<details>

Available units for damping coefficient.

<summary> **`DampCoefUnit`** </summary>

Available units for rotational stiffness.

| ID  | Key Name         | Usage                             | Description |
| --- | ---------------- | --------------------------------- | ----------- |
| 1   | DampCoef_Ns_mm   | JPT.DampCoefUnit.DampCoef_Ns_mm   | $N*s/mm$    |
| 2   | DampCoef_Ns_m    | JPT.DampCoefUnit.DampCoef_Ns_m    | $N*s/m$     |
| 3   | DampCoef_mNs_mm  | JPT.DampCoefUnit.DampCoef_mNs_mm  | $mN*s/mm$   |
| 4   | DampCoef_kgfs_mm | JPT.DampCoefUnit.DampCoef_kgfs_mm | $kgf*s/mm$  |
| 5   | DampCoef_lbfs_ft | JPT.DampCoefUnit.DampCoef_lbfs_ft | $lbf*s/ft$  |
| 6   | DampCoef_lbfs_in | JPT.DampCoefUnit.DampCoef_lbfs_in | $lbf*s/in$  |

</details>

<details>

Available units for rotational damping coefficient.

<summary> **`RotateDampCoefUnit`** </summary>

| ID  | Key Name                  | Usage                                            | Description    |
| --- | ------------------------- | ------------------------------------------------ | -------------- |
| 0   | RotateDampCoef_Nmms_rad   | JPT.RotateDampCoefUnit.RotateDampCoef_Nmms_rad   | $N*mm*s/rad$   |
| 1   | RotateDampCoef_Nms_rad    | JPT.RotateDampCoefUnit.RotateDampCoef_Nms_rad    | $N*mm*s/rad$   |
| 2   | RotateDampCoef_mNmms_rad  | JPT.RotateDampCoefUnit.RotateDampCoef_mNmms_rad  | $mN*mm*s/rad$  |
| 3   | RotateDampCoef_kgfmms_rad | JPT.RotateDampCoefUnit.RotateDampCoef_kgfmms_rad | $kgf*mm*s/rad$ |
| 4   | RotateDampCoef_lbffts_rad | JPT.RotateDampCoefUnit.RotateDampCoef_lbffts_rad | $lbf*ft*s/rad$ |
| 5   | RotateDampCoef_lbfins_rad | JPT.RotateDampCoefUnit.RotateDampCoef_lbfins_rad | $lbf*in*s/rad$ |
| 6   | RotateDampCoef_Nmms_deg   | JPT.RotateDampCoefUnit.RotateDampCoef_Nmms_deg   | $N*mm*s/deg$   |
| 7   | RotateDampCoef_mNmms_deg  | JPT.RotateDampCoefUnit.RotateDampCoef_mNmms_deg  | $mN*mm*s/deg$  |

</details>

<details>

Available units for elastic modulus.

<summary> **`ModulusUnit`** </summary>

| ID  | Key Name        | Usage                           | Description |
| --- | --------------- | ------------------------------- | ----------- |
| 0   | Modulus_N_mm2   | JPT.ModulusUnit.Modulus_N_mm2   | $N/mm^2$    |
| 1   | Modulus_N_m2    | JPT.ModulusUnit.Modulus_N_m2    | $N/m^2$     |
| 2   | Modulus_mN_mm2  | JPT.ModulusUnit.Modulus_mN_mm2  | $mN/mm^2$   |
| 3   | Modulus_kgf_mm2 | JPT.ModulusUnit.Modulus_kgf_mm2 | $kgf/mm^2$  |
| 4   | Modulus_lbf_ft2 | JPT.ModulusUnit.Modulus_lbf_ft2 | $lbf/ft^2$  |
| 5   | Modulus_lbf_in2 | JPT.ModulusUnit.Modulus_lbf_in2 | $lbf/in^2$  |

</details>

<details>

Available units for energy.

<summary> **`EnergyUnit`** </summary>

| ID  | Key Name     | Usage                       | Description |
| --- | ------------ | --------------------------- | ----------- |
| 1   | Energy_mJ    | JPT.EnergyUnit.Energy_mJ    | $mJ$        |
| 2   | Energy_J     | JPT.EnergyUnit.Energy_J     | $J$         |
| 3   | Energy_miuJ  | JPT.EnergyUnit.Energy_miuJ  | $miuJ$      |
| 4   | Energy_kCal  | JPT.EnergyUnit.Energy_kCal  | $kcal$      |
| 5   | Energy_ftlbf | JPT.EnergyUnit.Energy_ftlbf | $ft*lbf$    |
| 6   | Energy_inlbf | JPT.EnergyUnit.Energy_inlbf | $in*lbf$    |
| 7   | Energy_kJ    | JPT.EnergyUnit.Energy_kJ    | $kJ$        |
| 8   | Energy_cal   | JPT.EnergyUnit.Energy_cal   | $cal$       |

</details>

<details>

Available units for power.

<summary> **`PowerUnit`** </summary>

| ID  | Key Name      | Usage                       | Description |
| --- | ------------- | --------------------------- | ----------- |
| 0   | Power_mW      | JPT.PowerUnit.Power_mW      | $mW$        |
| 1   | Power_W       | JPT.PowerUnit.Power_W       | $W$         |
| 2   | Power_miuW    | JPT.PowerUnit.Power_miuW    | $miuW$      |
| 3   | Power_kcal_s  | JPT.PowerUnit.Power_kcal_s  | $kcal/s$    |
| 4   | Power_ftlbf_s | JPT.PowerUnit.Power_ftlbf_s | $ft*lbf/s$  |
| 5   | Power_inlbf_s | JPT.PowerUnit.Power_inlbf_s | $in*lbf/s$  |

</details>

<details>

Available units for coefficient of linear expansion

<summary> **`ThermalExCoefUnit`** </summary>

| ID  | Key Name         | Usage                                  | Description |
| --- | ---------------- | -------------------------------------- | ----------- |
| 0   | ThermalExCoef*K* | JPT.ThermalExCoefUnit.ThermalExCoef*K* | $/K$        |

</details>

<details>

Available units for thermal conductivity

<summary> **`ThermalConductUnit`** </summary>

| ID  | Key Name                 | Usage                                           | Description   |
| --- | ------------------------ | ----------------------------------------------- | ------------- |
| 0   | ThermalConduct_mW_mmK    | JPT.ThermalConductUnit.ThermalConduct_mW_mmK    | $mW/mm*K$     |
| 1   | ThermalConduct_W_mK      | JPT.ThermalConductUnit.ThermalConduct_W_mK      | $W/m*K$       |
| 2   | ThermalConduct_miuW_mmK  | JPT.ThermalConductUnit.ThermalConduct_miuW_mmK  | $miuW/mm*K$   |
| 3   | ThermalConduct_kcal_mmhK | JPT.ThermalConductUnit.ThermalConduct_kcal_mmhK | $kcal/mm*h*K$ |
| 4   | ThermalConduct_lbf_sK    | JPT.ThermalConductUnit.ThermalConduct_lbf_sK    | $lbf/s*K$     |

</details>

<details>

Available units for Convection coefficient

<summary> **`HeatTransCoefUnit`** </summary>

| ID  | Key Name                 | Usage                                          | Description   |
| --- | ------------------------ | ---------------------------------------------- | ------------- |
| 1   | HeatTransCoef_mW_mm2K    | JPT.HeatTransCoefUnit.HeatTransCoef_mW_mm2K    | $mW/mm*K$     |
| 2   | HeatTransCoef_W_m2K      | JPT.HeatTransCoefUnit.HeatTransCoef_W_m2K      | $W/m*K$       |
| 3   | HeatTransCoef_miuW_mm2K  | JPT.HeatTransCoefUnit.HeatTransCoef_miuW_mm2K  | $miuW/mm*K$   |
| 4   | HeatTransCoef_kcal_mm2hK | JPT.HeatTransCoefUnit.HeatTransCoef_kcal_mm2hK | $kcal/mm*h*K$ |
| 5   | HeatTransCoef_lbf_ftsK   | JPT.HeatTransCoefUnit.HeatTransCoef_lbf_ftsK   | $lbf/ft*s*K$  |
| 6   | HeatTransCoef_lbf_insK   | JPT.HeatTransCoefUnit.HeatTransCoef_lbf_insK   | $lbf/in*s*K$  |

</details>

<details>

Available units for specific heat.

<summary> **`SpecificHeatUnit`** </summary>

| ID  | Key Name                 | Usage                                         | Description     |
| --- | ------------------------ | --------------------------------------------- | --------------- |
| 0   | SpecificHeat_mJ_tK       | JPT.SpecificHeatUnit.SpecificHeat_mJ_tK       | $mJ/t*K$        |
| 1   | SpecificHeat_J_kgK       | JPT.SpecificHeatUnit.SpecificHeat_J_kgK       | $J/kg*K$        |
| 2   | SpecificHeat_miuJ_kgK    | JPT.SpecificHeatUnit.SpecificHeat_miuJ_kgK    | $miuJ/kg*K$     |
| 3   | SpecificHeat_kcal_kgK    | JPT.SpecificHeatUnit.SpecificHeat_kcal_kgK    | $kcal/kg*K$     |
| 4   | SpecificHeat_ftlbf_slugK | JPT.SpecificHeatUnit.SpecificHeat_ftlbf_slugK | $ft*lbf/slug*K$ |
| 5   | SpecificHeat_in2_s2K     | JPT.SpecificHeatUnit.SpecificHeat_in2_s2K     | $in^2/s^2*K$    |

</details>

<details>

Available units for heat flux.

<summary> **`HeatFluxUnit`** </summary>

| ID  | Key Name           | Usage                               | Description   |
| --- | ------------------ | ----------------------------------- | ------------- |
| 0   | HeatFlux_mW_mm2    | JPT.HeatFluxUnit.HeatFlux_mW_mm2    | $mW/mm^2$     |
| 1   | HeatFlux_W_m2      | JPT.HeatFluxUnit.HeatFlux_W_m2      | $W/m^2$       |
| 2   | HeatFlux_miuW_mm2  | JPT.HeatFluxUnit.HeatFlux_miuW_mm2  | $miuW/mm^2$   |
| 3   | HeatFlux_kcal_mm2h | JPT.HeatFluxUnit.HeatFlux_kcal_mm2h | $kcal/mm^2*h$ |
| 4   | HeatFlux_lbf_fts   | JPT.HeatFluxUnit.HeatFlux_lbf_fts   | $lbf/ft*s$    |
| 5   | HeatFlux_lbf_ins   | JPT.HeatFluxUnit.HeatFlux_lbf_ins   | $lbf/in*s$    |

</details>

<details>

Available units for heat generation.

<summary> **`HeatGenerationUnit`** </summary>

| ID  | Key Name                 | Usage                                           | Description    |
| --- | ------------------------ | ----------------------------------------------- | -------------- |
| 1   | HeatGeneration_mW_mm3    | JPT.HeatGenerationUnit.HeatGeneration_mW_mm3    | $mW/mm^3$      |
| 2   | HeatGeneration_W_m3      | JPT.HeatGenerationUnit.HeatGeneration_W_m3      | $W/m^3$        |
| 3   | HeatGeneration_miuW_mm3  | JPT.HeatGenerationUnit.HeatGeneration_miuW_mm3  | $miuW/mm^3$    |
| 4   | HeatGeneration_kcal_mm3h | JPT.HeatGenerationUnit.HeatGeneration_kcal_mm3h | $kcal//mm^3*h$ |
| 5   | HeatGeneration_lbf_ft2s  | JPT.HeatGenerationUnit.HeatGeneration_lbf_ft2s  | $lbf/ft^2*s$   |
| 6   | HeatGeneration_lbf_in2s  | JPT.HeatGenerationUnit.HeatGeneration_lbf_in2s  | $lbf/in^2*s$   |

</details>

<details>

Available units for linear density.

<summary> **`MassPerLengthUnit`** </summary>

| ID  | Key Name                | Usage                                         | Description |
| --- | ----------------------- | --------------------------------------------- | ----------- |
| 0   | MassPerLength_t_mm      | JPT.MassPerLengthUnit.MassPerLength_t_mm      | $$          |
| 1   | MassPerLength_kg_m      | JPT.MassPerLengthUnit.MassPerLength_kg_m      | $$          |
| 2   | MassPerLength_kg_mm     | JPT.MassPerLengthUnit.MassPerLength_kg_mm     | $$          |
| 3   | MassPerLength_kgfs2_mm2 | JPT.MassPerLengthUnit.MassPerLength_kgfs2_mm2 | $$          |
| 4   | MassPerLength_slug_ft   | JPT.MassPerLengthUnit.MassPerLength_slug_ft   | $$          |
| 5   | MassPerLength_lbfs2_in2 | JPT.MassPerLengthUnit.MassPerLength_lbfs2_in2 | $$          |

</details>

<details>

Available units for surface density.

<summary> **`MassPerAreaUnit`** </summary>

| ID  | Key Name              | Usage                                     | Description |
| --- | --------------------- | ----------------------------------------- | ----------- |
| 0   | MassPerArea_t_mm2     | JPT.MassPerAreaUnit.MassPerArea_t_mm2     | $$          |
| 1   | MassPerArea_kg_m2     | JPT.MassPerAreaUnit.MassPerArea_kg_m2     | $$          |
| 2   | MassPerArea_kg_mm2    | JPT.MassPerAreaUnit.MassPerArea_kg_mm2    | $$          |
| 3   | MassPerArea_kgfs2_mm3 | JPT.MassPerAreaUnit.MassPerArea_kgfs2_mm3 | $$          |
| 4   | MassPerArea_slug_ft2  | JPT.MassPerAreaUnit.MassPerArea_slug_ft2  | $$          |
| 5   | MassPerArea_lbfs2_in3 | JPT.MassPerAreaUnit.MassPerArea_lbfs2_in3 | $$          |

</details>

<details>

Available units for moment of inertia (area).

<summary> **`AreaMomentInertiaUnit`** </summary>

| ID  | Key Name              | Usage                                           | Description |
| --- | --------------------- | ----------------------------------------------- | ----------- |
| 0   | AreaMomentInertia_mm4 | JPT.AreaMomentInertiaUnit.AreaMomentInertia_mm4 | $mm^4$      |
| 1   | AreaMomentInertia_m4  | JPT.AreaMomentInertiaUnit.AreaMomentInertia_m4  | $m^4$       |
| 2   | AreaMomentInertia_ft4 | JPT.AreaMomentInertiaUnit.AreaMomentInertia_ft4 | $ft^4$      |
| 3   | AreaMomentInertia_in4 | JPT.AreaMomentInertiaUnit.AreaMomentInertia_in4 | $in^4$      |
| 4   | AreaMomentInertia_cm4 | JPT.AreaMomentInertiaUnit.AreaMomentInertia_cm4 | $cm^4$      |

</details>

<details>

Available units for torsional rigidity.

<summary> **`TorsionalConstUnit`** </summary>

| ID  | Key Name           | Usage                                     | Description |
| --- | ------------------ | ----------------------------------------- | ----------- |
| 0   | TorsionalConst_mm4 | JPT.TorsionalConstUnit.TorsionalConst_mm4 | $mm^4$      |
| 1   | TorsionalConst_m4  | JPT.TorsionalConstUnit.TorsionalConst_m4  | $m^4$       |
| 2   | TorsionalConst_ft4 | JPT.TorsionalConstUnit.TorsionalConst_ft4 | $ft^4$      |
| 3   | TorsionalConst_in4 | JPT.TorsionalConstUnit.TorsionalConst_in4 | $in^4$      |
| 4   | TorsionalConst_cm4 | JPT.TorsionalConstUnit.TorsionalConst_cm4 | $cm^4$      |

</details>

<details>

Available units for warping factor.

<summary> **`WarpCoefUnit`** </summary>

| ID  | Key Name     | Usage                         | Description |
| --- | ------------ | ----------------------------- | ----------- |
| 0   | WarpCoef_mm6 | JPT.WarpCoefUnit.WarpCoef_mm6 | $mm^6$      |
| 1   | WarpCoef_m6  | JPT.WarpCoefUnit.WarpCoef_m6  | $m^6$       |
| 2   | WarpCoef_ft6 | JPT.WarpCoefUnit.WarpCoef_ft6 | $ft^6$      |
| 3   | WarpCoef_in6 | JPT.WarpCoefUnit.WarpCoef_in6 | $in^6$      |
| 4   | WarpCoef_cm6 | JPT.WarpCoefUnit.WarpCoef_cm6 | $cm^6$      |

</details>

<details>

Available units for mass moment of inertia per unit length.

<summary> **`MassMomentInertiaPerLengthUnit`** </summary>

| ID  | Key Name                          | Usage                                                                | Description |
| --- | --------------------------------- | -------------------------------------------------------------------- | ----------- |
| 0   | MassMomentInertiaPerLength_tmm    | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength_tmm    | $t*mm$      |
| 1   | MassMomentInertiaPerLength_kgm    | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength_kgm    | $kg*m$      |
| 2   | MassMomentInertiaPerLength_kgmm   | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength_kgmm   | $kg*mm$     |
| 3   | MassMomentInertiaPerLength_kgfs2  | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength_kgfs2  | $kgf*s^2$   |
| 4   | MassMomentInertiaPerLength_slugft | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength_slugft | $slug*ft$   |
| 5   | MassMomentInertiaPerLength_lbfs2  | JPT.MassMomentInertiaPerLengthUnit.MassMomentInertiaPerLength_lbfs2  | $lbf*s^2$   |

</details>

<details>

<summary> **`MomentInertiaUnit`** </summary>

Available units for inertia (Area) moment.

| ID  | Key Name              | Usage                                       | Description  |
| --- | --------------------- | ------------------------------------------- | ------------ |
| 0   | MomentInertia_tmm2    | JPT.MomentInertiaUnit.MomentInertia_tmm2    | $t*mm^2$     |
| 1   | MomentInertia_kgm2    | JPT.MomentInertiaUnit.MomentInertia_kgm2    | $kg*m^2$     |
| 2   | MomentInertia_kgmm2   | JPT.MomentInertiaUnit.MomentInertia_kgmm2   | $kg*mm^2$    |
| 3   | MomentInertia_kgfmms2 | JPT.MomentInertiaUnit.MomentInertia_kgfmms2 | $kgf*mm*s^2$ |
| 4   | MomentInertia_slugft2 | JPT.MomentInertiaUnit.MomentInertia_slugft2 | $slug*ft^2$  |
| 5   | MomentInertia_lbfins2 | JPT.MomentInertiaUnit.MomentInertia_lbfins2 | $lbf*in*s^2$ |

</details>

<details>

Available units for stress.

<summary> **`StressUnit`** </summary>

| ID  | Key Name      | Usage                        | Description |
| --- | ------------- | ---------------------------- | ----------- |
| 0   | Stress_N_mm2  | JPT.StressUnit.Stress_N_mm2  | $mm^2$      |
| 1   | Stress_N_m2   | JPT.StressUnit.Stress_N_m2   | $N/m^2$     |
| 2   | Stress_mN_mm2 | JPT.StressUnit.Stress_mN_mm2 | $mN/mm^2$   |

</details>

<details>

Available units for strain.

<summary> **`StrainUnit`** </summary>

| ID  | Key Name    | Usage                      | Description |
| --- | ----------- | -------------------------- | ----------- |
| 0   | Strain_Null | JPT.StrainUnit.Strain_Null |             |

</details>

<details>

Available units for strain energy.

<summary> **`StrainEnergyUnit`** </summary>

| ID  | Key Name         | Usage                                 | Description |
| --- | ---------------- | ------------------------------------- | ----------- |
|     | StrainEnergy_Nm  | JPT.StrainEnergyUnit.StrainEnergy_Nm  | $N-m$       |
|     | StrainEnergy_Nmm | JPT.StrainEnergyUnit.StrainEnergy_Nmm | $N-mm$      |

</details>

<details>

Available units for thermal energy.

<summary> **`ThermalEnergyUnit`** </summary>

| ID  | Key Name          | Usage                                   | Description |
| --- | ----------------- | --------------------------------------- | ----------- |
| 0   | ThermalEnergy_J   | JPT.ThermalEnergyUnit.ThermalEnergy_J   | $J$         |
| 1   | ThermalEnergy_cal | JPT.ThermalEnergyUnit.ThermalEnergy_cal | $mJ$        |
| 2   | ThermalEnergy_mJ  | JPT.ThermalEnergyUnit.ThermalEnergy_mJ  | $cal$       |

</details>

<details>

Available units for frequency.

<summary> **`FrequencyUnit`** </summary>

| ID  | Key Name     | Usage                          | Description |
| --- | ------------ | ------------------------------ | ----------- |
| 0   | Frequency_hz | JPT.FrequencyUnit.Frequency_hz | $Hz$        |

</details>

<details>

Available units for volume energy density.

<summary> **`VolumeEnergyDensityUnit`** </summary>

| ID  | Key Name                   | Usage                                                  | Description |
| --- | -------------------------- | ------------------------------------------------------ | ----------- |
| 0   | VolumeEnergyDensity_J_m3   | JPT.VolumeEnergyDensityUnit.VolumeEnergyDensity_J_m3   | $J/mm^3$    |
| 1   | VolumeEnergyDensity_J_mm3  | JPT.VolumeEnergyDensityUnit.VolumeEnergyDensity_J_mm3  | $J/m^3$     |
| 2   | VolumeEnergyDensity_mJ_mm3 | JPT.VolumeEnergyDensityUnit.VolumeEnergyDensity_mJ_mm3 | $mJ/mm^3$   |

</details>

<details>

Available units for electrical resistivity.

<summary> **`ElectricalResistivityUnit`** </summary>

| ID  | Key Name                     | Usage  | Description |
| --- | ---------------------------- | ------ | ----------- |
| 0   | ElectricalResistivity_Ohm_m  | Ohm-m  |             |
| 1   | ElectricalResistivity_Ohm_mm | Ohm-mm |             |

</details>

<details>

Available units for stress reciprocal.

<summary> **`StressReciprocalUnit(temp) `** </summary>

</details>

<details>

Available units for thermal radiation.

<summary> **`ThermalRadiationUnit`** </summary>

| ID  | Key Name                     | Usage                                                 | Description |
| --- | ---------------------------- | ----------------------------------------------------- | ----------- |
| 0   | ThermalRadiation_W_m2K4      | JPT.ThermalRadiationUnit.ThermalRadiation_W_m2K4      | $mm^2/N$    |
| 1   | ThermalRadiation_mW_mm2K4    | JPT.ThermalRadiationUnit.ThermalRadiation_mW_mm2K4    | $m^2/N$     |
| 2   | ThermalRadiation_kcal_smm2K4 | JPT.ThermalRadiationUnit.ThermalRadiation_kcal_smm2K4 | $mm^2/mN$   |

</details>

<details>

Available units for displacement.

<summary> **`DisplacementUnit`** </summary>

| ID  | Key Name        | Usage                            | Description |
| --- | --------------- | -------------------------------- | ----------- |
| 0   | Displacement_mm | JPT.Displacement.Displacement_mm | $mm$        |
| 1   | Displacement_m  | JPT.Displacement.Displacement_m  | $m          |
| 2   | Displacement_ft | JPT.Displacement.Displacement_ft | $ft$        |
| 3   | Displacement_in | JPT.Displacement.Displacement_in | $in$        |
| 4   | Displacement_cm | JPT.Displacement.Displacement_cm | $cm$        |

</details>

<details>

Available units for energy density.

<summary> **`EnergyDensityUnit`** </summary>

| ID  | Key Name               | Usage                                        | Description |
| --- | ---------------------- | -------------------------------------------- | ----------- |
| 0   | EnergyDensity_J_m3     | JPT.EnergyDensityUnit.EnergyDensity_J_m3     | $mJ/mm^3$   |
| 1   | EnergyDensity_mJ_mm3   | JPT.EnergyDensityUnit.EnergyDensity_mJ_mm3   | $J/m^3$     |
| 2   | EnergyDensity_Kcal_mm3 | JPT.EnergyDensityUnit.EnergyDensity_Kcal_mm3 | $Kcal/mm^3$ |

</details>

<details>

Available units for temperature gradient.

<summary> **`TemperatureGradientUnit`** </summary>

| ID  | Key Name                 | Usage                                                | Description |
| --- | ------------------------ | ---------------------------------------------------- | ----------- |
| 0   | TemperatureGradient_K_m  | JPT.TemperatureGradientUnit.TemperatureGradient_K_m  | $K/m$       |
| 1   | TemperatureGradient_K_mm | JPT.TemperatureGradientUnit.TemperatureGradient_K_mm | $K/mm$      |

</details>

<details>

Available units for current.

<summary> **`CurrentUnit`** </summary>

| ID  | Key Name   | Usage                      | Description |
| --- | ---------- | -------------------------- | ----------- |
| 0   | Current_A  | JPT.CurrentUnit.Current_A  | $A$         |
| 1   | Current_mA | JPT.CurrentUnit.Current_mA | $mA$        |
| 2   | Current_uA | JPT.CurrentUnit.Current_uA | $uA$        |
| 3   | Current_kA | JPT.CurrentUnit.Current_kA | $kA$        |

</details>

<details>

Available units for voltage.

<summary> **`VoltageUnit`** </summary>

| ID  | Key Name   | Usage                      | Description |
| --- | ---------- | -------------------------- | ----------- |
| 0   | Voltage_V  | JPT.VoltageUnit.Voltage_V  | $V$         |
| 1   | Voltage_mV | JPT.VoltageUnit.Voltage_mV | $mV$        |
| 2   | Voltage_uV | JPT.VoltageUnit.Voltage_uV | $uV$        |
| 3   | Voltage_kV | JPT.VoltageUnit.Voltage_kV | $kV$        |

</details>
