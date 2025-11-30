# Orifinder
Author-Suraj Chauhan 

A Python tool to find the **Origin of Replication (oriC)** in bacterial genomes using GC Skew analysis.

##  What is this?

Imagine a bacterium's DNA is like a giant, circular race track. When a bacterium wants to make a copy of itself, it needs a specific **"Start Line."** In biology, this start line is called the **Origin of Replication**.
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/24693ea1-e41f-4373-bf03-48ba78f44e1a" />


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

   
Analysis Part

<img width="785" height="502" alt="image" src="https://github.com/user-attachments/assets/614cd0a9-33be-4bdf-b51c-d9f30536160b" />
1. The Y-Axis (Vertical Side)

This measures the Cumulative GC Skew. Think of this as a running score in a game.

    Every time the code sees a G, the score goes up.

    Every time the code sees a C, the score goes down.

    A and T do not change the score (they are worth 0 points).

2. The Downward Slope (0 to 40)

On the left side, the purple line goes steadily down. This corresponds to the first part of your synthetic DNA file where we put thousands of Cytosines (Cs). Because there are so many Cs and no Gs, the score keeps dropping lower and lower.

In a real bacteria, this represents the "lagging strand" of the DNA, which usually has more Cytosines.

3. The Flat Bottom (40 to 50)

You will notice the line goes flat at the bottom of the V shape. This is because, in the test file, we inserted a block of Adenines (As) between the Cs and the Gs. Since As and Ts are neutral in this calculation (they don't add or subtract from the score), the line stays horizontal.

4. The Upward Slope (50 to 90)

On the right side, the purple line shoots back up. This corresponds to the part of the file where we put thousands of Guanines (Gs). Because there are now many Gs, the score rises rapidly.

In a real bacteria, this represents the "leading strand," which usually has more Guanines.

5. The Red Dotted Line (The Prediction)

The red line marks the Origin of Replication. The code is programmed to find the lowest point on the graph (the minimum value).

    Because the graph hits its lowest score at position 40 and stays there until 50, the computer picked the first moment it hit that lowest score (index 40) as the "Winner."

    In biology, this turning point (where the bias switches from C-heavy to G-heavy) is the physical spot where the DNA replication machinery attaches to start copying the genome.
