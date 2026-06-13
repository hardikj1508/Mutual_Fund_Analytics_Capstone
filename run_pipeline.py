"""
Master execution script for Mutual Fund Analytics Project
"""

import os

print("Starting Mutual Fund Analytics Pipeline...")

print("Step 1: Running ETL Pipeline")
os.system("python scripts/etl_pipeline.py")

print("Step 2: Computing Performance Metrics")
os.system("python scripts/compute_metrics.py")

print("Step 3: Updating NAV Data")
os.system("python scripts/live_nav_fetch.py")

print("Pipeline Execution Complete")