import os
classes = [
   'Actinic Keratoses',
   'Basal Cell Carcinoma',
   'Benign Keratosis',
   'Dermatofibroma',
   'Melanoma',
   'Melanocytic Nevi',
   'Vascular naevus'
]

l = os.listdir("./testing")
res_class=[]
res_prob=[]
true_res= ["akiec","akiec","akiec","akiec","akiec","akiec","akiec","akiec","akiec","akiec","akiec","akiec","akiec","akiec","akiec","bcc","bcc","bcc","bcc","bcc","bcc","bcc","bcc","bcc","bcc","bcc","bcc","bcc","bcc","bkl","bkl","bkl","bkl","bkl","bkl","bkl","bkl","bkl","bkl","bkl","bkl","bkl","bkl","df","df","df","df","df","df","df","df","df","df","df","df","df","df","mel","mel","mel","mel","mel","mel","mel","mel","mel","mel","mel","mel","mel","mel","mel","nv","nv","nv","nv","nv","nv","nv","nv","nv","nv","nv","nv","nv","nv","nv","vasc","vasc","vasc","vasc","vasc","vasc","vasc","vasc","vasc","vasc","vasc","vasc","vasc",]
for i in l:
    result = model.predict(i)
    dict_result = {}
    for i in range(7):
        dict_result[result[0][i]] = classes[i]

    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:3]
        
    prob_result = []
    class_result = []
    for i in range(3):
        prob_result.append((prob[i]*100).round(2))
        class_result.append(dict_result[prob[i]])
    
    res_class.append(class_result)
    res_prob.append(prob_result)

accuracy = 0
for x in range(len(res_class)):
    if res_class[x]==true_res[x]:
        accuracy+=1

