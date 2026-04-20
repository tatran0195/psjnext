# Title:   Home.AddResults.UsersResult()
# Desc:    Add user result to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.UsersResult
# ---
# Put your sample files
mesh = "C:/Temp/mesh.bdf"
result = "C:/Temp/result.csv"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(mesh)
# Add result to the mesh file.
Home.AddResults.UsersResult(strlPath=result)  # [hl]
