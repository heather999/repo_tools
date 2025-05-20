from repo_tools import export_chained_collection

#repo = "dp1"
repo = "/sdf/group/rubin/repo/main"
parent_chain = "HSC/runs/PDR2/UDEEP/v24_1_0_rc2/DM-39132"

butler = export_chained_collection(repo, parent_chain)

