# Authorship Attribution in the Era of LLMs: Problems, Methodologies, and Challenges

## Overview
This repository hosts the paper list from the paper "Authorship Attribution in the Era of LLMs: Problems, Methodologies, and Challenges." *ACM SIGKDD Exploration* (2024) [[arXiv]](https://arxiv.org/abs/2408.08946) [[Project Website]](https://llm-authorship.github.io)

TLDR: This survey paper systematically categorizes authorship attribution in the era of LLMs into four problems: attributing unknown texts to human authors, detecting LLM-generated texts, identifying specific LLMs or human authors, and classifying texts as human-authored, machine-generated, or co-authored by both, while also highlighting key challenges and open problems.


As illustrated in figure below, authorship attribution can be systematically categorized into four problems. Each task presents unique challenges that necessitate corresponding solutions. Researchers continually adapt and refine attribution methods, transitioning from human-authored texts to
LLM-generated content, and navigating the complex interweaving in human-LLM co-authored works.
<img src="https://github.com/authorship-attribution-llm/authorship-llm-survey/blob/main/authorship_intro.png" width=80%>


## BibTex
```
@article{huang2024authorshipattributionerallms,
    title   = {Authorship Attribution in the Era of LLMs: Problems, Methodologies, and Challenges},
    author  = {Baixiang Huang and Canyu Chen and Kai Shu},
    year    = {2024},
    journal = {arXiv preprint arXiv: 2408.08946},
    url     = {https://arxiv.org/abs/2408.08946}, 
}
```

## Table of Content
- [Overview](#overview)
- [Benchmarks and Detectors](#benchmarks-and-detectors)
- [Paper List](#paper-list)
  - [1. Human-written Text Attribution](#1-human-written-text-attribution)
  - [2. LLM-generated Text Detection](#2-llm-generated-text-detection)
  - [3. LLM-generated Text Attribution](#3-llm-generated-text-attribution)
  - [4. Human-LLM Co-authored Text Attribution](#4-human-llm-co-authored-text-attribution)

- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Benchmarks and Detectors
The table below is a summary of Authorship Attribution Datasets and Benchmarks with LLM-Generated Text. Size is shown as the sum of LLM-generated and human-written texts (with the percentage of human-written texts in parentheses). Language is displayed using the two-letter ISO 639 abbreviation. Columns P2, P3, and P4 indicate whether the dataset supports problems described in Problem 2, 3, and 4, respectively.
| Name             | Domain                                                                                  | Size               | Length                                | Language                                   | Model                                                                                | P2  | P3  | P4  |
| :--------------- | :-------------------------------------------------------------------------------------- | :----------------- | :------------------------------------ | :----------------------------------------- | :----------------------------------------------------------------------------------- | :-: | :-: | :-: |
| [TuringBench](https://arxiv.org/pdf/2109.13296)      | News                                                                                    | 168,612 (5\.2%)    | 100 to 400 words                      | en                                         | GPT-1,2,3, GROVER, CTRL, XLM, XLNET, FAIR, TRANSFORMER-XL, PPLM                      | ✓   | ✓   |     |
| [TweepFake](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0251415)        | Social media                                                                            | 25,572 (50\.0%)    | less than 280 characters              | en                                         | GPT-2, RNN, Markov, LSTM, CharRNN                                                    | ✓   |     |     |
| [ArguGPT](https://arxiv.org/abs/2304.07666)          | Academic essays                                                                         | 8,153 (49\.5%)     | 300 words on average                  | en                                         | GPT2-Xl, text-babbage-001, text-curie-001, davinci-001,002,003, GPT-3\.5-Turbo       | ✓   |     |     |
| [AuTexTification](https://arxiv.org/abs/2309.11285)  | Tweets, reviews, news, legal, and how-to articles                                       | 163,306 (42\.5%)   | 20 to 100 tokens                      | en, es                                     | BLOOM, GPT-3                                                                         | ✓   | ✓   |     |
| [CHEAT](https://arxiv.org/pdf/2304.12008)            | Academic paper abstracts                                                                | 50,699 (30\.4%)    | 163\.9 words on average               | en                                         | ChatGPT                                                                              | ✓   |     |     |
| [GPABench2](https://arxiv.org/abs/2306.05524)        | Academic paper abstracts                                                                | 2\.385M (6.3%)     | 70 to 350 words                       | en                                         | ChatGPT                                                                              | ✓   |     | ✓   |
| [Ghostbuster](https://arxiv.org/pdf/2305.15047)      | News, student essays, creative writing                                                  | 23,091 (87\.0%)    | 77 to 559 (median words per document) | en                                         | ChatGPT, Claude                                                                      | ✓   |     |     |
| [HC3](https://arxiv.org/abs/2301.07597)              | Reddit, Wikipedia, medicine, finance                                                    | 125,230 (64\.5%)   | 25 to 254 words                       | en, zh                                     | ChatGPT                                                                              | ✓   |     |     |
| [HC3 Plus](https://arxiv.org/abs/2309.02731)         | News, social media                                                                      | 214,498            | N/A                                   | en, zh                                     | ChatGPT                                                                              | ✓   |     |     |
| [HC-Var](https://arxiv.org/pdf/2310.01307)           | News, reviews, essays, QA                                                               | 144k (68\.8%)      | 50 to 200 words                       | en                                         | ChatGPT                                                                              | ✓   |     |     |
| [HANSEN](https://arxiv.org/abs/2310.16746)           | Transcripts of speech (spoken text), statements (written text)                          | 535k (96\.1%)      | less than 1k tokens                   | en                                         | ChatGPT, PaLM2, Vicuna-13B                                                           | ✓   | ✓   |     |
| [M4](https://arxiv.org/pdf/2305.14902)               | Wikipedia, WikiHow, Reddit, QA, news, paper abstracts, peer reviews                     | 147,895 (24\.2%)   | more than 1k characters               | ar, bg, en, id, ru, ur, zh                 | davinci-003, ChatGPT, GPT-4, Cohere, Dolly2, BLOOMz                                  | ✓   |     |     |
| [MGTBench](https://arxiv.org/pdf/2303.14822)         | News, student essays, creative writing                                                  | 21k (14\.3%)       | 1 to 500 words                        | en                                         | ChatGPT, ChatGLM, Dolly, GPT4All, StableLM, Claude                                   | ✓   | ✓   |     |
| [MULTITuDE](https://arxiv.org/pdf/2310.13606)        | News                                                                                    | 74,081 (10\.8%)    | 200 to 512 tokens                     | ar, ca, cs, de, en, es, nl, pt, ru, uk, zh | GPT-3,4, ChatGPT, Llama-65B, Alpaca-LoRa-30B, Vicuna-13B, OPT-66B, OPT-IML-Max-1\.3B | ✓   |     |     |
| [OpenGPTText](https://arxiv.org/pdf/2305.07969)      | OpenWebText                                                                             | 58,790 (50\.0%)    | less than 2k words                    | en                                         | ChatGPT                                                                              | ✓   |     |     |
| [OpenLLMText](https://arxiv.org/abs/2311.08723)      | OpenWebText                                                                             | 344,530 (20%)      | 512 tokens                            | en                                         | ChatGPT, PaLM, Llama, GPT2-XL                                                        | ✓   | ✓   |     |
| [Scientic Paper](https://aclanthology.org/2023.trustnlp-1.17/)   | Scientific papers                                                                       | 29k (55\.2%)       | 900 tokens on average                 | en                                         | SCIgen, GPT-2,3, ChatGPT, Galactica                                                  | ✓   |     |     |
| [RAID](https://arxiv.org/abs/2405.07940)             | News, Wikipedia, paper abstracts, recipes, Reddit, poems, book summaries, movie reviews | 523,985 (2\.9%)    | 323 tokens on average                 | cs, de, en                                 | GPT-2,3,4, ChatGPT, Mistral-7B, MPT-30B, Llama2-70B, Cohere command and chat         | ✓   |     |     |
| [M4GT-Bench](https://arxiv.org/abs/2402.11175)       | Wikipedia, Wikihow, Reddit, arXiv abstracts, academic paper reviews, student essays     | 5,368,998 (96\.6%) | more than 50 characters               | ar, bg, de, en, id, it, ru, ur, zh         | ChatGPT, davinci-003, GPT-4, Cohere, Dolly-v2, BLOOMz                                | ✓   | ✓   | ✓   |
| [MAGE](https://arxiv.org/abs/2305.13242)             | Reddit, reviews, news, QA, story writing, Wikipedia, academic paper abstracts           | 448,459 (34\.4%)   | 263 words on average                  | en                                         | GPT, Llama, GLM-130B, FLAN-T5 OPT, T0, BLOOM-7B1, GPT-J-6B, GPT-NeoX-2               | ✓   |     |     |
| [MIXSET](https://aclanthology.org/2024.findings-naacl.29/)           | Email, news, game reviews, academic paper abstracts, speeches, blogs                    | 3\.6k (16.7%)      | 50 to 250 words                       | en                                         | GPT-4, Llama2                                                                        | ✓   |     | ✓   |




The Table below present an overview of LLM-Generated Text Detectors.
| Detector               | Price                                                 | API | Website                                                             |
| :--------------------- | :---------------------------------------------------- | :-- | :------------------------------------------------------------------ |
| GPTZero                | 150k words at $10/month, 10k words for free per month | Yes | https://gptzero.me/                                                 |
| ZeroGPT                | 100k characters for $9\.99, 15k characters for free   | Yes | https://www.zerogpt.com/                                            |
| Sapling                | 50k characters for $25, 2k characters for free        | Yes | https://sapling.ai/ai-content-detector                              |
| Originality.AI         | 200k words at $14\.95/month                           | Yes | https://originality.ai/                                             |
| CopyLeaks              | 300k words at $7\.99/month                            | Yes | https://copyleaks.com/ai-content-detector                           |
| Winston                | 80k words at $12/month                                | Yes | https://gowinston.ai/                                               |
| GPT Radar              | $0\.02/100 tokens                                     | N/A | https://gptradar.com/                                               |
| Turnitin’s AI detector | License  required                                     | N/A | https://www.turnitin.com/solutions/topics/ai-writing/ai-detector/   |
| GPT-2 Output Detector  | Free                                                  | N/A | https://github.com/openai/gpt-2-output-dataset/tree/master/detector |
| Crossplag              | Free                                                  | N/A | https://crossplag.com/ai-content-detector/                          |
| CatchGPT               | Free                                                  | N/A | https://www.catchgpt.ai/                                            |
| Quil.org               | Free                                                  | N/A | https://aiwritingcheck.org/                                         |
| Scribbr                | Free                                                  | N/A | https://www.scribbr.com/ai-detector/                                |
| Draft Goal             | Free                                                  | N/A | https://detector.dng.ai/                                            |
| Writefull              | Free                                                  | Yes | https://x.writefull.com/gpt-detector                                |
| Phrasly                | Free                                                  | Yes | https://phrasly.ai/ai-detector                                      |
| Writer                 | Free                                                  | Yes | https://writer.com/ai-content-detector/                             |


## Paper List

### 1. Human-written Text Attribution
- **Who could be behind QAnon? Authorship attribution with supervised machine-learning.** Florian Cafiero, and Jean-Baptiste Camps. *arXiv preprint arXiv:2303.02078* (2023) [[link]](https://arxiv.org/pdf/2303.02078)

- **PART: Pre-trained Authorship Representation Transformer.** Javier Huertas-Tato, Alvaro Huertas-Garcia, Alejandro Martin, and David Camacho. *arXiv preprint arXiv:2209.15373* (2022) [[link]](https://arxiv.org/pdf/2209.15373)
- **Tracing text provenance via context-aware lexical substitution.** Xi Yang, Jie Zhang, Kejiang Chen, Weiming Zhang, Zehua Ma, Feng Wang, and Nenghai Yu. *Proceedings of the AAAI Conference on Artificial Intelligence* (2022) [[link]](https://ojs.aaai.org/index.php/AAAI/article/view/21415)
- **A Survey on Authorship Analysis Tasks and Techniques.** Arta Misini, Arbana Kadriu, and Ercan Canhasi. *SEEU Review* (2022) [[link]](https://sciendo.com/pdf/10.2478/seeur-2022-0100)
- **On the state of the art in authorship attribution and authorship verification.** Jacob Tyo, Bhuwan Dhingra, and Zachary C Lipton. *arXiv preprint arXiv:2209.06869* (2022) [[link]](https://arxiv.org/abs/2209.06869)
- **Overview of PAN 2022: Authorship Verification, Profiling Irony and Stereotype Spreaders, and Style Change Detection.** Janek Bevendorff, Berta Chulvi, Elisabetta Fersini, Annina Heini, Mike Kestemont, Krzysztof Kredens, Maximilian Mayerl, Reynier Ortega-Bueno, Piotr Pęzik, Martin Potthast, and others. *International Conference of the Cross-Language Evaluation Forum for European Languages* (2022) [[link]](https://dbis.uibk.ac.at/sites/default/files/2022-09/bevendorff-clef-2022.pdf)
- **Same author or just same topic? towards content-independent style representations.** Anna Wegmann, Marijn Schraagen, and Dong Nguyen. *arXiv preprint arXiv:2204.04907* (2022) [[link]](https://arxiv.org/pdf/2204.04907)
- **Adversarial Authorship Attribution for Deobfuscation.** Wanyue Zhai, Jonathan Rusert, Zubair Shafiq, and Padmini Srinivasan. *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)* (2022) [[link]](https://aclanthology.org/2022.acl-long.509.pdf)
- **Creating and detecting fake reviews of online products.** Joni Salminen, Chandrashekhar Kandpal, Ahmed Mohamed Kamel, Soon-gyo Jung, and Bernard J Jansen. *Journal of Retailing and Consumer Services* (2022) [[link]](https://www.sciencedirect.com/science/article/pii/S0969698921003374)
- **Unified and multilingual author profiling for detecting haters.** Ipek Baris Schlicht, and Angel Felipe Magnossão de Paula. *arXiv preprint arXiv:2109.09233* (2021) [[link]](https://arxiv.org/pdf/2109.09233)
- **Performing multilingual analysis with Linguistic Inquiry and Word Count 2015 (LIWC2015). An equivalence study of four languages.** Diana Paula Dudău, and Florin Alin Sava. *Frontiers in Psychology* (2021) [[link]](https://www.frontiersin.org/articles/10.3389/fpsyg.2021.570568/pdf)
- **The topic confusion task: A novel evaluation scenario for authorship attribution.** Malik Altakrori, Jackie Chi Kit Cheung, and Benjamin CM Fung. *Findings of the Association for Computational Linguistics: EMNLP 2021* (2021) [[link]](https://aclanthology.org/2021.findings-emnlp.359.pdf)
- **Learning universal authorship representations.** Rafael A Rivera-Soto, Olivia Elizabeth Miano, Juanita Ordonez, Barry Y Chen, Aleem Khan, Marcus Bishop, and Nicholas Andrews. *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing* (2021) [[link]](https://aclanthology.org/2021.emnlp-main.70.pdf)
- **Posnoise: An effective countermeasure against topic biases in authorship analysis.** Oren Halvani, and Lukas Graner. *Proceedings of the 16th International Conference on Availability, Reliability and Security* (2021) [[link]](https://arxiv.org/pdf/2005.06605)

- **Overview of the Cross-Domain Authorship Verification Task at PAN 2021..** Mike Kestemont, Enrique Manjavacas, Ilia Markov, Janek Bevendorff, Matti Wiegmann, Efstathios Stamatatos, Martin Potthast, and Benno Stein. *CLEF (Working Notes)* (2021) [[link]](https://repository.uantwerpen.be/docstore/d:irua:3751)
- **Authorship attribution of social media messages.** Antonio Theophilo, Romain Giot, and Anderson Rocha. *IEEE Transactions on Computational Social Systems* (2021) [[link]](https://drive.google.com/file/d/1PQB3eNg_dWyZppF3Z7YG0NvRmwL0rAmI/view)
- **Siamese networks for large-scale author identification.** Chakaveh Saedi, and Mark Dras. *Computer Speech \& Language* (2021) [[link]](https://arxiv.org/pdf/1912.10616)

- **Developing a benchmark for reducing data bias in authorship attribution.** Benjamin Murauer, and Günther Specht. *Proceedings of the 2nd Workshop on Evaluation and Comparison of NLP Systems* (2021) [[link]](https://aclanthology.org/2021.eval4nlp-1.18.pdf)
- **Transferring bert-like transformers’ knowledge for authorship verification.** Andrei Manolache, Florin Brad, Elena Burceanu, Antonio Barbalau, Radu Ionescu, and Marius Popescu. *arXiv preprint arXiv:2112.05125* (2021) [[link]](https://www.researchgate.net/profile/Andrei-Manolache-2/publication/356919724_Transferring_BERT-like_Transformers'_Knowledge_for_Authorship_Verification/links/61b75b71a6251b553ab64f4e/Transferring-BERT-like-Transformers-Knowledge-for-Authorship-Verification.pdf)
- **The importance of suppressing domain style in authorship analysis.** Sebastian Bischoff, Niklas Deckers, Marcel Schliebs, Ben Thies, Matthias Hagen, Efstathios Stamatatos, Benno Stein, and Martin Potthast. *arXiv preprint arXiv:2005.14714* (2020) [[link]](https://arxiv.org/pdf/2005.14714)

- **The importance of suppressing domain style in authorship analysis.** Sebastian Bischoff, Niklas Deckers, Marcel Schliebs, Ben Thies, Matthias Hagen, Efstathios Stamatatos, Benno Stein, and Martin Potthast. *arXiv preprint arXiv:2005.14714* (2020) [[link]](https://arxiv.org/pdf/2005.14714)
- **Overview of pan 2020: Authorship verification, celebrity profiling, profiling fake news spreaders on twitter, and style change detection.** Janek Bevendorff, Bilal Ghanem, Anastasia Giachanou, Mike Kestemont, Enrique Manjavacas, Ilia Markov, Maximilian Mayerl, Martin Potthast, Francisco Rangel, Paolo Rosso, and others. *Experimental IR Meets Multilinguality, Multimodality, and Interaction: 11th International Conference of the CLEF Association, CLEF 2020, Thessaloniki, Greece, September 22--25, 2020, Proceedings 11* (2020) [[link]](https://riunet.upv.es/bitstream/handle/10251/179208/BevendorffGhanemGiachanou%20-%20Overview%20of%20PAN%202020%20Authorship%20Verification%20Celebrity%20Profiling%20Prof....pdf?sequence=1)
- **Forensic authorship analysis of microblogging texts using n-grams and stylometric features.** Nicole Mariah Sharon Belvisi, Naveed Muhammad, and Fernando Alonso-Fernandez. *2020 8th International Workshop on Biometrics and Forensics (IWBF)* (2020) [[link]](https://arxiv.org/pdf/2003.11545)
- **Masking domain-specific information for cross-domain deception detection.** Javier Sánchez-Junquera, Luis Villaseñor-Pineda, Manuel Montes-y-Gómez, Paolo Rosso, and Efstathios Stamatatos. *Pattern Recognition Letters* (2020) [[link]](https://riunet.upv.es/bitstream/handle/10251/176093/Sanchez-JunqueraVillasenor-PinedaMontes-y-Gomez%20-%20Masking%20domain-specific%20information%20for%20cross-d....pdf?sequence=7)
- **Cross-domain authorship attribution using pre-trained language models.** Georgios Barlas, and Efstathios Stamatatos. *Artificial Intelligence Applications and Innovations: 16th IFIP WG 12.5 International Conference, AIAI 2020, Neos Marmaras, Greece, June 5--7, 2020, Proceedings, Part I 16* (2020) [[link]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7256385/)
- **Deep Learning based Authorship Identification.** Arth Talati, A Sharma, and R Narayanan. *No venue* (2020) [[link]](https://www.researchgate.net/profile/Ranjani-Narayanan/publication/343848444_Deep_Learning_based_Authorship_Identification/links/5f447d0b458515b7294e1734/Deep-Learning-based-Authorship-Identification.pdf)
- **BertAA: BERT fine-tuning for Authorship Attribution.** Maél Fabien, Esaú Villatoro-Tello, Petr Motlicek, and Shantipriya Parida. *Proceedings of the 17th International Conference on Natural Language Processing (ICON)* (2020) [[link]](https://aclanthology.org/2020.icon-main.16.pdf)
- **Cross-domain authorship attribution using pre-trained language models.** Georgios Barlas, and Efstathios Stamatatos. *Artificial Intelligence Applications and Innovations: 16th IFIP WG 12.5 International Conference, AIAI 2020, Neos Marmaras, Greece, June 5--7, 2020, Proceedings, Part I 16* (2020) [[link]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7256385/)

- **Text messaging forensics: Txt 4n6: idiolect-free authorship analysis?.** Tim Grant. *The Routledge handbook of forensic linguistics* (2020) [[link]](https://www.academia.edu/download/27070255/the_routledge_handbook_of_forensic_linguistics_2010.pdf#page=537)
- **Exclusive: FBI document warns conspiracy theories are a new domestic terrorism threat.** Jana Winter. *Yahoo News* (2019) [[link]](No link found)
- **Paraphrase plagiarism identification with character-level features.** Fernando Sánchez-Vega, Esaú Villatoro-Tello, Manuel Montes-y-Gómez, Paolo Rosso, Efstathios Stamatatos, and Luis Villasenor-Pineda. *Pattern Analysis and Applications* (2019) [[link]](https://riunet.upv.es/bitstream/handle/10251/159992/S%C3%A1nchez-Vega%3BVillatoro-Tello%3BMontes-y-G%C3%B3mez%20-%20Paraphrase%20Plagiarism%20Identifcation%20with%20Character-....pdf?sequence=5)
- **A Girl Has No Name: Automated Authorship Obfuscation using Mutant-X..** Asad Mahmood, Faizan Ahmad, Zubair Shafiq, Padmini Srinivasan, and Fareed Zaffar. *Proc. Priv. Enhancing Technol.* (2019) [[link]](https://petsymposium.org/popets/2019/popets-2019-0058.pdf)

- **Code authorship attribution: Methods and challenges.** Vaibhavi Kalgutkar, Ratinder Kaur, Hugo Gonzalez, Natalia Stakhanova, and Alina Matyukhina. *ACM Computing Surveys (CSUR)* (2019) [[link]](https://cyberlab.usask.ca/papers/CodeAttribution-20.pdf)
- **A survey on stylometric text features.** Ksenia Lagutina, Nadezhda Lagutina, Elena Boychuk, Inna Vorontsova, Elena Shliakhtina, Olga Belyaeva, Ilya Paramonov, and PG Demidov. *2019 25th Conference of Open Innovations Association (FRUCT)* (2019) [[link]](https://www.academia.edu/download/81574987/Lag.pdf)
- **Attributing the Bixby Letter using n-gram tracing.** Jack Grieve, Isobelle Clarke, Emily Chiang, Hannah Gideon, Annina Heini, Andrea Nini, and Emily Waibel. *Digital Scholarship in the Humanities* (2019) [[link]](https://research.aston.ac.uk/files/26121655/Attributing_the_Bixby_Letter_using_n_gram_tracing.pdf)
- **Similarity learning for authorship verification in social media.** Benedikt Boenninghoff, Robert M Nickel, Steffen Zeiler, and Dorothea Kolossa. *ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)* (2019) [[link]](https://arxiv.org/pdf/1908.07844)
- **Improving author verification based on topic modeling.** Nektaria Potha, and Efstathios Stamatatos. *Journal of the Association for Information Science and Technology* (2019) [[link]](https://www.researchgate.net/profile/Nektaria-Potha/publication/331568430_Improving_author_verification_based_on_topic_modeling/links/5f0c47a792851c38a519aabd/Improving-author-verification-based-on-topic-modeling.pdf)
- **Learning invariant representations of social media users.** Nicholas Andrews, and Marcus Bishop. *arXiv preprint arXiv:1910.04979* (2019) [[link]](https://arxiv.org/pdf/1910.04979)
- **Explainable authorship verification in social media via attention-based similarity learning.** Benedikt Boenninghoff, Steffen Hessler, Dorothea Kolossa, and Robert M Nickel. *2019 IEEE International Conference on Big Data (Big Data)* (2019) [[link]](https://arxiv.org/pdf/1910.08144)

- **Classification for authorship of tweets by comparing logistic regression and naive bayes classifiers.** Opeyemi Aborisade, and Mohd Anwar. *2018 IEEE International Conference on Information Reuse and Integration (IRI)* (2018) [[link]](https://ieeexplore.ieee.org/abstract/document/8424720/)
- **What represents “style” in authorship attribution?.** Kalaivani Sundararajan, and Damon Woodard. *Proceedings of the 27th International Conference on Computational Linguistics* (2018) [[link]](https://aclanthology.org/C18-1238.pdf)
- **Masking topic-related information to enhance authorship attribution.** Efstathios Stamatatos. *Journal of the Association for Information Science and technology* (2018) [[link]](https://icsdweb.aegean.gr/stamatatos/papers/jasist-2018-preprint.pdf)
- **Bert: Pre-training of deep bidirectional transformers for language understanding.** Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. *arXiv preprint arXiv:1810.04805* (2018) [[link]](https://arxiv.org/pdf/1810.04805.pdf&usg=ALkJrhhzxlCL6yTht2BRmH9atgvKFxHsxQ%EF%BB%BF)
- **An investigation of supervised learning methods for authorship attribution in short hinglish texts using char \& word n-grams.** Abhay Sharma, Ananya Nandan, and Reetika Ralhan. *arXiv preprint arXiv:1812.10281* (2018) [[link]](https://arxiv.org/pdf/1812.10281)
- **Syntax encoding with application in authorship attribution.** Richong Zhang, Zhiyuan Hu, Hongyu Guo, and Yongyi Mao. *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing* (2018) [[link]](https://aclanthology.org/D18-1294.pdf)
- **Universal language model fine-tuning for text classification.** Jeremy Howard, and Sebastian Ruder. *arXiv preprint arXiv:1801.06146* (2018) [[link]](https://aclanthology.org/P18-1031.pdf)
- **Topic or style? exploring the most useful features for authorship attribution.** Yunita Sari, Mark Stevenson, and Andreas Vlachos. *Proceedings of the 27th international conference on computational linguistics* (2018) [[link]](https://aclanthology.org/C18-1029.pdf)

- **Computational forensic authorship analysis: Promises and pitfalls.** Shlomo Argamon. *Language and Law/Linguagem e Direito* (2018) [[link]](http://aleph.letras.up.pt/index.php/LLLD/article/download/6115/5757)
- **Authorship verification applied to detection of compromised accounts on online social networks: A continuous approach.** Sylvio Barbon, Rodrigo Augusto Igawa, and Bruno Bogaz Zarpelão. *Multimedia Tools and Applications* (2017) [[link]](https://link.springer.com/article/10.1007/s11042-016-3899-8)
- **What represents “style” in authorship attribution?.** Kalaivani Sundararajan, and Damon Woodard. *Proceedings of the 27th International Conference on Computational Linguistics* (2018) [[link]](https://aclanthology.org/C18-1238.pdf)
- **Convolutional neural networks for authorship attribution of short texts.** Prasha Shrestha, Sebastian Sierra, Fabio A González, Manuel Montes, Paolo Rosso, and Thamar Solorio. *Proceedings of the 15th conference of the European chapter of the association for computational linguistics: Volume 2, short papers* (2017) [[link]](https://aclanthology.org/E17-2106.pdf)

- **Authorship verification applied to detection of compromised accounts on online social networks: A continuous approach.** Sylvio Barbon, Rodrigo Augusto Igawa, and Bruno Bogaz Zarpelão. *Multimedia Tools and Applications* (2017) [[link]](https://link.springer.com/article/10.1007/s11042-016-3899-8)
- **Convolutional neural networks for authorship attribution of short texts.** Prasha Shrestha, Sebastian Sierra, Fabio A González, Manuel Montes, Paolo Rosso, and Thamar Solorio. *Proceedings of the 15th conference of the European chapter of the association for computational linguistics: Volume 2, short papers* (2017) [[link]](https://aclanthology.org/E17-2106.pdf)
- **Deep learning based authorship identification.** Chen Qian, Tianchang He, and Rao Zhang. *Report, Stanford University* (2017) [[link]](No link found)
- **Stylometric authorship attribution of collaborative documents.** Edwin Dauber, Rebekah Overdorf, and Rachel Greenstadt. *Cyber Security Cryptography and Machine Learning: First International Conference, CSCML 2017, Beer-Sheva, Israel, June 29-30, 2017, Proceedings 1* (2017) [[link]](https://overdorf.github.io/assets/papers/17CSCML.pdf)
- **A unified approach to interpreting model predictions.** Scott M Lundberg, and Su-In Lee. *Advances in neural information processing systems* (2017) [[link]](https://proceedings.neurips.cc/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf)

- **Convolutional neural networks for authorship attribution of short texts.** Prasha Shrestha, Sebastian Sierra, Fabio A González, Manuel Montes, Paolo Rosso, and Thamar Solorio. *Proceedings of the 15th conference of the European chapter of the association for computational linguistics: Volume 2, short papers* (2017) [[link]](https://aclanthology.org/E17-2106.pdf)

- **Surveying stylometry techniques and applications.** Tempestt Neal, Kalaivani Sundararajan, Aneez Fatima, Yiming Yan, Yingfei Xiang, and Damon Woodard. *ACM Computing Surveys (CSuR)* (2017) [[link]](https://dl.acm.org/doi/abs/10.1145/3132039)
- **Authorship verification: a review of recent advances.** Efstathios Stamatatos. *Research in Computing Science* (2016) [[link]](https://rcs.cic.ipn.mx/2016_123/Authorship%20Verification_%20A%20Review%20of%20Recent%20Advances.pdf)
- **Authorship attribution for social media forensics.** Anderson Rocha, Walter J Scheirer, Christopher W Forstall, Thiago Cavalcante, Antonio Theophilo, Bingyu Shen, Ariadne RB Carvalho, and Efstathios Stamatatos. *IEEE transactions on information forensics and security* (2016) [[link]](https://ieeexplore.ieee.org/abstract/document/7555393/)
- **Domain adaptation for authorship attribution: Improved structural correspondence learning.** Upendra Sapkota, Thamar Solorio, Manuel Montes, and Steven Bethard. *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)* (2016) [[link]](https://aclanthology.org/P16-1210.pdf)
- **Character-level and multi-channel convolutional neural networks for large-scale authorship attribution.** Sebastian Ruder, Parsa Ghaffari, and John G Breslin. *arXiv preprint arXiv:1609.06686* (2016) [[link]](http://www.johnbreslin.com/files/publications/20160921_arxi2016.pdf)

- **Profile-based authorship analysis.** Jonathan Dunn, Shlomo Argamon, Amin Rasooli, and Geet Kumar. *Digital Scholarship in the Humanities* (2016) [[link]](https://www.academia.edu/download/37660622/Dunn.Profile-based_Authorship.pdf)
- **The Rowling case: a proposed standard analytic protocol for authorship questions.** Patrick Juola. *Digital Scholarship in the Humanities* (2015) [[link]](https://academic.oup.com/dsh/article-pdf/30/suppl_1/i100/1038325/fqv040.pdf)
- **The development and psychometric properties of LIWC2015.** James W Pennebaker, Ryan L Boyd, Kayla Jordan, and Kate Blackburn. *No venue* (2015) [[link]](https://repositories.lib.utexas.edu/bitstreams/b0d26dcf-2391-4701-88d0-3cf50ebee697/download)
- **Author identification using multi-headed recurrent neural networks.** Douglas Bagnall. *arXiv preprint arXiv:1506.04891* (2015) [[link]](https://arxiv.org/pdf/1506.04891)
- **Does size matter? Authorship attribution, small samples, big problem.** Maciej Eder. *Digital Scholarship in the Humanities* (2015) [[link]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=097aaf2484e5e66e6bb406c03f8af546decdeafc)

- **Authorship attribution with topic models.** Yanir Seroussi, Ingrid Zukerman, and Fabian Bohnert. *Computational Linguistics* (2014) [[link]](https://direct.mit.edu/coli/article-pdf/40/2/269/1803926/coli_a_00173.pdf)
- **Authorship attribution for forensic investigation with thousands of authors.** Min Yang, and Kam-Pui Chow. *ICT Systems Security and Privacy Protection: 29th IFIP TC 11 International Conference, SEC 2014, Marrakech, Morocco, June 2-4, 2014. Proceedings 29* (2014) [[link]](https://inria.hal.science/hal-01370381/file/978-3-642-55415-5_28_Chapter.pdf)
- **The secret life of pronouns. what our words say about us.** John Nerbonne. *Literary and Linguistic Computing* (2014) [[link]](https://academic.oup.com/dsh/article-abstract/29/1/139/948842)
- **Breaking the closed-world assumption in stylometric authorship attribution.** Ariel Stolerman, Rebekah Overdorf, Sadia Afroz, and Rachel Greenstadt. *Advances in Digital Forensics X: 10th IFIP WG 11.9 International Conference, Vienna, Austria, January 8-10, 2014, Revised Selected Papers 10* (2014) [[link]](https://inria.hal.science/hal-01393771/file/978-3-662-44952-3_13_Chapter.pdf)
- **Zipf’s word frequency law in natural language: A critical review and future directions.** Steven T Piantadosi. *Psychonomic bulletin \& review* (2014) [[link]](https://link.springer.com/article/10.3758/s13423-014-0585-6)

- **The handbook of language variation and change.** Jack K Chambers, Peter Trudgill, and Natalie Schilling-Estes. *John Wiley & Sons* (2013) [[link]](https://books.google.com/books?hl=en&lr=&id=wNhVDwAAQBAJ&oi=fnd&pg=PR15&dq=The+handbook+of+language+variation+and+change+Jack+K+Chambers,+Peter+Trudgill,+and+Natalie+Schilling-Estes&ots=xyBnEcvMIB&sig=zKCbjWQDAmJtO6icoyKi8whEnP0)
- **Automated authorship attribution using advanced signal classification techniques.** Maryam Ebrahimpour, Tālis J Putniņš, Matthew J Berryman, Andrew Allison, Brian W-H Ng, and Derek Abbott. *PloS one* (2013) [[link]](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0054998&type=printable)

- **Authorship verification for short messages using stylometry.** Marcelo Luiz Brocardo, Issa Traore, Sherif Saad, and Isaac Woungang. *2013 International Conference on Computer, Information and Telecommunication Systems (CITS)* (2013) [[link]](https://www.academia.edu/download/44592452/Authorship_verification_for_short_messag20160410-28575-2urvko.pdf)
- **Detecting hoaxes, frauds, and deception in writing style online.** Sadia Afroz, Michael Brennan, and Rachel Greenstadt. *2012 IEEE Symposium on Security and Privacy* (2012) [[link]](https://www.ieee-security.org/TC/SP2012/papers/4681a461.pdf)
- **Stylometry and immigration: A case study.** Patrick Juola. *JL \& Pol'y* (2012) [[link]](https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/jlawp21&section=19)
- **The “fundamental problem” of authorship attribution.** Moshe Koppel, Jonathan Schler, Shlomo Argamon, and Yaron Winter. *English Studies* (2012) [[link]](https://www.tandfonline.com/doi/abs/10.1080/0013838X.2012.668794)

- **Adversarial stylometry: Circumventing authorship recognition to preserve privacy and anonymity.** Michael Brennan, Sadia Afroz, and Rachel Greenstadt. *ACM Transactions on Information and System Security (TISSEC)* (2012) [[link]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=2db56e054cac99d80da9c193082a8fbc384432ad)
- **Finding deceptive opinion spam by any stretch of the imagination.** Myle Ott, Yejin Choi, Claire Cardie, and Jeffrey T Hancock. *arXiv preprint arXiv:1107.4557* (2011) [[link]](https://arxiv.org/pdf/1107.4557)
- **Ghosts from the high court's past: Evidence from computational linguistics for Dixon ghosting for Mctiernan and rich.** Yanir Seroussi, Russell Smyth, and Ingrid Zukerman. *University of New South Wales Law Journal, The* (2011) [[link]](http://users.monash.edu/~ingrid/Publications/SeroussiSmythZukerman.pdf)
- **Plagiarism and authorship analysis: introduction to the special issue.** Efstathios Stamatatos, and Moshe Koppel. *Language Resources and Evaluation* (2011) [[link]](https://www.academia.edu/download/44789886/Plagiarism_and_authorship_analysis_intro20160416-18347-1nu6uiy.pdf)
- **Domain independent authorship attribution without domain adaptation.** Rohith Menon, and Yejin Choi. *Proceedings of the International Conference Recent Advances in Natural Language Processing 2011* (2011) [[link]](https://aclanthology.org/R11-1043.pdf)

- **Person identification from text and speech genre samples.** Jade Goldstein, Ransom Winder, and Roberta Sabin. *Proceedings of the 12th Conference of the European Chapter of the ACL (EACL 2009)* (2009) [[link]](https://aclanthology.org/E09-1039.pdf)

- **Automatically profiling the author of an anonymous text.** Shlomo Argamon, Moshe Koppel, James W Pennebaker, and Jonathan Schler. *Communications of the ACM* (2009) [[link]](https://dl.acm.org/doi/pdf/10.1145/1461928.1461959)
- **A survey of modern authorship attribution methods.** Efstathios Stamatatos. *Journal of the American Society for information Science and Technology* (2009) [[link]](https://www.cnts.ua.ac.be/~walter/educational/material/Stamatatos_survey2009.pdf)
- **Writeprints: A stylometric approach to identity-level identification and similarity detection in cyberspace.** Ahmed Abbasi, and Hsinchun Chen. *ACM Transactions on Information Systems (TOIS)* (2008) [[link]](http://ahmedabbasi.com/wp-content/uploads/J/AbbasiChen_Writeprints_ACMTOIS.pdf)
- **Authorship Attribution of E-Mail: Comparing Classifiers over a New Corpus for Evaluation..** Ben Allison, and Louise Guthrie. *LREC* (2008) [[link]](https://www.cs.brandeis.edu/~marc/misc/proceedings/lrec-2008/pdf/552_paper.pdf)
- **Author identification: Using text sampling to handle the class imbalance problem.** Efstathios Stamatatos. *Information Processing \& Management* (2008) [[link]](https://icsdweb.aegean.gr/stamatatos/papers/ipm%202008%20preprint.pdf)
- **Detecting Fake Content with Relative Entropy Scoring.** Thomas Lavergne, Tanguy Urvoy, and François Yvon. *Pan* (2008) [[link]](https://ceur-ws.org/Vol-377/paper4.pdf)

- **Quantifying evidence in forensic authorship analysis.** Tim Grant. *International Journal of Speech, Language \& the Law* (2007) [[link]](https://search.ebscohost.com/login.aspx?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=17488885&AN=28749573&h=GGDwBC6v7aN3hT6g0jRL4oihnqnUbG2wvHl6vhhXWEQwnxA%2FQISb4pXr%2Fzf%2Flsf9EF2tRaC2W47kDZ71JHvCfg%3D%3D&crl=c)
- **Authorship attribution in law enforcement scenarios.** Moshe Koppel, Jonathan Schler, and Eran Messeri. *NATO Security Through Science Series D-Information and Communication Security* (2008) [[link]](https://u.cs.biu.ac.il/~koppel/papers/authorship-NATO-bookchapter-final_2_.pdf)
- **Opinion spam and analysis.** Nitin Jindal, and Bing Liu. *Proceedings of the 2008 international conference on web search and data mining* (2008) [[link]](https://www.researchgate.net/profile/Bing-Liu-120/publication/200044297_Opinion_Spam_and_Analysis/links/5472bbfd0cf216f8cfae8836/Opinion-Spam-and-Analysis.pdf)
- **Plagiarism detection without reference collections.** Sven Meyer zu Eissen, Benno Stein, and Marion Kulig. *Advances in Data Analysis: Proceedings of the 30 th Annual Conference of the Gesellschaft für Klassifikation eV, Freie Universität Berlin, March 8--10, 2006* (2007) [[link]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=20163f0e34cbf6405033fe258de095dcbdff4db4)
- **On lying and being lied to: A linguistic analysis of deception in computer-mediated communication.** Jeffrey T Hancock, Lauren E Curry, Saurabh Goorha, and Michael Woodworth. *Discourse Processes* (2007) [[link]](https://socialmedialab.sites.stanford.edu/sites/g/files/sbiybj22976/files/media/file/hancock-dp-on-lying.pdf)
- **Measuring Differentiability: Unmasking Pseudonymous Authors..** Moshe Koppel, Jonathan Schler, and Elisheva Bonchek-Dokow. *Journal of Machine Learning Research* (2007) [[link]](https://www.jmlr.org/papers/volume8/koppel07a/koppel07a.pdf)
- **An algorithm for identifying authors using synonyms.** Jonathan H Clark, and Charles J Hannon. *Eighth Mexican International Conference on Current Trends in Computer Science (ENC 2007)* (2007) [[link]](https://ieeexplore.ieee.org/abstract/document/4351431/)
- **Authorship attribution.** Ilker Nadi Bozkurt, Ozgur Baghoglu, and Erkan Uyar. *2007 22nd international symposium on computer and information sciences* (2007) [[link]](https://repository.bilkent.edu.tr/bitstream/handle/11693/27016/Authorship%20attribution%20Performance%20of%20various%20features%20and%20classification%20methods.pdf?sequence=1)
- **Bigrams of syntactic labels for authorship discrimination of short texts.** Graeme Hirst, and Ol’ga Feiguina. *Literary and Linguistic Computing* (2007) [[link]](ftp://ftp.sys.utoronto.ca/dist/gh/Hirst+Feiguina-2007-as-published.pdf)
- **Measuring Differentiability: Unmasking Pseudonymous Authors..** Moshe Koppel, Jonathan Schler, and Elisheva Bonchek-Dokow. *Journal of Machine Learning Research* (2007) [[link]](https://www.jmlr.org/papers/volume8/koppel07a/koppel07a.pdf)

- **A framework for authorship identification of online messages: Writing-style features and classification techniques.** Rong Zheng, Jiexun Li, Hsinchun Chen, and Zan Huang. *Journal of the American society for information science and technology* (2006) [[link]](https://www.academia.edu/download/49478125/asi.2031620161009-19274-21644z.pdf)
- **Authorship attribution with thousands of candidate authors.** Moshe Koppel, Jonathan Schler, Shlomo Argamon, and Eran Messeri. *Proceedings of the 29th annual international ACM SIGIR conference on Research and development in information retrieval* (2006) [[link]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=596e8f1e22f00671237768225250f1974162c566)

- **Effects of age and gender on blogging..** Jonathan Schler, Moshe Koppel, Shlomo Argamon, and James W Pennebaker. *AAAI spring symposium: Computational approaches to analyzing weblogs* (2006) [[link]](https://cdn.aaai.org/Symposia/Spring/2006/SS-06-03/SS06-03-039.pdf)
- **Author identification on the large scale.** David Madigan, Alexander Genkin, David D Lewis, Shlomo Argamon, Dmitriy Fradkin, and Li Ye. *Proceedings of the 2005 Meeting of the Classification Society of North America (CSNA)* (2005) [[link]](https://www.academia.edu/download/42715834/authorid-csna05.pdf)

- **Determining an author's native language by mining a text for errors.** Moshe Koppel, Jonathan Schler, and Kfir Zigdon. *Proceedings of the eleventh ACM SIGKDD international conference on Knowledge discovery in data mining* (2005) [[link]](https://u.cs.biu.ac.il/~schlerj/schler_kdd05.pdf)
- **Who’s at the keyboard? Authorship attribution in digital evidence investigations.** Carole E Chaski. *International journal of digital evidence* (2005) [[link]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=adefdb1f5cd3c734215efb11bc10aea2f7db9cd1)
- **Bayesian multinomial logistic regression for author identification.** David Madigan, Alexander Genkin, David D Lewis, and Dmitriy Fradkin. *AIP conference proceedings* (2005) [[link]](https://www.academia.edu/download/42715855/Bayesian_Multinomial_Logistic_Regression20160215-30550-tr5uoz.pdf)
- **On compression-based text classification.** Yuval Marton, Ning Wu, and Lisa Hellerstein. *Advances in Information Retrieval: 27th European Conference on IR Research, ECIR 2005, Santiago de Compostela, Spain, March 21-23, 2005. Proceedings 27* (2005) [[link]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=309520990da6455b1d0375897727162331092916)
- **Authorship verification as a one-class classification problem.** Moshe Koppel, and Jonathan Schler. *Proceedings of the twenty-first international conference on Machine learning* (2004) [[link]](https://icml.cc/Conferences/2004/proceedings/papers/415.pdf)

- **Author identification, idiolect, and linguistic uniqueness.** Malcolm Coulthard. *Applied linguistics* (2004) [[link]](https://publications.aston.ac.uk/id/eprint/1928/1/A_AppLing.art.final.doc)

- **Ad-hoc authorship attribution competition.** Patrick Juola. *Proceedings of the Joint Conference of the Association for Computers and the Humanities and the Association for Literary and Linguistic Computing* (2004) [[link]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=92292ca483b209122d614c54880ac46a3ac736a8)
- **Lying words: Predicting deception from linguistic styles.** Matthew L Newman, James W Pennebaker, Diane S Berry, and Jane M Richards. *Personality and social psychology bulletin* (2003) [[link]](http://www1.cs.columbia.edu/~julia/papers/newmanetal2003.pdf)

- **Gender, genre, and writing style in formal written texts.** Shlomo Argamon, Moshe Koppel, Jonathan Fine, and Anat Rachel Shimoni. *Text \& talk* (2003) [[link]](https://www.academia.edu/download/31542872/gendertext04.pdf)
- **Psychological aspects of natural language use: Our words, our selves.** James W Pennebaker, Matthias R Mehl, and Kate G Niederhoffer. *Annual review of psychology* (2003) [[link]](http://cognaction.org/cogs105/readings/LIWC.pdf)
- **Automatically categorizing written texts by author gender.** Moshe Koppel, Shlomo Argamon, and Anat Rachel Shimoni. *Literary and linguistic computing* (2002) [[link]](https://academic.oup.com/dsh/article-abstract/17/4/401/1019830)
- **Grammatical word class variation within the British National Corpus sampler.** Paul Rayson, Andrew Wilson, and Geoffrey Leech. *New frontiers of corpus research* (2002) [[link]](https://core.ac.uk/download/pdf/70428.pdf)

- **Machine learning in automated text categorization.** Fabrizio Sebastiani. *ACM computing surveys (CSUR)* (2002) [[link]](https://arxiv.org/pdf/cs/0110053)
- **Computer-based authorship attribution without lexical measures.** Efstathios Stamatatos, Nikos Fakotakis, and Georgios Kokkinakis. *Computers and the Humanities* (2001) [[link]](http://www.iula.upf.edu/materials/050401sanchez.pdf)

- **Mining e-mail content for author identification forensics.** Olivier De Vel, Alison Anderson, Malcolm Corney, and George Mohay. *ACM Sigmod Record* (2001) [[link]](https://eprints.qut.edu.au/8019/1/8019.pdf)
- **Support vector machines for spam categorization.** Harris Drucker, Donghui Wu, and Vladimir N Vapnik. *IEEE Transactions on Neural networks* (1999) [[link]](https://www.site.uottawa.ca/~nat/Courses/NLP-Course/itnn_1999_09_1048.pdf)

- **The state of authorship attribution studies: Some problems and solutions.** Joseph Rudman. *Computers and the Humanities* (1997) [[link]](http://staff.um.edu.mt/albert.gatt/teaching/dl/rudman97_status-of-authorship-attribution.pdf)

- **Authorship attribution.** David I Holmes. *Computers and the Humanities* (1994) [[link]](https://link.springer.com/article/10.1007/BF01830689)
- **Stylometry.** Jose Nilo G Binongo. *Notes and Queries* (1996) [[link]](https://go.gale.com/ps/i.do?id=GALE%7CA19139685&sid=googleScholar&v=2.1&it=r&linkaccess=abs&issn=00293970&p=AONE&sw=w)
- **The Federalist revisited: New directions in authorship attribution.** David I Holmes, and Richard S Forsyth. *Literary and Linguistic computing* (1995) [[link]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=4442be2cf81dde5f5ef76d0ac877de4ec4a57b46)

- **Inference in an authorship problem: A comparative study of discrimination methods applied to the authorship of the disputed Federalist Papers.** Frederick Mosteller, and David L Wallace. *Journal of the American Statistical Association* (1963) [[link]](https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500849)

- **The statistical study of literary vocabulary.** C Udny Yule. *No venue* (1944) [[link]](https://pure.mpg.de/rest/items/item_2407784/component/file_2622080/content)
- **On sentence-length as a statistical characteristic of style in prose: With application to two cases of disputed authorship.** G Udny Yule. *Biometrika* (1939) [[link]](https://pure.mpg.de/rest/items/item_2407783_2/component/file_2407782/content)
- **The characteristic curves of composition.** Thomas Corwin Mendenhall. *Science* (1887) [[link]](https://www.jstor.org/stable/pdf/1764604.pdf)



### 2. LLM-generated Text Detection
**Scalable watermarking for identifying large language model outputs.** Sumanth Dathathri, et al. *Nature 634.8035 (2024): 818-823* [[link]](https://www.nature.com/articles/s41586-024-08025-4.pdf)
- **Fighting fire with fire: can ChatGPT detect AI-generated text?** Amrita Bhattacharjee, and Huan Liu. *ACM SIGKDD Explorations Newsletter* (2024) [[link]](https://arxiv.org/pdf/2308.01284)
- **Paraphrasing evades detectors of ai-generated text, but retrieval is an effective defense.** Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, and Mohit Iyyer. *Advances in Neural Information Processing Systems* (2024) [[link]](https://proceedings.neurips.cc/paper_files/paper/2023/file/575c450013d0e99e4b0ecf82bd1afaa4-Paper-Conference.pdf)
- **Adaptive ensembles of fine-tuned transformers for llm-generated text detection.** Zhixin Lai, Xuesheng Zhang, and Suiyao Chen. *arXiv preprint arXiv:2403.13335* (2024) [[link]](https://arxiv.org/pdf/2403.13335)
- **ALISON: Fast and Effective Stylometric Authorship Obfuscation.** Eric Xing, Saranya Venkatraman, Thai Le, and Dongwon Lee. *arXiv preprint arXiv:2402.00835* (2024) [[link]](https://ojs.aaai.org/index.php/AAAI/article/download/29901/31575)
- **Authorship obfuscation in multilingual machine-generated text detection.** Dominik Macko, Robert Moro, Adaku Uchendu, Ivan Srba, Jason Samuel Lucas, Michiharu Yamashita, Nafis Irtiza Tripto, Dongwon Lee, Jakub Simko, and Maria Bielikova. *arXiv preprint arXiv:2401.07867* (2024) [[link]](https://arxiv.org/pdf/2401.07867)
- **On the detectability of chatgpt content: benchmarking, methodology, and evaluation through the lens of academic writing.** Zeyan Liu, Zijun Yao, Fengjun Li, and Bo Luo. *ACM SIGSAC Conference on Computer and Communications Security* (2024) [[link]](https://dl.acm.org/doi/pdf/10.1145/3658644.3670392)
- **Can Large Language Models Identify Authorship?.** Baixiang Huang, Canyu Chen, and Kai Shu. *arXiv preprint arXiv:2403.08213* (2024) [[link]](https://arxiv.org/abs/2403.08213)
- **RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors.** Liam Dugan, Alyssa Hwang, Filip Trhlik, Josh Magnus Ludan, Andrew Zhu, Hainiu Xu, Daphne Ippolito, and Chris Callison-Burch. *arXiv preprint arXiv:2405.07940* (2024) [[link]](https://arxiv.org/abs/2405.07940)
- **Paraphrasing evades detectors of ai-generated text, but retrieval is an effective defense.** Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, and Mohit Iyyer. *Advances in Neural Information Processing Systems* (2024) [[link]](https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html)
- **Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text.** Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein. *arXiv preprint arXiv:2401.12070* (2024) [[link]](https://arxiv.org/abs/2401.12070)
- **Red teaming language model detectors with language models.** Zhouxing Shi, Yihan Wang, Fan Yin, Xiangning Chen, Kai-Wei Chang, and Cho-Jui Hsieh. *Transactions of the Association for Computational Linguistics* (2024) [[link]](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00639/119629)
- **MAGE: Machine-generated Text Detection in the Wild.** Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang, Longyue Wang, Linyi Yang, Shuming Shi, and Yue Zhang. *arXiv preprint arXiv:2305.13242* (2024) [[link]](https://arxiv.org/abs/2305.13242)
- **Machine-made media: Monitoring the mobilization of machine-generated articles on misinformation and mainstream news websites.** Hans WA Hanley, and Zakir Durumeric. *Proceedings of the International AAAI Conference on Web and Social Media* (2024) [[link]](https://ojs.aaai.org/index.php/ICWSM/article/view/31333)
- **Few-Shot Detection of Machine-Generated Text using Style Representations.** Rafael Rivera Soto, Kailin Koch, Aleem Khan, Barry Chen, Marcus Bishop, and Nicholas Andrews. *arXiv preprint arXiv:2401.06712* (2024) [[link]](https://arxiv.org/abs/2401.06712)

- **M4: Multi-generator, multi-domain, and multi-lingual black-box machine-generated text detection.** Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Chenxi Whitehouse, Osama Mohammed Afzal, Tarek Mahmoud, Toru Sasaki, and others. *arXiv preprint arXiv:2305.14902* (2023) [[link]](https://arxiv.org/pdf/2305.14902)
- **DeepTextMark: Deep Learning based Text Watermarking for Detection of Large Language Model Generated Text.** Travis Munyer, and Xin Zhong. *arXiv preprint arXiv:2305.05773* (2023) [[link]](https://arxiv.org/pdf/2305.05773)
- **Paraphrasing evades detectors of ai-generated text, but retrieval is an effective defense.** Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, and Mohit Iyyer. *arXiv preprint arXiv:2303.13408* (2023) [[link]](https://proceedings.neurips.cc/paper_files/paper/2023/file/575c450013d0e99e4b0ecf82bd1afaa4-Paper-Conference.pdf)
- **A survey on detection of llms-generated content.** Xianjun Yang, Liangming Pan, Xuandong Zhao, Haifeng Chen, Linda Petzold, William Yang Wang, and Wei Cheng. *arXiv preprint arXiv:2310.15654* (2023) [[link]](https://arxiv.org/abs/2310.15654)
- **A survey on llm-gernerated text detection: Necessity, methods, and future directions.** Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Derek F Wong, and Lidia S Chao. *arXiv preprint arXiv:2310.14724* (2023) [[link]](https://arxiv.org/abs/2310.14724)
- **A watermark for large language models.** John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein. *International Conference on Machine Learning* (2023) [[link]](https://proceedings.mlr.press/v202/kirchenbauer23a.html)
- **Machine-generated text: A comprehensive survey of threat models and detection methods.** Evan Crothers, Nathalie Japkowicz, and Herna L Viktor. *IEEE Access* (2023) [[link]](https://ieeexplore.ieee.org/abstract/document/10177704/)
- **ArguGPT: evaluating, understanding and identifying argumentative essays generated by GPT models.** Yikang Liu, Ziyin Zhang, Wanyang Zhang, Shisen Yue, Xiaojing Zhao, Xinyuan Cheng, Yiwen Zhang, and Hai Hu. *arXiv preprint arXiv:2304.07666* (2023) [[link]](https://arxiv.org/abs/2304.07666)
- **Distinguishing Fact from Fiction: A Benchmark Dataset for Identifying Machine-Generated Scientific Papers in the LLM Era..** Edoardo Mosca, Mohamed Hesham Ibrahim Abdalla, Paolo Basso, Margherita Musumeci, and Georg Groh. *Proceedings of the 3rd Workshop on Trustworthy Natural Language Processing (TrustNLP 2023)* (2023) [[link]](https://aclanthology.org/2023.trustnlp-1.17/)
- **On the Generalization of Training-based ChatGPT Detection Methods.** Han Xu, Jie Ren, Pengfei He, Shenglai Zeng, Yingqian Cui, Amy Liu, Hui Liu, and Jiliang Tang. *No venue* (2023) [[link]](https://arxiv.org/abs/2310.01307)


- **Large language models can be used to effectively scale spear phishing campaigns.** Julian Hazell. *arXiv preprint arXiv:2305.06972* (2023) [[link]](https://newsletter.radensa.ru/wp-content/uploads/2023/09/2305.06972.pdf)
- **AI model GPT-3 (dis) informs us better than humans.** Giovanni Spitale, Nikola Biller-Andorno, and Federico Germani. *Science Advances* (2023) [[link]](https://www.science.org/doi/pdf/10.1126/sciadv.adh1850)
- **ChatGPT and a new academic reality: Artificial Intelligence-written research papers and the ethics of the large language models in scholarly publishing.** Brady D Lund, Ting Wang, Nishith Reddy Mannuru, Bing Nie, Somipam Shimray, and Ziang Wang. *Journal of the Association for Information Science and Technology* (2023) [[link]](https://arxiv.org/pdf/2303.13367)
- **Evade ChatGPT detectors via a single space.** Shuyang Cai, and Wanyun Cui. *arXiv preprint arXiv:2307.02599* (2023) [[link]](https://arxiv.org/pdf/2307.02599)
- **Do language models plagiarize?.** Jooyoung Lee, Thai Le, Jinghui Chen, and Dongwon Lee. *Proceedings of the ACM Web Conference 2023* (2023) [[link]](https://arxiv.org/pdf/2203.07618)
- **How reliable are ai-generated-text detectors? an assessment framework using evasive soft prompts.** Tharindu Kumarage, Paras Sheth, Raha Moraffah, Joshua Garland, and Huan Liu. *arXiv preprint arXiv:2310.05095* (2023) [[link]](https://arxiv.org/pdf/2310.05095)
- **Large language models can be guided to evade ai-generated text detection.** Ning Lu, Shengcai Liu, Rui He, Qi Wang, Yew-Soon Ong, and Ke Tang. *arXiv preprint arXiv:2305.10847* (2023) [[link]](https://arxiv.org/pdf/2305.10847)
- **Efficient Black-Box Adversarial Attacks on Neural Text Detectors.** Vitalii Fishchuk, and Daniel Braun. *arXiv preprint arXiv:2311.01873* (2023) [[link]](https://arxiv.org/pdf/2311.01873)
- **Detectgpt: Zero-shot machine-generated text detection using probability curvature.** Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D Manning, and Chelsea Finn. *arXiv preprint arXiv:2301.11305* (2023) [[link]](https://proceedings.mlr.press/v202/mitchell23a.html)
- **Deepfake text detection: Limitations and opportunities.** Jiameng Pu, Zain Sarwar, Sifat Muhammad Abdullah, Abdullah Rehman, Yoonjin Kim, Parantapa Bhattacharya, Mobin Javed, and Bimal Viswanath. *2023 IEEE Symposium on Security and Privacy (SP)* (2023) [[link]](https://ieeexplore.ieee.org/abstract/document/10179387/)
- **Can ai-generated text be reliably detected?.** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi. *arXiv preprint arXiv:2303.11156* (2023) [[link]](https://arxiv.org/abs/2303.11156)
- **The science of detecting llm-generated texts.** Ruixiang Tang, Yu-Neng Chuang, and Xia Hu. *arXiv preprint arXiv:2303.07205* (2023) [[link]](https://dl.acm.org/doi/abs/10.1145/3624725)
- **Generating Phishing Attacks using ChatGPT.** Sayak Saha Roy, Krishna Vamsi Naragam, and Shirin Nilizadeh. *arXiv preprint arXiv:2305.05133* (2023) [[link]](https://arxiv.org/abs/2305.05133)
- **Bot or human? detecting chatgpt imposters with a single question.** Hong Wang, Xuan Luo, Weizhi Wang, and Xifeng Yan. *arXiv preprint arXiv:2305.06424* (2023) [[link]](https://arxiv.org/abs/2305.06424)
- **Smaller Language Models are Better Black-box Machine-Generated Text Detectors.** Fatemehsadat Mireshghallah, Justus Mattern, Sicun Gao, Reza Shokri, and Taylor Berg-Kirkpatrick. *arXiv preprint arXiv:2305.09859* (2023) [[link]](https://arxiv.org/abs/2305.09859)
- **Generative Language Models and Automated Influence Operations: Emerging Threats and Potential Mitigations.** Josh A. Goldstein, Girish Sastry, Micah Musser, Renee DiResta, Matthew Gentzel, and Katerina Sedova. *arXiv* (2023) [[link]](https://arxiv.org/abs/2301.04246)
- **Neural Authorship Attribution: Stylometric Analysis on Large Language Models.** Tharindu Kumarage, and Huan Liu. *arXiv preprint arXiv:2308.07305* (2023) [[link]](https://ieeexplore.ieee.org/abstract/document/10438784/)
- **On the possibilities of ai-generated text detection.** Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, and Furong Huang. *arXiv preprint arXiv:2304.04736* (2023) [[link]](https://arxiv.org/abs/2304.04736)
- **Paraphrase detection: Human vs. machine content.** Jonas Becker, Jan Philip Wahle, Terry Ruas, and Bela Gipp. *arXiv preprint arXiv:2303.13989* (2023) [[link]](https://arxiv.org/abs/2303.13989)
- **Detectllm: Leveraging log rank information for zero-shot detection of machine-generated text.** Jinyan Su, Terry Yue Zhuo, Di Wang, and Preslav Nakov. *arXiv preprint arXiv:2306.05540* (2023) [[link]](https://arxiv.org/abs/2306.05540)
- **Gpt-who: An information density-based machine-generated text detector.** Saranya Venkatraman, Adaku Uchendu, and Dongwon Lee. *arXiv preprint arXiv:2310.06202* (2023) [[link]](https://arxiv.org/abs/2310.06202)

- **Semstamp: A semantic watermark with paraphrastic robustness for text generation.** Abe Bohan Hou, Jingyu Zhang, Tianxing He, Yichen Wang, Yung-Sung Chuang, Hongwei Wang, Lingfeng Shen, Benjamin Van Durme, Daniel Khashabi, and Yulia Tsvetkov. *arXiv preprint arXiv:2310.03991* (2023) [[link]](https://arxiv.org/abs/2310.03991)
- **Dipmark: A stealthy, efficient and resilient watermark for large language models.** Yihan Wu, Zhengmian Hu, Hongyang Zhang, and Heng Huang. *arXiv preprint arXiv:2310.07710* (2023) [[link]](https://arxiv.org/abs/2310.07710)
- **Provable robust watermarking for ai-generated text.** Xuandong Zhao, Prabhanjan Ananth, Lei Li, and Yu-Xiang Wang. *arXiv preprint arXiv:2306.17439* (2023) [[link]](https://arxiv.org/abs/2306.17439)

- **Evaluating AIGC detectors on code content.** Jian Wang, Shangqing Liu, Xiaofei Xie, and Yi Li. *arXiv preprint arXiv:2304.05193* (2023) [[link]](https://arxiv.org/pdf/2304.05193)
- **Cheat: A large-scale dataset for detecting chatgpt-written abstracts.** Peipeng Yu, Jiahan Chen, Xuan Feng, and Zhihua Xia. *arXiv preprint arXiv:2304.12008* (2023) [[link]](https://arxiv.org/pdf/2304.12008)
- **Ghostbuster: Detecting text ghostwritten by large language models.** Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan Klein. *arXiv preprint arXiv:2305.15047* (2023) [[link]](https://arxiv.org/pdf/2305.15047)
- **Gpt-sentinel: Distinguishing human and chatgpt generated content.** Yutian Chen, Hao Kang, Vivian Zhai, Liangze Li, Rita Singh, and Bhiksha Raj. *arXiv preprint arXiv:2305.07969* (2023) [[link]](https://arxiv.org/pdf/2305.07969)
- **MULTITuDE: Large-Scale Multilingual Machine-Generated Text Detection Benchmark.** Dominik Macko, Robert Moro, Adaku Uchendu, Jason Samuel Lucas, Michiharu Yamashita, Matúš Pikuliak, Ivan Srba, Thai Le, Dongwon Lee, Jakub Simko, and others. *arXiv preprint arXiv:2310.13606* (2023) [[link]](https://arxiv.org/pdf/2310.13606)
- **Efficient Detection of LLM-generated Texts with a Bayesian Surrogate Model.** Zhijie Deng, Hongcheng Gao, Yibo Miao, and Hao Zhang. *arXiv preprint arXiv:2305.16617* (2023) [[link]](https://arxiv.org/abs/2305.16617)
- **On the generalization of training-based chatgpt detection methods.** Han Xu, Jie Ren, Pengfei He, Shenglai Zeng, Yingqian Cui, Amy Liu, Hui Liu, and Jiliang Tang. *arXiv preprint arXiv:2310.01307* (2023) [[link]](https://arxiv.org/pdf/2310.01307)
- **ChatGPT Generated Text Detection.** Rexhep Shijaku, and Ercan Canhasi. *Publisher: Unpublished* (2023) [[link]](https://www.researchgate.net/profile/Ercan-Canhasi/publication/366898047_ChatGPT_Generated_Text_Detection/links/63b76718097c7832ca932473/ChatGPT-Generated-Text-Detection.pdf)
- **DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.** Xianjun Yang, Wei Cheng, Linda Petzold, William Yang Wang, and Haifeng Chen. *arXiv preprint arXiv:2305.17359* (2023) [[link]](https://arxiv.org/abs/2305.17359)
- **Efficient Detection of LLM-generated Texts with a Bayesian Surrogate Model.** Zhijie Deng, Hongcheng Gao, Yibo Miao, and Hao Zhang. *arXiv preprint arXiv:2305.16617* (2023) [[link]](https://arxiv.org/abs/2305.16617)
- **GPT detectors are biased against non-native English writers.** Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric Wu, and James Zou. *Patterns* (2023) [[link]](https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7?ref=maginative.com)
- **Reverse Turing Test in the Age of Deepfake Texts.** Adaku Uchendu. *The Pennsylvania State University* (2023) [[link]](https://search.proquest.com/openview/afdfe44f26ff6fe708a2d768c3f87837/1?pq-origsite=gscholar&cbl=18750&diss=y)
- **How close is chatgpt to human experts? comparison corpus, evaluation, and detection.** Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang, Jinran Nie, Yuxuan Ding, Jianwei Yue, and Yupeng Wu. *arXiv preprint arXiv:2301.07597* (2023) [[link]](https://arxiv.org/abs/2301.07597)
- **Hc3 plus: A semantic-invariant human chatgpt comparison corpus.** Zhenpeng Su, Xing Wu, Wei Zhou, Guangyuan Ma, and Songlin Hu. *arXiv preprint arXiv:2309.02731* (2023) [[link]](https://arxiv.org/abs/2309.02731)
- **Llmdet: A third party large language models generated text detection tool.** Kangxi Wu, Liang Pang, Huawei Shen, Xueqi Cheng, and Tat-Seng Chua. *Findings of the Association for Computational Linguistics: EMNLP 2023* (2023) [[link]](https://arxiv.org/abs/2305.15004)
- **Fast-detectgpt: Efficient zero-shot detection of machine-generated text via conditional probability curvature.** Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang. *arXiv preprint arXiv:2310.05130* (2023) [[link]](https://arxiv.org/abs/2310.05130)
- **Radar: Robust ai-text detection via adversarial learning.** Xiaomeng Hu, Pin-Yu Chen, and Tsung-Yi Ho. *Advances in Neural Information Processing Systems* (2023) [[link]](https://proceedings.neurips.cc/paper_files/paper/2023/hash/30e15e5941ae0cdab7ef58cc8d59a4ca-Abstract-Conference.html)
- **Conda: Contrastive domain adaptation for ai-generated text detection.** Amrita Bhattacharjee, Tharindu Kumarage, Raha Moraffah, and Huan Liu. *arXiv preprint arXiv:2309.03992* (2023) [[link]](https://arxiv.org/abs/2309.03992)
- **On the zero-shot generalization of machine-generated text detectors.** Xiao Pu, Jingyu Zhang, Xiaochuang Han, Yulia Tsvetkov, and Tianxing He. *arXiv preprint arXiv:2310.05165* (2023) [[link]](https://arxiv.org/abs/2310.05165)
- **G3Detector: General GPT-generated text detector.** Haolan Zhan, Xuanli He, Qiongkai Xu, Yuxiang Wu, and Pontus Stenetorp. *arXiv preprint arXiv:2305.12680* (2023) [[link]](https://arxiv.org/abs/2305.12680)
- **Counter Turing Test CT^2: AI-Generated Text Detection is Not as Easy as You May Think--Introducing AI Detectability Index.** Megha Chakraborty, SM Tonmoy, SM Zaman, Krish Sharma, Niyar R Barman, Chandan Gupta, Shreya Gautam, Tanay Kumar, Vinija Jain, Aman Chadha, and others. *arXiv preprint arXiv:2310.05030* (2023) [[link]](https://arxiv.org/abs/2310.05030)
- **Long-form analogies generated by chatGPT lack human-like psycholinguistic properties.** SM Seals, and Valerie L Shalin. *arXiv preprint arXiv:2306.04537* (2023) [[link]](https://arxiv.org/abs/2306.04537)

- **Cross-domain detection of GPT-2-generated technical text.** Juan Diego Rodriguez, Todd Hay, David Gros, Zain Shamsi, and Ravi Srinivasan. *Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies* (2022) [[link]](https://aclanthology.org/2022.naacl-main.88/)

- **Cross-domain detection of GPT-2-generated technical text.** Juan Diego Rodriguez, Todd Hay, David Gros, Zain Shamsi, and Ravi Srinivasan. *Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: human language technologies* (2022) [[link]](https://aclanthology.org/2022.naacl-main.88.pdf)
- **Creating and detecting fake reviews of online products.** Joni Salminen, Chandrashekhar Kandpal, Ahmed Mohamed Kamel, Soon-gyo Jung, and Bernard J Jansen. *Journal of Retailing and Consumer Services* (2022) [[link]](https://www.sciencedirect.com/science/article/pii/S0969698921003374)
- **Detecting and understanding textual deepfakes in online reviews.** Peter Kowalczyk, Marco Röder, Alexander Dürr, and Frédéric Thiesse. *No venue* (2022) [[link]](https://aisel.aisnet.org/hicss-55/da/xai/3/)
- **On pushing DeepFake Tweet Detection capabilities to the limits.** Margherita Gambini, Tiziano Fagni, Fabrizio Falchi, and Maurizio Tesconi. *14th ACM Web Science Conference 2022* (2022) [[link]](https://dl.acm.org/doi/abs/10.1145/3501247.3531560)
- **Deepfake Text Detection: Limitations and Opportunities.** Jiameng Pu, Zain Sarwar, Sifat Muhammad Abdullah, Abdullah Rehman, Yoonjin Kim, Parantapa Bhattacharya, Mobin Javed, and Bimal Viswanath. *arXiv preprint arXiv:2210.09421* (2022) [[link]](https://ieeexplore.ieee.org/abstract/document/10179387/)
- **Synthetic Text Detection: Systemic Literature Review.** Jesus Guerrero, and Izzat Alsmadi. *arXiv preprint arXiv:2210.06336* (2022) [[link]](https://arxiv.org/abs/2210.06336)
- **Detecting computer-generated disinformation.** Harald Stiff, and Fredrik Johansson. *International Journal of Data Science and Analytics* (2022) [[link]](https://link.springer.com/article/10.1007/s41060-021-00299-5)
- **Comparing scientific abstracts generated by ChatGPT to original abstracts using an artificial intelligence output detector, plagiarism detector, and blinded human reviewers.** Catherine A Gao, Frederick M Howard, Nikolay S Markov, Emma C Dyer, Siddhi Ramesh, Yuan Luo, and Alexander T Pearson. *BioRxiv* (2022) [[link]](https://www.biorxiv.org/content/10.1101/2022.12.23.521610.abstract)
- **Findings of the the ruatd shared task 2022 on artificial text detection in russian.** Tatiana Shamardina, Vladislav Mikhailov, Daniil Chernianskii, Alena Fenogenova, Marat Saidov, Anastasiya Valeeva, Tatiana Shavrina, Ivan Smurov, Elena Tutubalina, and Ekaterina Artemova. *arXiv preprint arXiv:2206.01583* (2022) [[link]](https://arxiv.org/abs/2206.01583)
- **Automatic detection of Chinese generated essayss based on pre-trained BERT.** Xingyuan Chen, Peng Jin, Siyuan Jing, and Chunming Xie. *2022 IEEE 10th Joint International Information Technology and Artificial Intelligence Conference (ITAIC)* (2022) [[link]](https://ieeexplore.ieee.org/abstract/document/9836571/)
- **SynSciPass: detecting appropriate uses of scientific text generation.** Domenic Rosati. *arXiv preprint arXiv:2209.03742* (2022) [[link]](https://arxiv.org/pdf/2209.03742)
- **Robustness analysis of grover for machine-generated news detection.** Rinaldo Gagiano, Maria Myung-Hee Kim, Xiuzhen Jenny Zhang, and Jennifer Biggs. *Proceedings of the The 19th Annual Workshop of the Australasian Language Technology Association* (2021) [[link]](https://aclanthology.org/2021.alta-1.12.pdf)
- **All that's' human'is not gold: Evaluating human evaluation of generated text.** Elizabeth Clark, Tal August, Sofia Serrano, Nikita Haduong, Suchin Gururangan, and Noah A Smith. *arXiv preprint arXiv:2107.00061* (2021) [[link]](https://arxiv.org/abs/2107.00061)
- **Automated identification of social media bots using deepfake text detection.** Sina Mahdipour Saravani, Indrajit Ray, and Indrakshi Ray. *Information Systems Security: 17th International Conference, ICISS 2021, Patna, India, December 16--20, 2021, Proceedings* (2021) [[link]](https://link.springer.com/chapter/10.1007/978-3-030-92571-0_7)
- **Feature-based detection of automated language models: tackling GPT-2, GPT-3 and Grover.** Leon Fröhling, and Arkaitz Zubiaga. *PeerJ Computer Science* (2021) [[link]](https://peerj.com/articles/cs-443/)
- **Unsupervised and distributional detection of machine-generated text.** Matthias Gallé, Jos Rozen, Germán Kruszewski, and Hady Elsahar. *arXiv preprint arXiv:2111.02878* (2021) [[link]](https://arxiv.org/abs/2111.02878)
- **TweepFake: About detecting deepfake tweets.** Tiziano Fagni, Fabrizio Falchi, Margherita Gambini, Antonio Martella, and Maurizio Tesconi. *Plos one* (2021) [[link]](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0251415)
- **Through the looking glass: Learning to attribute synthetic text generated by language models.** Shaoor Munir, Brishna Batool, Zubair Shafiq, Padmini Srinivasan, and Fareed Zaffar. *Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume* (2021) [[link]](https://aclanthology.org/2021.eacl-main.155/)

- **Neural deepfake detection with factual structure of text.** Wanjun Zhong, Duyu Tang, Zenan Xu, Ruize Wang, Nan Duan, Ming Zhou, Jiahai Wang, and Jian Yin. *arXiv preprint arXiv:2010.07475* (2020) [[link]](https://arxiv.org/abs/2010.07475)

- **Automatic detection of machine generated text: A critical survey.** Ganesh Jawahar, Muhammad Abdul-Mageed, and Laks VS Lakshmanan. *arXiv preprint arXiv:2011.01314* (2020) [[link]](https://arxiv.org/pdf/2011.01314)
- **Authorship attribution for neural text generation.** Adaku Uchendu, Thai Le, Kai Shu, and Dongwon Lee. *Proceedings of the 2020 conference on empirical methods in natural language processing (EMNLP)* (2020) [[link]](https://aclanthology.org/2020.emnlp-main.673.pdf)
- **How effectively can machines defend against machine-generated fake news? an empirical study.** Meghana Moorthy Bhat, and Srinivasan Parthasarathy. *Proceedings of the First Workshop on Insights from Negative Results in NLP* (2020) [[link]](https://aclanthology.org/2020.insights-1.7.pdf)
- **How effectively can machines defend against machine-generated fake news? an empirical study.** Meghana Moorthy Bhat, and Srinivasan Parthasarathy. *Proceedings of the First Workshop on Insights from Negative Results in NLP* (2020) [[link]](https://aclanthology.org/2020.insights-1.7/)
- **Detecting cross-modal inconsistency to defend against neural fake news.** Reuben Tan, Bryan A Plummer, and Kate Saenko. *arXiv preprint arXiv:2009.07698* (2020) [[link]](https://arxiv.org/pdf/2009.07698)
- **The limitations of stylometry for detecting machine-generated fake news.** Tal Schuster, Roei Schuster, Darsh J Shah, and Regina Barzilay. *Computational Linguistics* (2020) [[link]](https://direct.mit.edu/coli/article-abstract/46/2/499/93369)

- **Defending against neural fake news.** Rowan Zellers, Ari Holtzman, Hannah Rashkin, Yonatan Bisk, Ali Farhadi, Franziska Roesner, and Yejin Choi. *Advances in neural information processing systems* (2019) [[link]](https://proceedings.neurips.cc/paper/2019/file/3e9f0fc9b2f89e043bc6233994dfcf76-Paper.pdf)
- **Gltr: Statistical detection and visualization of generated text.** Sebastian Gehrmann, Hendrik Strobelt, and Alexander M Rush. *arXiv preprint arXiv:1906.04043* (2019) [[link]](https://arxiv.org/abs/1906.04043)
- **The curious case of neural text degeneration.** Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. *arXiv preprint arXiv:1904.09751* (2019) [[link]](https://arxiv.org/abs/1904.09751)
- **Automatic detection of generated text is easiest when humans are fooled.** Daphne Ippolito, Daniel Duckworth, Chris Callison-Burch, and Douglas Eck. *arXiv preprint arXiv:1911.00650* (2019) [[link]](https://arxiv.org/abs/1911.00650)
- **Best practices for the human evaluation of automatically generated text.** Chris Van Der Lee, Albert Gatt, Emiel Van Miltenburg, Sander Wubben, and Emiel Krahmer. *Proceedings of the 12th International Conference on Natural Language Generation* (2019) [[link]](https://aclanthology.org/W19-8643/)

- **Identifying computer-generated text using statistical analysis.** Hoang-Quoc Nguyen-Son, Ngoc-Dung T Tieu, Huy H Nguyen, Junichi Yamagishi, and Isao Echi Zen. *2017 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC)* (2017) [[link]](https://ieeexplore.ieee.org/abstract/document/8282270/)

- **Computer-generated text detection using machine learning: A systematic review.** Daria Beresneva. *Natural Language Processing and Information Systems: 21st International Conference on Applications of Natural Language to Information Systems, NLDB 2016, Salford, UK, June 22-24, 2016, Proceedings 21* (2016) [[link]](https://link.springer.com/chapter/10.1007/978-3-319-41754-7_43)


### 3. LLM-generated Text Attribution
- **TURINGBENCH: A benchmark environment for Turing test in the age of neural text generation.** Adaku Uchendu, Zeyu Ma, Thai Le, Rui Zhang, and Dongwon Lee. *arXiv preprint arXiv:2109.13296* (2021) [[link]](https://arxiv.org/pdf/2109.13296)

- **Origin tracing and detecting of llms.** Linyang Li, Pengyu Wang, Ke Ren, Tianxiang Sun, and Xipeng Qiu. *arXiv preprint arXiv:2304.14072* (2023) [[link]](https://arxiv.org/abs/2304.14072)

- **Mgtbench: Benchmarking machine-generated text detection.** Xinlei He, Xinyue Shen, Zeyuan Chen, Michael Backes, and Yang Zhang. *arXiv preprint arXiv:2303.14822* (2023) [[link]](https://arxiv.org/pdf/2303.14822)

- **Overview of autextification at iberlef 2023: Detection and attribution of machine-generated text in multiple domains.** Areg Mikael Sarvazyan, José ángel González, Marc Franco-Salvador, Francisco Rangel, Berta Chulvi, and Paolo Rosso. *arXiv preprint arXiv:2309.11285* (2023) [[link]](https://arxiv.org/abs/2309.11285)

- **HANSEN: human and AI spoken text benchmark for authorship analysis.** Nafis Irtiza Tripto, Adaku Uchendu, Thai Le, Mattia Setzu, Fosca Giannotti, and Dongwon Lee. *arXiv preprint arXiv:2310.16746* (2023) [[link]](https://arxiv.org/abs/2310.16746)

- **Token prediction as implicit classification to identify LLM-generated text.** Yutian Chen, Hao Kang, Vivian Zhai, Liangze Li, Rita Singh, and Bhiksha Raj. *arXiv preprint arXiv:2311.08723* (2023) [[link]](https://arxiv.org/abs/2311.08723)

- **TOPFORMER: Topology-Aware Authorship Attribution of Deepfake Texts with Diverse Writing Styles.** Adaku Uchendu, Thai Le, and Dongwon Lee. *arXiv preprint arXiv:2309.12934* (2023) [[link]](https://arxiv.org/abs/2309.12934)


### 4. Human-LLM Co-authored Text Attribution

- **EditLens: Quantifying the Extent of AI Editing in Text.** Katherine Thai, Bradley Emi, Elyas Masrour, and Mohit Iyyer. *arXiv preprint arXiv:2510.03154* (2025) [[link]](https://arxiv.org/abs/2510.03154)

- **Imitate Before Detect: Aligning Machine Stylistic Preference for Machine-Revised Text Detection.** Jiaqi Chen, Xiaoye Zhu, Tianyang Liu, Ying Chen, Xinhui Chen, Yiwen Yuan, Chak Tou Leong, and others. *arXiv preprint arXiv:2412.10432* (2024) [[link]](https://arxiv.org/pdf/2412.10432)

- **LLM-as-a-Coauthor: Can Mixed Human-Written and Machine-Generated Text Be Detected?.** Qihui Zhang, Chujie Gao, Dongping Chen, Yue Huang, Yixin Huang, Zhenyang Sun, Shilin Zhang, Weiye Li, Zhengyan Fu, Yao Wan, and Lichao Sun. *Findings of the Association for Computational Linguistics: NAACL 2024* (2024) [[link]](https://aclanthology.org/2024.findings-naacl.29/)

- **Dna-gpt: Divergent n-gram analysis for training-free detection of gpt-generated text.** Xianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, and Haifeng Chen. *arXiv preprint arXiv:2305.17359* (2023) [[link]](https://arxiv.org/abs/2305.17359)

- **M4GT-Bench: Evaluation Benchmark for Black-Box Machine-Generated Text Detection.** Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohanned Afzal, Tarek Mahmoud, Giovanni Puccetti, Thomas Arnold, and others. *to appear in ACL 2024* (2024) [[link]](https://arxiv.org/abs/2402.11175)

- **Automatic Authorship Analysis in Human-AI Collaborative Writing.** Aquia Richburg, Calvin Bao, and Marine Carpuat. *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)* (2024) [[link]](https://aclanthology.org/2024.lrec-main.165/)

- **Real or fake text?: Investigating human ability to detect boundaries between human-written and machine-generated text.** Liam Dugan, Daphne Ippolito, Arun Kirubarajan, Sherry Shi, and Chris Callison-Burch. *Proceedings of the AAAI Conference on Artificial Intelligence* (2023) [[link]](https://ojs.aaai.org/index.php/AAAI/article/view/26501)

- **Automatic Detection of Hybrid Human-Machine Text Boundaries.** Joseph Cutler, Liam Dugan, Shreya Havaldar, and Adam Stein. (2021) [[link]](https://www.cis.upenn.edu/~jwc/assets/nlp.pdf)


## Contributing
We welcome contributions from the community. If you have a paper, dataset, or implementation to add, please submit a pull request or open an issue.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<!-- 
## Acknowledgments
We would like to thank the researchers and practitioners whose work has contributed to this survey. This repository aims to serve as a centralized resource for the community interested in authorship attribution in the era of LLMs. -->

---

## Contact
For any questions or inquiries, please contact [Baixiang Huang](mailto:bhuang15@hawk.iit.edu) and [Kai Shu](mailto:kai.shu@emory.edu).

---
By organizing and curating the extensive body of literature on authorship attribution, we hope this repository will be a valuable resource for researchers and practitioners in the field.
