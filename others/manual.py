result_file = open('/Users/mingot/Projectes/BCNAnalytics/hackathon/test.csv')
real_private = []
real_public = []
real_total = []
public_indexes = []
i = 0
for r in result_file:
    real_total.append(int(r))
    if i%20==0:  # Private (20%)
        real_public.append(int(r))
        public_indexes.append(i)

    else:
        real_private.append(int(r))
    i+=1


def tied_rank(x):
    """
    This function computes the tied rank of elements in x.
    Parameters
    ----------
    x : list of numbers, numpy array
    Returns
    -------
    score : list of numbers
            The tied rank f each element in x
    """
    sorted_x = sorted(zip(x,range(len(x))))
    r = [0 for k in x]
    cur_val = sorted_x[0][0]
    last_rank = 0
    for i in range(len(sorted_x)):
        if cur_val != sorted_x[i][0]:
            cur_val = sorted_x[i][0]
            for j in range(last_rank, i): 
                r[sorted_x[j][1]] = float(last_rank+1+i)/2.0
            last_rank = i
        if i==len(sorted_x)-1:
            for j in range(last_rank, i+1): 
                r[sorted_x[j][1]] = float(last_rank+i+2)/2.0
    return r

def auc(actual, posterior):
    """
    This function computes the AUC error metric for binary classification.
    Parameters
    ----------
    actual : list of binary numbers, numpy array
             The ground truth value
    posterior : same type as actual
                Defines a ranking on the binary numbers, from most likely to
                be positive to least likely to be positive.
    Returns
    -------
    score : double
            The mean squared error between actual and posterior
    """
    r = tied_rank(posterior)
    num_positive = len([0 for x in actual if x==1])
    num_negative = len(actual)-num_positive
    sum_positive = sum([r[i] for i in range(len(r)) if actual[i]==1])
    auc = ((sum_positive - num_positive*(num_positive+1)/2.0) /
           (num_negative*num_positive))
    return auc

results_file = open('/Users/mingot/Downloads/train_test/wifi/wife-high_151114105945_560.csv')
results_file = open('/Users/mingot/Downloads/train_test/wifi/wife-high_151114105701_860.csv')
results_file = open('/Users/mingot/Downloads/train_test/wifi/picadilly_151114113604_124.csv')

# results_file = open('/Users/mingot/Downloads/train_test/wifi/wife-high_151114104525_681.csv')



i = 0
predicted_private = []
predicted_public = []
predicted_total = []
for r in results_file:
    if r=='':
        continue
    predicted_total.append(float(r))
    if i%20==0:
        predicted_public.append(float(r))
    else:
        predicted_private.append(float(r))
    i+=1

print len(real_public)
print len(predicted_public)
print real_public[0:10]
print predicted_public[0:10]
auc_public = auc(real_public, predicted_public)
auc_private = auc(real_private, predicted_private)
auc_total = auc(real_total, predicted_total)

print auc_public
print auc_private
print auc_total
