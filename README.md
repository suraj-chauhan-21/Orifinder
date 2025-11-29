# Orifinder
Author-Suraj Chauhan
# Simple O 🧬

A Python tool to find the **Origin of Replication (oriC)** in bacterial genomes using GC Skew analysis.

## 👶 What is this?

Imagine a bacterium's DNA is like a giant, circular race track. When a bacterium wants to make a copy of itself, it needs a specific **"Start Line."** In biology, this start line is called the **Origin of Replication**.

### How does it work?
We look for clues in the letters of the DNA (A, T, C, G).
1. We walk along the DNA and count the Gs and Cs.
2. If there are more **C**s, the graph goes **down**.
3. If there are more **G**s, the graph goes **up**.
4. The point where the graph hits the very bottom (the tip of the "V" shape) is usually the **Start Line**.

## 🛠️ Installation

1. Clone this repository or download the files.
2. Install the required library:
   ```bash
   pip install -r requirements.txt
