# Title:   Home.AddResults.Sysnoise()
# Desc:    Add sysnoise result to the current Jupiter Database
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.Sysnoise
# ---
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Sysnoise(strlPaths=[Result], bMergeTree=False)  # [hl]
