import fasttext

model = fasttext.load_model('/workspace/datasets/fasttext/title_model_final.bin')

with open("/workspace/datasets/fasttext/top_words.txt", "r") as top_words, open("/workspace/datasets/fasttext/synonyms.csv", "w") as synonyms_output:
    for word in top_words:
        word = word.strip()
        nearest_neighbors = model.get_nearest_neighbors(word)
        synonyms = [w for (sim, w) in nearest_neighbors if sim >= 0.75]
        if len(synonyms) > 0:
            synonyms_output.write(f"{word},{','.join(synonyms)}\n")
