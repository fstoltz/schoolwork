
class SentimentStore:
    def __init__(self):
        # : decide which data structure you need to track
        #   the sentiment of each word
        # : decide which data structure you need to track
        #   the number of times each word has been seen
        self.totalWordCount = 0
        self.uniqueWordScore = {}
        self.seenCounter = {}
    
    def getNumberOfWords(self):
        # returns the number of unique words in the dataset
        return len(self.uniqueWordScore)

    def getNumberOfPositiveWords(self):
        # return the number of unique words with positive scores
        numPos = 0
        for score in self.uniqueWordScore.values():
            if score >= 1:
                numPos += 1
        return numPos
        
    def getNumberOfNegativeWords(self):
        # return the number of unique words with negative scores
        numNeg = 0
        for score in self.uniqueWordScore.values():
            if score <= -1:
                numNeg += 1
        return numNeg

    def getTotalWordCount(self):
        # return the total number of words in the store
        return self.totalWordCount

    def addWordScore(self, word, score):
        #   add a word with a score
        #        - add score to our running total score for that word
        #        - add 1 to our count for number of times this word has been seen

        #####################################################
        # Handle running total score for 'word' #
        if word in self.uniqueWordScore:
            if score == 1: # Positive(increment by 1)
                self.uniqueWordScore[word] += 1
            if score == -1: # Negative(decrement by 1)
                self.uniqueWordScore[word] -= 1

        if word not in self.uniqueWordScore: # (first occurance of this 'word')
            self.uniqueWordScore[word] = score
        #####################################################
        # handle number of times 'word' has been seen #
        if word in self.seenCounter: #om det är en upprepning, increment by 1
            self.seenCounter[word] += 1
        if word not in self.seenCounter: # om det är första gången ett ord ses, initalize to 1
            self.seenCounter[word] = 1

    def addStringScore(self, string, score):
        words = string.split(" ")
        for word in words:
            if len(word) > 3: # ignore short words
                self.addWordScore(word, score)
                self.totalWordCount += 1

    def getWordSentiment(self, word):
        # : return sentiment score for a given word,
        # : return 0 if word not in store
        if word in self.uniqueWordScore:
            return self.uniqueWordScore[word]
        else:
            return 0

    def getWordCount(self, word):
        # : return how many times we have seen a word
        # : return 0 if word not in store
        if word in self.seenCounter:
            return self.seenCounter[word]
        else:
            return 0
        

    def getNormalizedWordSentiment(self, word):
        # This function is important - by normalizing the data we compensate
        # for the fact that some words occurs far more often than others.
        if self.getWordCount(word) != 0:
            return self.getWordSentiment(word) / self.getWordCount(word)
        else:
            return 0


    def getStringSentiment(self, s):
        score = 0
        count = 0
        words = s.split(" ")
        for word in words:
            if len(word) > 3: # ignore short words
                count += 1
                word = word.lower()
                score += self.getNormalizedWordSentiment(word)
        return score / count
