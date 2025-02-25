import numpy as np 
import os 

def generate_seq(num_seq=10,seq_len=10**6,output_dir="dataset"):
    os.makedirs(output_dir,exist_ok=True)

    sequences=[]
    
    seq1=np.sort(np.random.rand(seq_len))
    seq2=np.sort(np.random.rand(seq_len))[::-1]

    sequences.append(seq1),sequences.append(seq2)

    for i in range(8):
        seq=np.random.rand(seq_len)
        sequences.append(seq)

    for i,seq in enumerate(sequences):
        file_path=os.path.join(output_dir,f"seq_{i}.txt")
        np.savetxt(file_path,seq,fmt="%.6f")
        print(f"save {file_path}")


if __name__ == "__main__":
    generate_seq()

