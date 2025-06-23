# smind_cli.py
# Minimal CLI tool to generate SMIND loop scaffolding

import os
import argparse
from datetime import datetime

TEMPLATE_PACER = """loop_id: {loop_id}"""

TEMPLATE_CLAIM = """# ⌬ Claim — {loop_id}: {topic}

---

> _Powered by **Second Mind OS**._

"""

TEMPLATE_REFLECT = """# Reflect — {loop_id}: {topic}

---

> _Powered by **Second Mind OS**._

"""

TEMPLATE_NOTE = """# {loop_id} — {topic}

---

> _Powered by [**Second Mind OS Lab**](https://github.com/smindlab) — Protocol-first learning system for cognitive leverage._

"""

TEMPLATE_LOG = """# Log — {today}

---

**Powered by Second Mind OS** — _Log-traceable insight loops for deep learning._

"""

TEMPLATE_OUTPUT = """# Output — {loop_id}: {topic}

---

> _Powered by Second Mind OS_

"""


def create_file(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"- {path}")


def init_loop(loop_id, topic):
    today = datetime.today().strftime("%Y-%m-%d")

    os.makedirs(f"loop/{loop_id}", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    os.makedirs(f"outputs/{loop_id}", exist_ok=True)

    create_file(
        f"docs/{loop_id}.md",
        TEMPLATE_NOTE.format(loop_id=loop_id, topic=topic),
    )
    create_file(f"logs/{today}-{loop_id}.md", TEMPLATE_LOG.format(today=today))
    create_file(
        f"loop/{loop_id}/pacer.yaml",
        TEMPLATE_PACER.format(loop_id=loop_id, topic=topic, today=today),
    )
    create_file(
        f"loop/{loop_id}/claim.md",
        TEMPLATE_CLAIM.format(loop_id=loop_id, topic=topic),
    )
    create_file(
        f"loop/{loop_id}/reflect.md",
        TEMPLATE_REFLECT.format(loop_id=loop_id, topic=topic),
    )
    create_file(
        f"outputs/{loop_id}/output.md",
        TEMPLATE_OUTPUT.format(loop_id=loop_id, topic=topic, today=today),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Initialize a new SMIND learning loop."
    )
    parser.add_argument("loop_id", type=str, help="Loop ID (e.g. week-01-c)")
    parser.add_argument(
        "--topic", type=str, required=True, help="Topic or focus of the loop"
    )

    args = parser.parse_args()
    init_loop(args.loop_id, args.topic)
