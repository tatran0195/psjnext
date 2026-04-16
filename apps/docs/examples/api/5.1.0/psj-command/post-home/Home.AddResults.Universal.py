# Title:   Home.AddResults.Universal()
# Desc:    Add result written in Universal file to the current Jupiter-Post Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.Universal
# ---
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.unv"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Universal(strlPaths=[Result], bMergeTree=False)  # [hl]
