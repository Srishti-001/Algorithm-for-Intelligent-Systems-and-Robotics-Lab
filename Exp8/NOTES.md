# Experiment 8: Cross-Embodiment Transfer of a Manipulation Skill
**Author:** Sarthak Jakhmola (500122482), Batch B2
**Platform:** PyBullet 3.2.7, Python 3.12, Windows 11

## Executed Commands:
1. Setup check: `python experiments/00_check_setup.py`
2. Workspace exploration: `python experiments/01_explore_embodiments.py`
3. Joint-space transfer: `python experiments/02_joint_space_transfer.py`
4. Task-space transfer: `python experiments/03_task_space_transfer.py`
5. Learn once, deploy many: `python experiments/04_learn_once_deploy_many.py`
6. Multi-embodiment learning: `python experiments/05_multi_embodiment.py`

## Core Conclusions:
- Joint space replay fails immediately on morphology mismatch (0% success on other embodiments).
- Task-space delta end-effector control enables >90% zero-shot transfer across distinct manipulator architectures.
