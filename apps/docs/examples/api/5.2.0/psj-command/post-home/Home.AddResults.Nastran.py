# Title:   Home.AddResults.Nastran()
# Desc:    Add Nastran Op2 results to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.Nastran
# ---
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.op2"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Nastran(strlPaths=[Result], bMergeTree=False)  # [hl]
