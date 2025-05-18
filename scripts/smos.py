# smos_cli.py
# Minimal CLI tool to generate SMOS loop scaffolding

import os
import argparse
from datetime import datetime

TEMPLATE_PACER = """loop_id: {loop_id}
topic: {topic}
plan:
  - TODO: Define objective
  - TODO: Define scope
  - TODO: Define constraints
outputs:
  - outputs/{loop_id}-output.md
logs:
  - logs/{today}-{loop_id}-log.md
status: in-progress
claims:
  - ⌬ TODO: Write symbolic claim
"""

TEMPLATE_NOTE = """# {loop_id} — {topic}

## Concepts
- 

## Code examples
- 

## Insight
- 

## Questions
- 
"""

TEMPLATE_LOG = """# Log — {today}

## Blockers 🚧
- 

## Resolutions 🛠️
- 

## Pings 💡
- 
"""

TEMPLATE_OUTPUT = """# Output — {loop_id}

## Summary

## Final Code

## Reflection

## Link

Verified: logs/{today}-{loop_id}-log.md

⌬ Mindstamp: TODO

Powered by Second Mind OS
"""


def create_file(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ Created: {path}")


def init_loop(loop_id, topic):
    today = datetime.today().strftime("%Y-%m-%d")

    os.makedirs(f"loop/{loop_id}", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    create_file(
        f"loop/{loop_id}/pacer.yaml",
        TEMPLATE_PACER.format(loop_id=loop_id, topic=topic, today=today),
    )
    create_file(
        f"docs/{loop_id}.md",
        TEMPLATE_NOTE.format(loop_id=loop_id, topic=topic),
    )
    create_file(
        f"logs/{today}-{loop_id}-log.md", TEMPLATE_LOG.format(today=today)
    )
    create_file(
        f"outputs/{loop_id}-output.md",
        TEMPLATE_OUTPUT.format(loop_id=loop_id, today=today),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Initialize a new SMOS learning loop."
    )
    parser.add_argument("loop_id", type=str, help="Loop ID (e.g. week-01)")
    parser.add_argument(
        "--topic", type=str, required=True, help="Topic or focus of the loop"
    )

    args = parser.parse_args()
    init_loop(args.loop_id, args.topic)
