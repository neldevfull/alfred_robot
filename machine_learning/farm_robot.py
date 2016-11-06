"""
FarmRobot is an algorithm multinomial Bayesian
to classify whether the referenced animal is pig or dog

Data used for classification
-------------------------------------------------------------------------------
There are an array containing the values 1 or 0
meaning: fat ? short leg ? bark ?

result is 1 for pig and -1 for dog

"""

from sklearn.naive_bayes import MultinomialNB


def main():
    pig1 = [1, 1, 0]
    pig2 = [1, 1, 0]
    pig3 = [1, 1, 0]

    dog1 = [1, 1, 1]
    dog2 = [0, 1, 1]
    dog3 = [0, 0, 1]

    data = [pig1, pig2, pig3, dog1, dog2, dog3]
    results = ['pig', 'pig', 'pig', 'dog', 'dog', 'dog']

    sample1 = [1, 1, 1]
    sample2 = [1, 0, 0]
    sample3 = [1, 0, 1]
    sample4 = [0, 1, 0]
    set_sample = [sample1, sample2, sample3, sample4]

    model = MultinomialNB()
    model.fit(data, results)

    print(model.predict(set_sample))


if __name__ == '__main__':
    main()
