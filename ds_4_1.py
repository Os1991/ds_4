# hit rate at k
import numpy as np
import pandas as pd


def hit_rate_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list[:k])

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate

# money_precision_at_k

def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    bought_list = bought_list
    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    flags = np.isin(recommended_list, bought_list)

    bought_sum = sum(flags * prices_recommended)
    recommended_sum = sum(prices_recommended)
    precision = bought_sum / recommended_sum

    return precision

# recall_at_k

def recall_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall

# money_recall_at_k

def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]
    flags = np.isin(recommended_list, bought_list)
    recommended_rel_sum = sum(flags * prices_recommended)
    rel_sum = sum(prices_bought)
    recall = recommended_rel_sum / rel_sum

    return recall

# map_k

def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    # assert len(bought_list) > len(recommended_list)
    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def ap_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(recommended_list, bought_list)

    if sum(flags) == 0:
        return 0

    sum_ = 0
    for i in range(0, k - 1):
        if flags[i] == True:
            p_k = precision_at_k(recommended_list, bought_list, k=i + 1)
            sum_ += p_k

    result = sum_ / sum(flags)

    return result


def map_k(recommended_list, bought_list, k=5, u=1):
    sum_ = 0
    for i in range(0, u - 1):
        sum_ += ap_k(recommended_list[i], bought_list[i], k)

    result = sum_ / u

    return result