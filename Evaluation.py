"""
Lab NLP: Implement Evaluation
Author: Zhanruo Qu
"""
def IO_function(file):
    labels = list()
    for line in file:
        labels.append(line.strip())
    return labels

def get_emotions(list_gold):
    emotions = list(set(list_gold))
    return  emotions

def emo_evaluation(emotion,list_gold,list_prediction):
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    for i in range(len(list_gold)):
        if list_gold[i] == list_prediction[i] and list_gold[i] == emotion:
        	tp += 1
        elif list_prediction[i] == emotion and list_gold[i] != emotion:
        	fp += 1
        elif list_gold[i] == emotion and list_prediction[i] != emotion:
        	fn += 1
        else:
        	tn += 1

    print ('tp:%d, fp:%d, fn:%d, tn:%d' % (tp,fp,fn,tn))
    p = tp / (tp + fp)
    #print (p)
    r = tp / (tp + fn)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    f1_score = 2 * (p * r) / (p + r)
    result = [p , r , accuracy ,f1_score]
    return result

def main():
    File_gold = open("dev.txt")
    File_prediction = open("dev-predicted.csv")
    Labels_gold = IO_function(File_gold)
    Labels_prediction = IO_function(File_prediction)
    emotions = get_emotions(Labels_gold)
    for emotion in emotions:
        print (emotion)
        p , r , accuarcy, f1_score =  emo_evaluation(emotion, Labels_gold , Labels_prediction)
        print ("p",p,"r",r,"accuracy",accuarcy,"f1-score",f1_score)

if __name__ == "__main__":
    main()
