# Task 2 - Git Merge vs Git Rebase

This document shows the difference between git merge and git rebase by creating branches and integrating them back to main.

## Setup

Created two branches from main and made them diverge with commits.

### Commands Run:

1. **Create branches:**

   ```bash
   git checkout -b branch-1
   git checkout -b branch-2
   ```

2. **Add commit on main to make branches diverge:**

   ```bash
   git checkout main
   git commit -m "chore: test_file"
   ```

3. **Add commit on branch-1:**

   ```bash
   git checkout branch-1
   git commit -m "feat: Commit C on branch-1"
   ```

4. **Add commit on branch-2:**

   ```bash
   git checkout branch-2
   git commit -m "feat: Commit D on branch-2"
   ```

## Merge Operation

Integrated branch-1 into main using git merge.

### Commands Run:

1. **Merge branch-1:**

   ```bash
   git checkout main
   git merge branch-1
   ```

The merge created a merge commit that preserves the branch history.

## Rebase Operation

Integrated branch-2 into main using git rebase.

### Commands Run:

1. **Rebase branch-2 onto main:**

   ```bash
   git checkout branch-2
   git rebase main
   ```

The rebase rewrote the commit history to appear linear.

## Final Result

Checked the complete git history to see both merge and rebase results.

```bash
git log --graph
```

## Key Differences

**Merge:**

- Preserves original branch history
- Creates merge commits
- Shows when branches diverged and merged
- History looks like a tree with branches

**Rebase:**

- Rewrites commit history
- Makes history look linear
- Loses information about when branching happened
- History appears as a straight line

Choose merge for shared branches and rebase for cleaning up local feature branches.

## Screenshots

branch-1 merge to the main branch showing the merge commits to merge the two branch togethere
![Initial setup with diverging branches](screenshots/Screenshot%202025-12-05%20at%2012.39.56 PM.png)

history of the entire commands ran to achive this result
![Merge result showing non-linear history](screenshots/Screenshot%202025-12-05%20at%2012.40.57 PM.png)
![Final git log showing both merge and rebase histories](screenshots/Screenshot%202025-12-05%20at%2012.43.11 PM.png)

after the rebase from the main branch so to rewrite the commit D on the history fetched from the main
![Rebase result showing linear history](screenshots/Screenshot%202025-12-05%20at%2012.42.37 PM.png)

git tree after the merge and the rebase
![Additional verification of git history](screenshots/Screenshot%202025-12-05%20at%2012.47.41 PM.png)
