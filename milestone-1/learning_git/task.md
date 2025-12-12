# Task 2 - Git Merge vs Git Rebase

This document shows the difference between `git merge` and `git rebase` by creating branches, integrating the changes from `main` _into_ the feature branches, and then pushing the updated history back to the remote repository. This demonstrates a common workflow for keeping feature branches up-to-date.

## Setup and Remote Operations

The first phase involved creating the necessary branches and publishing them to the remote (`origin`) before making the branches diverge.

### Commands Run:

1.  **Initial Commit and Push to `origin`:**

    ```bash
    git commit -m "feat: Initial commit (A)"
    git push -u origin main
    ```

2.  **Create, Publish, and Diverge:**

    ```bash
    # Create branches locally and push to remote
    git checkout -b branch-1
    git push -u origin branch-1
    git checkout -b branch-2
    git push -u origin branch-2

    # Create Commit B on main (the divergence point)
    git checkout main
    git commit -m "chore: Commit B on main"
    git push origin main
    ```

3.  **Add Feature Commits (C and D) and Push:**

    ```bash
    # Add Commit C and push
    git checkout branch-1
    git commit -m "feat: Commit C on branch-1"
    git push origin branch-1

    # Add Commit D and push
    git checkout branch-2
    git commit -m "feat: Commit D on branch-2"
    git push origin branch-2
    ```

![](./screenshots/Screenshot 2025-12-05 at 4.06.43 PM.png)

![](./screenshots/Screenshot%202025-12-05%20at%204.08.15 PM.png)

### Merge Operation (`main` into `branch-1`)

The merge operation was performed on `branch-1` to pull `main`'s changes.

#### Commands Run:

1.  **Perform Merge:**
    ```bash
    git checkout branch-1
    git merge main
    ```
2.  **Publish Changes:**
    ```bash
    git push origin branch-1
    ```

![](./screenshots/Screenshot%202025-12-05%20at%204.12.09 PM.png)

The merge created a **Merge Commit (M)** on `branch-1`. This new commit incorporates `main`'s history (**B**) while preserving the original timeline of `branch-1` (**C**).

### Rebase Operation (`branch-2` onto `main`)

The rebase operation was performed on `branch-2` to clean up its history by placing it on top of `main`.

#### Commands Run:

1.  **Perform Rebase:**
    ```bash
    git checkout branch-2
    git rebase main
    ```
2.  **Publish Changes (History Rewritten):**
    ```bash
    git push origin branch-2 --force
    ```

![](./screenshots/Screenshot%202025-12-05%20at%204.14.44 PM.png)

The rebase **rewrote Commit D** as **D'** and moved it to appear immediately after `main`'s commit (**B**). Because the local history was altered, a **forced push (`--force`)** was required to update the remote branch.

# graph

![](./screenshots/Screenshot%202025-12-05%20at%204.33.44 PM.png)

![](./screenshots/20251205_162850.jpg)
