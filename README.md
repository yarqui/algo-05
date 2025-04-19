# Substring Search Algorithm Benchmark

This project compares the performance of three classical substring search algorithms:

- **Knuth-Morris-Pratt (KMP)**
- **Boyer-Moore**
- **Rabin-Karp**

Each algorithm is tested on two input files (`article 1.txt` and `article 2.txt`), using both a **present substring** (which exists in the file) and an **absent substring** (which does not exist in the file).

---

## Benchmark Results

### 📄 File: `article 1.txt`

| Algorithm   | Present Substring (`int elementToSearch`) | Absent Substring (`we're going to build a wall`) |
| ----------- | ----------------------------------------- | ------------------------------------------------ |
| KMP Search  | 0.0004020 sec                             | 0.0014240 sec                                    |
| Boyer-Moore | **0.0000956 sec**                         | **0.0002343 sec**                                |
| Rabin-Karp  | 0.0015899 sec                             | 0.0054957 sec                                    |

---

### 📄 File: `article 2.txt`

| Algorithm   | Present Substring (`linked list`) | Absent Substring (`we're going to build a wall`) |
| ----------- | --------------------------------- | ------------------------------------------------ |
| KMP Search  | 0.0006962 sec                     | 0.0019689 sec                                    |
| Boyer-Moore | **0.0004846 sec**                 | **0.0003038 sec**                                |
| Rabin-Karp  | 0.0028198 sec                     | 0.0076888 sec                                    |

---

## Conclusions

- **Boyer-Moore consistently outperforms the other algorithms** for both present and absent substring cases, due to its efficient use of character skipping via its bad character heuristic.
- **KMP performs reasonably well**, especially on medium-sized texts, and offers consistent linear-time performance regardless of pattern content.
- **Rabin-Karp is the slowest** in this comparison, especially when the substring is not found. This is because its hashing approach still requires character-by-character comparisons after hash matches and is sensitive to collisions.
- **Absent substrings** increase execution time across all algorithms, as the search must scan more of the text.

---

## Takeaway

Although all three algorithms are theoretically efficient, **Boyer-Moore** is practically the best choice for most substring search tasks in large texts, especially when frequent mismatches are expected.

---
