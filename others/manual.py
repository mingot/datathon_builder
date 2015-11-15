import numpy as np
import time

start=time.time()

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
    r = tied_rank(posterior)
    num_positive = len([0 for x in actual if x==1])
    num_negative = len(actual)-num_positive
    sum_positive = sum([r[i] for i in range(len(r)) if actual[i]==1])
    auc = ((sum_positive - num_positive*(num_positive+1)/2.0) /
           (num_negative*num_positive))
    return auc

# results_file = open('/Users/mingot/Downloads/train_test/wifi/wife-high_151114105945_560.csv')
# results_file = open('/Users/mingot/Downloads/train_test/wifi/wife-high_151114105701_860.csv')
# results_file = open('/Users/mingot/Downloads/train_test/wifi/picadilly_151114113604_124.csv')


files = [
'/Users/mingot/Downloads/final/Alpha_aiorla_151115095842_277',
'/Users/mingot/Downloads/final/Bcn_R_users_group_Jordi_151115020356_108',
'/Users/mingot/Downloads/final/Green_Monkeys_Antonio_151115100244_817',
'/Users/mingot/Downloads/final/Hacaguays_cristian_pachon_151115094724_643',
'/Users/mingot/Downloads/final/Pretty_fly_for_a_wifi_picadilly_151115095817_930',
'/Users/mingot/Downloads/final/Red_Jaguars_xparedes_151115100106_862',
'/Users/mingot/Downloads/final/TeamUNO_xavijacas_151115095826_474',
'/Users/mingot/Downloads/final/The_G-Priors_uhoenig_151115095816_915',
'/Users/mingot/Downloads/final/Silver_Snakes_fizlazgmail_151115095811_825',
]

# results_file = open('/Users/mingot/Downloads/train_test/wifi/wife-high_151114104525_681.csv')

for result_filename in files:
    i = 0
    predicted_private = []
    predicted_public = []
    predicted_total = []
    results_file = open(result_filename)
    for r in results_file:
        if r=='':
            continue
        if r=='NA':
            r=0
        if r=='NA ':
            r=0
        try:
            predicted_total.append(float(r))
        except:
            print r
        if i%20==0:
            predicted_public.append(float(r))
        else:
            predicted_private.append(float(r))
        i+=1

    auc_public = auc(real_public, predicted_public)
    auc_private = auc(real_private, predicted_private)
    auc_total = auc(real_total, predicted_total)

    print "team: %s" % result_filename
    print "auc total: %f, auc private: %f, auc public: %f" % (auc_total, auc_private, auc_public)
