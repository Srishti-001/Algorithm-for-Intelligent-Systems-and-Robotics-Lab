# Experiment 7: Mobile Robot Simulation in Webots
**Author:** Srishti Batham (500124490), Batch B2
**Platform:** Webots R2025a, Python 3.12, Windows 11

## Executed Commands:
1. Swarm Arena simulation (Part A):
   `python tools/run_experiment.py swarm --seconds 120`
   `python tools/run_experiment.py swarm --seconds 120 --set cruise=0.9`

2. Pioneer 3-DX Lidar Navigation (Part B):
   `python tools/run_experiment.py pioneer --seconds 180 --set bubble=0.25`

## Key Findings:
- Higher cruise speeds increase arena exploration rate but also increase collision/corner entrapment risk.
- Follow-the-gap navigation requires a safety bubble radius strictly larger than the robot half-width (0.15 m) to prevent corner clipping.
