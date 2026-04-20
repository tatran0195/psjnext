# Title:   Home.AddResults.Abaqus()
# Desc:    Add Abaqus .odb results to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.Abaqus
# ---
# Put your sample files
Mesh = "C:/Temp/mesh.inp"
Result = "C:/Temp/result.odb"

# Import mesh file
Home.ImportResults.ImportMesh.Abaqus(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Abaqus(strlPaths=[Result], bMergeTree=False)  # [hl]
