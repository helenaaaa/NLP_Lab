"""
Lab NLP: Implement Evaluation
Author: Zhanruo Qu
"""
def IO_function(file):
    labels = list()
    for line in file:
        labels.append(line)
    return labels

def Evaluation(gold_labels,pre_labels):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for num in len(gold_labels):
        if gold_labels(num) == pre_labels(num):
            TP += 1
        else:
            FN += 1


