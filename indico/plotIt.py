import matplotlib.pyplot as plt

badReview = {'anger': 0.6636017561, 'joy': 0.0246269684, 'sadness': 0.22964957360000002, 'fear': 0.0575886741, 'surprise': 0.0245330147}

goodReview = {'anger': 0.0368778966, 'joy': 0.7489670515, 'fear': 0.0957892686, 'sadness': 0.0645314008, 'surprise': 0.0538343713}

review = badReview

plt.bar(range(len(review)), list(review.values()), align='center')
plt.xticks(range(len(review)), list(review.keys()))
plt.xlabel("Emotion", fontsize=12, fontweight='bold') 
plt.ylabel("Level", fontsize=12, fontweight='bold') 
plt.suptitle('Negative Review', fontsize=14, fontweight='bold')
plt.show() 
