# Title:   Home.ImportMesh.Ansys()
# Desc:    Import an Ansys file (*.dat) to the Jupiter Database (Mesh, boundary conditions, etc.)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportMesh.Ansys
# ---
from os import environ

ansys_file_path = environ["Temp"] + "/TechnoStar/Exported_Ansys_File_EXPORT_DAT.dat"

Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)],
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=5000000.0,
                                    crlTargets=[Face(23)])

Properties.Material.Add("Stainless_Steel",
                        [Density([(DENSITY, 7.75e-09)]),
                         Elastic([(YOUNGS_MODULUS, 193000.0),
                                  (POISSONS_RATIO, 0.31)])])
Properties.Solid(crlTargets=[Part(1)],
                 strName="Cube_for_testing",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

Analysis.Ansys.LinearStatic("Job1",
                            ansysAnalysisBasic=BASIC(dTimeStepSize=1.0,
                                                     dMinTimeStep=1.0),
                            iLoadCaseId=1,
                            strFileName=ansys_file_path)

JPT.Exec('New Document()')
import_status = Home.ImportMesh.Ansys(strlPaths=[ansys_file_path])  # [hl]
JPT.Debugger(import_status)
