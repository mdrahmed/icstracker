import os
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from time import time

def get_word_frequencies(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([text])
    # Get feature names (words)
    feature_names = vectorizer.get_feature_names_out()
    # Get word frequencies
    word_frequencies = zip(feature_names, vectors.sum(axis=0).A1)
    # Sort by frequency in descending order
    sorted_word_frequencies = sorted(word_frequencies, key=lambda x: x[1], reverse=True)

    return sorted_word_frequencies

if __name__ == "__main__":
    runtime_start_ms = time()
    parser = argparse.ArgumentParser()
    # specifying input dir to following
    #parser.add_argument("--input_dir", type=str, default="../step2/")
    parser.add_argument("--input_dir", type=str, default="../step_1_2/step2-extracted_common_part_retrieval/")
    parser.add_argument("--fname", type=str, required=True)
    parser.add_argument("--freq_to_remove", type=str, required=True)
    args = parser.parse_args()

    #input_file= 'uniqueVariantTraces_1000_256_1_10_100'
    input_file = os.path.join(args.input_dir, args.fname)
    if not input_file:
        print(f"File not found\n")
    word_frequencies = get_word_frequencies(input_file)
    if not os.path.isdir("./frequent_traces_removed"):
        os.mkdir("./frequent_traces_removed")
    fout_path = "./frequent_traces_removed"

    # create the output name to mostFrequentFunctions
    last_part = input_file.split('Traces')[-1]
    fout_name = f"mostFrequentFunctions" 
    fout_file = os.path.join(fout_path, fout_name)
    with open(fout_file, "w")as fout:
        # Print word frequencies from highest to lowest
        for word, frequency in word_frequencies:
            fout.write(f'{word}: {frequency}\n')
        print(f"Total frequency written to file: {fout_path}/{fout_name}")
    
    freq = args.freq_to_remove
    # removing words has frequency greater than 0.05
    filtered_words = {word for word, frequency in word_frequencies if frequency > float(freq)}
    print(f"Filtered word set to remove: {filtered_words}")
    if not os.path.isdir("idf_traces"):
        os.mkdir("./idf_traces")
    idfTrace_dir = "./idf_traces"  
    idfTrace_name = f"idf_traces_{freq}"
    idfTrace_file = os.path.join(idfTrace_dir, idfTrace_name)

    with open(input_file, "r") as fin, open(idfTrace_file, "w") as fout:
        for line in fin:
            if line.strip().lower() not in filtered_words: 
                fout.write(line)
        print(f"Functions removed based on frequency. It is removed if greater than {freq}")
    
    runtime_stop_ms = time()
    print("Step 3-Process time:",(runtime_stop_ms-runtime_start_ms)*1000,"ms")


