import sys
import matplotlib.pyplot as plt

def read_fasta(file_path):
    """
    Reads a FASTA file and returns the DNA sequence as a single string.
    """
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        # Join lines, skip headers
        sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
        return sequence.upper()
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
        return None

def calculate_gc_skew(sequence, window_size=1000):
    """
    Calculates GC Skew across the genome using a sliding window.
    Formula: (G - C) / (G + C)
    """
    skews = []
    # Adjust window size if genome is very small
    if len(sequence) < window_size:
        window_size = len(sequence) // 100
        if window_size < 1: window_size = 1
    
    print(f"⚙️  Using window size: {window_size} bp")

    for i in range(0, len(sequence), window_size):
        chunk = sequence[i : i + window_size]
        g = chunk.count('G')
        c = chunk.count('C')
        
        if g + c == 0:
            skew = 0
        else:
            skew = (g - c) / (g + c)
        skews.append(skew)
        
    return skews, window_size

def calculate_cumulative_skew(skews):
    """
    Calculates the cumulative sum of skews to visualize the 'V' shape.
    """
    cumulative = []
    current_sum = 0
    for val in skews:
        current_sum += val
        cumulative.append(current_sum)
    return cumulative

def main():
    # Check for command line argument
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-'):
        filename = sys.argv[1]
    else:
        print("⚠️ No file provided. Usage: python orifinder.py <file.fasta>")
        return

    print(f"🧬 Reading file: {filename}...")
    dna_seq = read_fasta(filename)
    
    if dna_seq is None:
        return

    print(f"📏 Genome Length: {len(dna_seq)} base pairs")
    
    # Calculation
    print("🧮 Calculating GC Skew...")
    raw_skews, final_window = calculate_gc_skew(dna_seq, window_size=1000)
    cumulative_skews = calculate_cumulative_skew(raw_skews)

    # Find the Minimum (The Origin)
    min_skew = min(cumulative_skews)
    min_index = cumulative_skews.index(min_skew)
    predicted_loc = min_index * final_window

    print("-" * 30)
    print(f"📍 PREDICTED ORIGIN: Base Pair ~{predicted_loc}")
    print("-" * 30)

    # Plotting
    print("🎨 Generating Graph...")
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_skews, color='purple', label='Cumulative Skew')
    plt.axvline(x=min_index, color='red', linestyle='--', label='Predicted Origin')
    plt.title(f'Ori-Finder Result for {filename}')
    plt.xlabel(f'Position (x {final_window} bp)')
    plt.ylabel('Cumulative GC Skew')
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    plt.savefig("orifinder_result.png")
    print("✅ Done! Graph saved as 'orifinder_result.png'")

if __name__ == "__main__":
    main()
