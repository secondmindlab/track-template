# Log — YYYY-MM-DD-topic-tag

## 1. Focus Unit & Context

**Track:** [track-name]  
**Week:** 01  
**Problem:** `pset1-mario`  
**Current Phase:** Debug + Reflection  
**Related files:**

- `docs/week-01-c.md`
- `loop/week-01-c/pacer.yaml`
- `outputs/week-01-c/output.md`

## 2. 🚧 Blockers, Bugs, and Blindspots

- Infinite loop in `mario.c` when `n = 1` → stack overflow suspicion
- Confusion about how `printf("\n")` interacts with loop count
- Misunderstood `i--` vs `--i` inside nested loop

## 3. 🛠️ Resolution & Fix Strategy

- Used `printf("i: %d j: %d\n", i, j)` for trace-based debugging
- Re-read CS50 walkthrough → matched with my code
- Rewrote condition as: `for (int i = 0; i < height; i++)`  
  → Resolved control flow logic

## 4. 📣 Insights & Claims (`⌬`)

- ⌬ Loop order always reveals mental model: outer = rows, inner = cols
- ⌬ Debugging = trace over theory → always anchor back to observable I/O
- ⌬ Bugs are often off-by-one mindset blindspots, not syntax

## 5. 🏛 Meta Reflection (System Layer)

> What did I learn about how I learn?

- I waste time when I try to “figure it out in my head” — should **externalize state early**
- Debug logs are 10x leverage over mental simulation
- From now on, I’ll use trace-dump before asking GPT or rereading docs

## 6. Next Steps

- Update `outputs/week-01-c/output.md` with fixed version + ⌬ claims
- Start new PACER loop for Week-02
- Share selected insight card to LinkedIn ("⌬ Debug = trace > theory")

---

**Powered by Second Mind OS** — _Log-traceable insight loops for deep learning._
