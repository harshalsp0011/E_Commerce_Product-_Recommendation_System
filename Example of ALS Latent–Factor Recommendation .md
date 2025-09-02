<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Example of ALS Latent–Factor Recommendation

Consider the following small user–item interaction table, where each “strength” reflects implicit feedback (view = 1, add-to-cart = 3, purchase = 5):


| user_id | item | strength |
| :-- | :-- | :-- |
| 11001 | A | 1 |
| 11002 | B | 8 |
| 11003 | C | 1 |
| 11004 | D | 5 |
| 11004 | B | 1 |

**Step 1: Build the Interaction Matrix**
Rows index items [A, B, C, D], columns index users [11001][11002][11003][11004]:


|  | 11001 | 11002 | 11003 | 11004 |
| :-- | :-- | :-- | :-- | :-- |
| **A** | 1 | 0 | 0 | 0 |
| **B** | 0 | 8 | 0 | 1 |
| **C** | 0 | 0 | 1 | 0 |
| **D** | 0 | 0 | 0 | 5 |

**Step 2: Factorize into Latent Factors**
Suppose ALS learns 2-dimensional latent vectors for each user and each item:

- Users:
– 11001 → $u_{11001} = [0.8,\;0.1]$
– 11002 → $u_{11002} = [0.2,\;0.9]$
– 11003 → $u_{11003} = [0.1,\;0.3]$
– 11004 → $u_{11004} = [0.5,\;0.4]$
- Items:
– A → $v_A = [0.9,\;0.2]$
– B → $v_B = [0.1,\;0.8]$
– C → $v_C = [0.4,\;0.4]$
– D → $v_D = [0.3,\;0.7]$

**Step 3: Compute Predicted Scores**
The predicted affinity score for user $i$ and item $j$ is the dot product $u_i \cdot v_j$. For user 11004 (with vector $[0.5,0.4]$) computing for unseen items A and C:

$$
\begin{aligned}
\text{score}(11004, A) &= [0.5,\,0.4]\cdot[0.9,\,0.2] = 0.5\times0.9 + 0.4\times0.2 = 0.45 + 0.08 = 0.53,\\
\text{score}(11004, B) &= [0.5,\,0.4]\cdot[0.1,\,0.8] = 0.05 + 0.32 = 0.37,\\
\text{score}(11004, C) &= [0.5,\,0.4]\cdot[0.4,\,0.4] = 0.20 + 0.16 = 0.36,\\
\text{score}(11004, D) &= [0.5,\,0.4]\cdot[0.3,\,0.7] = 0.15 + 0.28 = 0.43.
\end{aligned}
$$

**Step 4: Generate Top-N Recommendations**
Rank the scores for user 11004 in descending order:


| item | score |
| :-- | :-- |
| A | 0.53 |
| D | 0.43 |
| B | 0.37 |
| C | 0.36 |

For **Top-2** recommendations for user 11004:

1. **Item A** (score 0.53)
2. **Item D** (score 0.43)

This simple example illustrates how ALS leverages learned latent vectors to predict user affinity for unseen items and produce personalized recommendations.

