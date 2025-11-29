# This script generates a synthetic DNA file to test the Ori-Finder tool.
# It creates a file with a perfect "V" shape GC skew.

def create_dummy_data():
    filename = "test_genome.fasta"
    print("🧪 Generating synthetic test data...")
    
    # 1. Create a "Down" slope (Rich in Cytosine 'C')
    part1 = "C" * 40000 + "A" * 10000 

    # 2. Create an "Up" slope (Rich in Guanine 'G')
    part2 = "G" * 40000 + "T" * 10000

    full_genome = part1 + part2

    with open(filename, "w") as f:
        f.write(">Synthetic_Test_Bacteria_Genome\n")
        f.write(full_genome)

    print(f"✅ Created '{filename}' with {len(full_genome)} base pairs.")
    print("👉 # This script generates a synthetic DNA file to test the Ori-Finder tool.
# It creates a file with a perfect "V" shape GC skew.

if __name__ == "__main__":
    create_dummy_data()
