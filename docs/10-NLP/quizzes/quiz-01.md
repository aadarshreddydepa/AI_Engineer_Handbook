# 📝 Module 10 · NLP — Quiz 01

[🏠 Module 10](../README.md) · [📖 Lessons](../weeks/README.md) · [✅ Answers](answers-01.md)

> **40 questions across all 15 lessons.** Aim for an explanation, not just the letter — the [answers](answers-01.md) grade reasoning. Target: **32/40** to consider the module solid.

---

## Part A · Representation (10.1–10.4)

**1.** State, in one sentence, the single problem that all of NLP is solving. Why is it hard?

**2.** What is the distributional hypothesis, and why is it the theoretical foundation of every text representation from TF-IDF to attention?

**3.** Give a sentence pair with identical bag-of-words but opposite meaning. Which two limitations of BoW does it expose?

**4.** Derive TF-IDF. Explain specifically why the IDF term uses a logarithm — what breaks without it?

**5.** Why must a TF-IDF vectorizer be fit on training data only? What kind of leakage does fitting on test cause?

**6.** Explain why one-hot and bag-of-words representations are "meaning-blind." What single property do embeddings add that fixes this?

**7.** Describe Word2Vec's "fake task." What do you keep, what do you throw away, and why does the result encode meaning?

**8.** What does negative sampling replace, and why was it necessary to make Word2Vec trainable at scale?

**9.** Why do we use cosine similarity rather than Euclidean distance for embeddings?

**10.** What is the fundamental limitation of static embeddings (Word2Vec/GloVe), and which later mechanism resolves it?

**11.** Where does bias in word embeddings come from, and why can't you remove it just by cleaning the data?

---

## Part B · Sequence & attention (10.5–10.8)

**12.** Why is word order "signal"? Give a concrete example where a bag-of-words model necessarily fails and a sequence model can succeed.

**13.** Explain how the vanishing gradient manifests as a *linguistic* failure in a vanilla RNN. Name two specific NLP phenomena it breaks.

**14.** How does an LSTM's cell state preserve long-range gradients? Relate it to residual connections.

**15.** When is a bidirectional model appropriate, and when is it forbidden? Why?

**16.** Describe the seq2seq information bottleneck. Why does performance collapse on long inputs?

**17.** ⭐ Write the scaled dot-product attention formula. Explain what each of Q, K, and V represents, and why Key and Value are kept separate.

**18.** ⭐ Why is the attention score divided by √dₖ? What specifically fails without it?

**19.** What is a contextual embedding, and how does self-attention produce one? Why couldn't Word2Vec?

**20.** Explain multi-head attention. Why use several heads instead of one larger attention?

**21.** Compare attention and an RNN on (a) path length between two tokens and (b) parallelizability. What does attention pay for these advantages?

**22.** What is teacher forcing, and what problem (name it) does it create at inference time?

**23.** Why is beam search a poor choice for open-ended text generation, and what's used instead?

**24.** Trace the lineage from RNN seq2seq to the Transformer. What did each step fix, and what did the Transformer remove?

---

## Part C · Tasks, evaluation, data (10.6, 10.9, 10.10)

**25.** Name the four NLP I/O shapes. For each, give a task, the head, and the metric.

**26.** Why does NER often add a CRF layer on top of a BiLSTM? What goes wrong without it?

**27.** Explain bi-encoders vs cross-encoders. Why does production retrieval use both?

**28.** What does BLEU measure, and what does ROUGE measure? Why is one precision-oriented and the other recall-oriented?

**29.** What is perplexity, and how does it relate to cross-entropy loss? What does a perplexity of 20 mean intuitively?

**30.** Give a concrete example where BLEU misjudges a translation in both directions (good translation, low BLEU; bad translation, high BLEU).

**31.** What is inter-annotator agreement, and why does it bound the achievable accuracy of a model? A model reports 90% accuracy on a task where two annotators agree 65% of the time — what's your reaction?

**32.** Name three NLP-specific forms of data leakage and how to prevent each.

---

## Part D · Engineering & ethics (10.11–10.14)

**33.** What does the NLP front end add to the standard PyTorch training loop? Which parts of the loop itself change?

**34.** Why must the vocabulary be built on training data only, and why are `<pad>` and `<unk>` tokens non-negotiable?

**35.** How do you prevent padding from corrupting a model? Give the mechanism for an RNN, for attention, and for a tagging loss.

**36.** What is subword tokenization, and what specific problem does it solve? Why must you use the exact tokenizer a model was trained with?

**37.** What is fine-tuning, and why does it beat training from scratch when labels are limited?

**38.** What is train/serve skew in NLP, why is it so common, and how do you prevent it?

**39.** Why is the biggest NLP latency win usually a smaller model, and what is the single highest-leverage optimization in semantic search?

**40.** Explain why hallucination is *structural* in language models. Name two mitigations.

---

## 🎁 Bonus (harder)

**B1.** You have written scaled dot-product attention in NumPy and rebuilt it in PyTorch with the same weights and input. What single assertion proves your implementation is correct, and why is building it by hand the point of the whole module?

**B2.** A sentiment model does well in offline eval but poorly in production on the *same* domain. You confirm the model weights are fine. Name the two most likely one-line causes.

**B3.** Explain why "we only shipped the model, not the training data" is false comfort from a privacy standpoint. What two attacks make it false?

---

[✅ Check your answers →](answers-01.md) · [🧠 Flashcards](../flashcards/deck.md) · [📄 Cheat sheet](../cheat-sheets/nlp-cheatsheet.md)
