# Demo url - https://healthcare-pharma-ai-fde-642990533848.asia-southeast1.run.app/

# Cursor reference for Workflows - https://cursor.com/dashboard/shared-chats?shareId=persona-e2e-ui-specs-_mrLhmLulmpd
# Project AEGIS-PHARMA — Pharmaceutical AI FDE Capstone

A challenge-only, fully synthetic and offline-capable AI Forward Deployed Engineering capstone for a fictional global pharmaceutical enterprise.

## Package scale

- 84 disclosed, cross-linked injects across 13 dimensions.
- Three mandatory, safety-bounded workflows.
- 139 original synthetic operational datasets plus generated integrity metadata.
- 32 mixed-authority knowledge documents with complete cataloguing.
- Deliberately defective brownfield Python and JavaScript components.
- 15 public scenarios with reproducible local evidence bundles.
- Executable fail-closed response contracts and positive/negative tests.
- 30 structured participant artefact templates.
- 180-point scoring model with non-negotiable GxP, safety and security gates.
- Cross-platform offline preflight and strict final-submission validation.

## Start

Read `START_HERE.md`, then run:

```text
python run_capstone.py --check
```

All participant work belongs under `submission/`. The original challenge evidence is protected by `FILE_HASHES.csv`.

## Non-negotiable boundary

The package contains no solution, answer key, completed POC, batch-release decision, safety-case decision, clinical recommendation, stock allocation, recall instruction or finished elevator pitch. It is synthetic training material and is not suitable for real GxP, clinical, safety, regulatory, supply or patient use.

## **********************************************************************************************
# Graphify V1 → V2 → V3 Version Comparison

This README explains how to reproduce the complete Graphify version-comparison workflow on another Windows machine.

The solution:

1. Creates isolated Git worktrees for three application versions.
2. Generates an independent Graphify knowledge graph for each version.
3. Compares the three graphs deterministically using Python.
4. Generates an interactive browser visualization showing how the solution evolved across versions.

---

## 1. Repository

Repository:

```text
https://github.com/abhinavarya3131-lgtm/Healthcare-Pharma-AI-FDE.git
```

### Version Mapping

| Application Version | Git Branch |
| ------------------- | ---------- |
| V1                  | `V-1`      |
| V2                  | `V-2`      |
| V3                  | `V-3`      |

The branch names must be used exactly as shown above.

---

# 2. Final Output

The comparison supports:

```text
V1 → V2
V2 → V3
V1 → V3
```

Changes are classified as:

```text
GREEN   = Added
RED     = Removed
AMBER   = Modified
GREY    = Unchanged
```

The visualization provides:

* Version comparison selector
* Added filter
* Removed filter
* Modified filter
* Unchanged filter
* Node-type filter
* Search
* Zoom
* Pan
* Fit-to-screen
* Clickable nodes
* Node details
* Relationship details
* Summary counts

---

# 3. Prerequisites

Install the following:

* Git
* Python 3.10+
* Node.js/npm
* VS Code
* OpenCode
* `uv`
* Graphify
* Access to the private GitHub repository

Verify:

```powershell
git --version
python --version
node --version
npm --version
```

---

# 4. Install OpenCode

```powershell
npm install -g opencode-ai
```

Verify:

```powershell
opencode --version
```

---

# 5. Install uv

```powershell
winget install astral-sh.uv
```

Restart the terminal.

Verify:

```powershell
uv --version
```

---

# 6. Install Graphify

Install:

```powershell
uv tool install graphifyy
```

If Graphify is already installed:

```powershell
uv tool upgrade graphifyy
```

Update the shell PATH if required:

```powershell
uv tool update-shell
```

Restart VS Code or PowerShell.

Verify:

```powershell
graphify --version
```

---

# 7. Install Graphify Integration for OpenCode

Run:

```powershell
graphify install --platform opencode
```

This installs the Graphify skill that OpenCode can use.

---

# 8. GitHub Authentication

The repository is private, so Git on the new machine must be authenticated.

If GitHub CLI is available:

```powershell
gh auth login
```

Select:

```text
GitHub.com
HTTPS
Login with a web browser
```

Then:

```powershell
gh auth setup-git
```

Test repository access:

```powershell
git ls-remote https://github.com/abhinavarya3131-lgtm/Healthcare-Pharma-AI-FDE.git
```

If commit hashes and refs are returned, access is working.

If `gh` is not installed:

```powershell
winget install --id GitHub.cli --source winget
```

Restart the terminal and repeat the authentication steps.

---

# 9. Create Working Directory

The example below uses:

```text
C:\GraphifyComparison
```

Create it:

```powershell
mkdir C:\GraphifyComparison
cd C:\GraphifyComparison
```

---

# 10. Clone the Repository

```powershell
git clone https://github.com/abhinavarya3131-lgtm/Healthcare-Pharma-AI-FDE.git
```

Enter the repository:

```powershell
cd C:\GraphifyComparison\Healthcare-Pharma-AI-FDE
```

Fetch the latest branches:

```powershell
git fetch origin --prune
```

Check:

```powershell
git branch -r
```

Confirm that these branches exist:

```text
origin/V-1
origin/V-2
origin/V-3
```

---

# 11. Create Separate Git Worktrees

Create an isolated worktree for each application version.

### V1

```powershell
git worktree add --detach ..\graphify-v1 origin/V-1
```

### V2

```powershell
git worktree add --detach ..\graphify-v2 origin/V-2
```

### V3

```powershell
git worktree add --detach ..\graphify-v3 origin/V-3
```

Verify:

```powershell
git worktree list
```

Expected structure:

```text
C:\GraphifyComparison
│
├── Healthcare-Pharma-AI-FDE
│
├── graphify-v1
│
├── graphify-v2
│
└── graphify-v3
```

The worktrees are intentionally created using detached HEAD because they are being used for analysis rather than development.

---

# 12. Generate Graphify Graph for V1

Move to V1:

```powershell
cd C:\GraphifyComparison\graphify-v1
```

Start OpenCode using Nemotron:

```powershell
opencode --model opencode/nemotron-3-ultra-free
```

Inside OpenCode run:

```text
/graphify .
```

If `/graphify` does not appear in autocomplete, type it manually.

Alternatively ask OpenCode:

```text
Load the Graphify skill and generate a complete Graphify knowledge graph for the current repository.

Use the currently selected OpenCode model for semantic extraction.
```

After completion, verify:

```powershell
Test-Path .\graphify-out\graph.json
```

Expected:

```text
True
```

---

# 13. Generate Graphify Graph for V2

Move to V2:

```powershell
cd C:\GraphifyComparison\graphify-v2
```

Start OpenCode:

```powershell
opencode --model opencode/nemotron-3-ultra-free
```

Inside OpenCode:

```text
/graphify .
```

Verify afterward:

```powershell
Test-Path .\graphify-out\graph.json
```

Expected:

```text
True
```

---

# 14. Generate Graphify Graph for V3

Move to V3:

```powershell
cd C:\GraphifyComparison\graphify-v3
```

Start OpenCode:

```powershell
opencode --model opencode/nemotron-3-ultra-free
```

Inside OpenCode:

```text
/graphify .
```

Verify:

```powershell
Test-Path .\graphify-out\graph.json
```

Expected:

```text
True
```

---

# 15. Required Graph Inputs

Before continuing, verify all three graphs exist:

```powershell
Test-Path C:\GraphifyComparison\graphify-v1\graphify-out\graph.json

Test-Path C:\GraphifyComparison\graphify-v2\graphify-out\graph.json

Test-Path C:\GraphifyComparison\graphify-v3\graphify-out\graph.json
```

All three commands must return:

```text
True
```

The required inputs are:

```text
graphify-v1
└── graphify-out
    └── graph.json

graphify-v2
└── graphify-out
    └── graph.json

graphify-v3
└── graphify-out
    └── graph.json
```

---

# 16. Important Consistency Rule

V1, V2 and V3 should be generated using the same:

```text
Graphify version
OpenCode model
Semantic extraction approach
Graphify configuration
```

This reduces the possibility that extraction differences are incorrectly interpreted as application-version differences.

---

# 17. Create the Comparison Directory

Create:

```powershell
mkdir C:\GraphifyComparison\graphify-version-comparison
```

The working comparison utility should contain:

```text
graphify-version-comparison
│
├── schema_inspect.py
├── compare_graphs.py
├── graphify-version-diff.html
└── validate.py
```

These are the reusable comparison files created for this solution.

The following files are generated when the utility runs:

```text
schema-report.json
comparison.json
comparison-summary.md
```

---

# 18. Recommended Portable Directory Structure

The complete structure should be:

```text
C:\GraphifyComparison
│
├── Healthcare-Pharma-AI-FDE
│
├── graphify-v1
│   └── graphify-out
│       └── graph.json
│
├── graphify-v2
│   └── graphify-out
│       └── graph.json
│
├── graphify-v3
│   └── graphify-out
│       └── graph.json
│
└── graphify-version-comparison
    ├── schema_inspect.py
    ├── compare_graphs.py
    ├── graphify-version-diff.html
    └── validate.py
```

---

# 19. Check for Machine-Specific Paths

Before running the utility on another machine:

```powershell
cd C:\GraphifyComparison\graphify-version-comparison
```

Search the Python files for old machine paths:

```powershell
Select-String -Path *.py -Pattern "C:\\Users\\"
```

If old paths are present, update them.

The graph locations should point to:

```text
C:\GraphifyComparison\graphify-v1\graphify-out\graph.json

C:\GraphifyComparison\graphify-v2\graphify-out\graph.json

C:\GraphifyComparison\graphify-v3\graphify-out\graph.json
```

Prefer relative paths where possible:

```text
..\graphify-v1\graphify-out\graph.json

..\graphify-v2\graphify-out\graph.json

..\graphify-v3\graphify-out\graph.json
```

Relative paths make the utility portable between machines.

---

# 20. Inspect the Graphify Schemas

Move to:

```powershell
cd C:\GraphifyComparison\graphify-version-comparison
```

Run:

```powershell
python schema_inspect.py
```

This inspects the Graphify schema and creates:

```text
schema-report.json
```

The script should inspect:

* Node structure
* Node IDs
* Node type
* Node name
* Source file
* Edge structure
* Edge source
* Edge target
* Relationship type
* Node counts
* Edge counts

It does not modify the original Graphify files.

---

# 21. Generate V1/V2/V3 Comparison

Run:

```powershell
python compare_graphs.py
```

The utility performs three comparisons:

```text
V1 → V2

V2 → V3

V1 → V3
```

It generates:

```text
comparison.json

comparison-summary.md
```

---

# 22. Comparison Logic

The comparison is deterministic.

The LLM does not decide whether nodes are equal.

Node matching prioritizes:

```text
Stable Graphify node ID
```

and where required:

```text
normalized node type
+
normalized node name
+
source/file
```

Edge comparison uses:

```text
source node
+
target node
+
relationship type
```

Changes are classified as:

```text
ADDED
REMOVED
MODIFIED
UNCHANGED
UNCERTAIN_MATCH
```

---

# 23. comparison.json Structure

The output should contain:

```text
v1_to_v2
v2_to_v3
v1_to_v3
```

Verify:

```powershell
python -c "import json; d=json.load(open('comparison.json',encoding='utf-8')); print(list(d.keys()))"
```

Expected:

```text
['v1_to_v2', 'v2_to_v3', 'v1_to_v3']
```

Each comparison contains:

```text
version_a
version_b
node_counts
edge_counts
nodes
edges
```

Node and edge buckets contain:

```text
added
removed
modified
unchanged
uncertain_matches
```

---

# 24. Validate the Comparison

Run:

```powershell
python validate.py
```

Also verify:

```powershell
Test-Path .\comparison.json
Test-Path .\comparison-summary.md
Test-Path .\graphify-version-diff.html
```

Expected:

```text
True
True
True
```

---

# 25. Start the Visualization Server

The visualization reads `comparison.json` dynamically.

Therefore:

**Do not double-click `graphify-version-diff.html`.**

Opening it directly produces a URL such as:

```text
file:///C:/...
```

and the browser may block JavaScript from loading `comparison.json`.

Instead run:

```powershell
cd C:\GraphifyComparison\graphify-version-comparison
```

Then:

```powershell
python -m http.server 8765
```

Expected:

```text
Serving HTTP on ... port 8765
```

Leave this terminal running.

---

# 26. Verify the Local Server

Open another PowerShell terminal.

Check `comparison.json`:

```powershell
Invoke-WebRequest "http://localhost:8765/comparison.json" -UseBasicParsing |
Select-Object StatusCode, RawContentLength
```

Expected:

```text
StatusCode       : 200
RawContentLength : greater than 0
```

Check the HTML:

```powershell
Invoke-WebRequest "http://localhost:8765/graphify-version-diff.html" -UseBasicParsing |
Select-Object StatusCode, RawContentLength
```

Expected:

```text
StatusCode       : 200
RawContentLength : greater than 0
```

---

# 27. Open the Interactive Visualization

Run:

```powershell
Start-Process "http://localhost:8765/graphify-version-diff.html"
```

The browser URL must be:

```text
http://localhost:8765/graphify-version-diff.html
```

and NOT:

```text
file:///C:/...
```

---

# 28. Using the Dashboard

The version selector supports:

```text
V1 → V2

V2 → V3

V1 → V3
```

Node colors:

```text
GREEN  = Added

RED    = Removed

AMBER  = Modified

GREY   = Unchanged
```

Relationship colors:

```text
GREEN       = Added relationship

RED/DASHED  = Removed relationship

AMBER       = Modified relationship

GREY        = Unchanged relationship
```

---

# 29. Recommended Default Filters

For large graphs keep:

```text
Added       ON

Removed     ON

Modified    ON

Unchanged   OFF
```

Turning on all unchanged nodes can make a large graph difficult to navigate.

Enable unchanged nodes only when additional architectural context is required.

---

# 30. Search and Navigation

The dashboard provides:

* Node search
* Node-type filtering
* Zoom
* Pan
* Fit-to-screen
* Node selection
* Node details
* Relationship inspection

Click a node to inspect:

```text
Node name
Node ID
Node type
Change status
Associated metadata
```

---

# 31. End-to-End Architecture

```text
                    GitHub Repository
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
         V-1              V-2              V-3
          │                │                │
          ▼                ▼                ▼
    graphify-v1      graphify-v2      graphify-v3
          │                │                │
          ▼                ▼                ▼
       Graphify          Graphify          Graphify
          │                │                │
          ▼                ▼                ▼
      graph.json       graph.json       graph.json
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                   schema_inspect.py
                           │
                           ▼
                    schema-report.json
                           │
                           ▼
                    compare_graphs.py
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
        comparison.json     comparison-summary.md
                │
                ▼
      graphify-version-diff.html
                │
                ▼
       Python HTTP Server
                │
                ▼
        localhost:8765
                │
                ▼
       Interactive Graph Diff
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
     V1→V2    V2→V3    V1→V3
```

---

# 32. Quick Execution — After Initial Setup

Once the machine has been configured and the three Graphify graphs exist:

```powershell
cd C:\GraphifyComparison\graphify-version-comparison
```

Run:

```powershell
python schema_inspect.py
```

Then:

```powershell
python compare_graphs.py
```

Then:

```powershell
python validate.py
```

Start the server:

```powershell
python -m http.server 8765
```

Open:

```text
http://localhost:8765/graphify-version-diff.html
```

---

# 33. Re-run After a Version Changes

If, for example, V3 changes:

```powershell
cd C:\GraphifyComparison\Healthcare-Pharma-AI-FDE
```

Fetch:

```powershell
git fetch origin --prune
```

Update/recreate the V3 analysis worktree as required and regenerate:

```text
graphify-v3\graphify-out\graph.json
```

Then rerun:

```powershell
cd C:\GraphifyComparison\graphify-version-comparison

python schema_inspect.py

python compare_graphs.py

python validate.py
```

Refresh the browser:

```text
Ctrl + Shift + R
```

If V1 and V2 have not changed, their Graphify graphs do not need to be regenerated.

---

# 34. Troubleshooting — Blank Graph

If the dashboard loads but no graph appears, verify the browser is using:

```text
http://localhost:8765/graphify-version-diff.html
```

not:

```text
file:///C:/...
```

Then verify:

```powershell
Invoke-WebRequest "http://localhost:8765/comparison.json" -UseBasicParsing |
Select-Object StatusCode, RawContentLength
```

The status must be:

```text
200
```

and the content length must be greater than zero.

---

# 35. Troubleshooting — Port Already in Use

If port `8765` is unavailable:

```powershell
python -m http.server 9000
```

Then open:

```text
http://localhost:9000/graphify-version-diff.html
```

---

# 36. Troubleshooting — Graphify Skill Not Visible

If `/graphify` does not appear in OpenCode autocomplete:

```powershell
graphify install --platform opencode
```

Restart OpenCode.

Then either type:

```text
/graphify .
```

manually or ask:

```text
Load the Graphify skill and generate the knowledge graph for the current repository.
```

---

# 37. Troubleshooting — Nemotron Timeout

Long OpenCode/Nemotron operations may occasionally time out.

Avoid asking the model to:

* Read all three large `graph.json` files
* Build the comparison itself
* Generate a massive HTML containing all graph data

The intended architecture is:

```text
OpenCode/Nemotron
       │
       ▼
Generate Graphify graphs / development assistance

Python
       │
       ▼
Perform deterministic V1/V2/V3 comparison

Browser JavaScript
       │
       ▼
Render comparison.json interactively
```

Once the three Graphify `graph.json` files exist, the comparison does not require an LLM.

---

# 38. Important Security Note

Do not:

```text
Commit API keys
Commit tokens
Store credentials in source code
```

If API keys are required for an alternative Graphify backend, provide them through environment variables.

Example:

```powershell
$env:ANTHROPIC_API_KEY="YOUR_KEY"
```

Never commit `.env` files containing secrets unless the file is safely excluded from Git.

---

# 39. Cleaning Up Worktrees

When the comparison environment is no longer required:

```powershell
cd C:\GraphifyComparison\Healthcare-Pharma-AI-FDE
```

Remove:

```powershell
git worktree remove ..\graphify-v1

git worktree remove ..\graphify-v2

git worktree remove ..\graphify-v3
```

Then:

```powershell
git worktree prune
```

Only remove worktrees after confirming that no required generated outputs need to be retained.

---

# 40. Final Deliverables

The primary outputs of the solution are:

### Machine-readable comparison

```text
comparison.json
```

### Human-readable comparison

```text
comparison-summary.md
```

### Interactive visualization

```text
graphify-version-diff.html
```

### Graphify source graphs

```text
graphify-v1\graphify-out\graph.json

graphify-v2\graphify-out\graph.json

graphify-v3\graphify-out\graph.json
```

---

## Final Workflow Summary

```text
V-1 ──► Graphify ──► V1 Graph ─┐
                               │
V-2 ──► Graphify ──► V2 Graph ─┼──► Deterministic Python Diff
                               │             │
V-3 ──► Graphify ──► V3 Graph ─┘             ▼
                                      comparison.json
                                             │
                                             ▼
                                graphify-version-diff.html
                                             │
                                             ▼
                                  Interactive Browser View
                                             │
                                  ┌──────────┼──────────┐
                                  ▼          ▼          ▼
                                V1→V2      V2→V3      V1→V3
```

This setup allows the V1/V2/V3 application evolution to be reproduced consistently on another machine while keeping all three Git versions and Graphify knowledge graphs isolated.


