# Title:   Home.ImportMesh.FrontISTR()
# Desc:    Import an FrontISTR file (*.msh) to the Jupiter Database (Mesh, boundary conditions, etc.)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportMesh.FrontISTR
# ---
from os import environ

FrontISTR_file_path = environ["Temp"] + "/TechnoStar/"
FrontISTR_job_name = "Job_1"

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

JPT.Exec(f'FrontISTR_LinearStatic("{FrontISTR_file_path}", \  # [hl:start]
        [], "{FrontISTR_job_name}", 3, 20000, 2, 0, 0, 1e-06, 1, 0, 0, 0, "", "STEP0", 0, \
        ["AP1", 0.25, 10, 50, 10, 1, 1.25, 1, 1, 1, 5, 0.25, 5], \
        0, ["TP1", 0, 0, 0, 0, 0, 0], 1e-05, 10, 0, 0, 0, "", "", \
        0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 0, 1, 1, 1, 1, 0, 0, \
        0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, "", "", "", "", "", "", "", "", 0, 0, 1, \
        "10", "1.0e-8", "60", 0, 0, "", "", "", "", "0.0", "1.0", 0, 0, \
        "0.0", "0.0", "0.log", "", "1.0e-8", "10", 1, "1", 0, 0, 0, 0, "", "", 1, 0, 0)')  # [hl:end]

JPT.Exec('New Document()')
import_status = Home.ImportMesh.FrontISTR(strlPaths=[FrontISTR_file_path+FrontISTR_job_name+".msh"])
JPT.Debugger(import_status)
