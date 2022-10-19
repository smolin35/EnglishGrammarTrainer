import json
import random
import sys

class IVerbs:
    def guess(self):
        print('# List irregulars verbs #')
        #with open('dict/verbs_test.json') as json_file:

        with open(sys.argv[1]) as json_file:
            words = json.load(json_file)

        successList = []

        totalWords = len(words) - 1
        wordsKeys = list(words.keys())
        continues = 1
        isOneTimeRepeat = False
        while(continues):
            if isOneTimeRepeat == False:
                wordRandom = random.randint(0, totalWords)
            word = wordsKeys[wordRandom]
            isSuccess = True
            isSure = True
            if word != "" and not word in successList:
                print(f'\n{word} :')
                for k in words[word].keys():
                    inputWorld = self.input(f'  {k}:')
                    isCorrect,isSure_ = self.check(inputWorld, words[word][k])
                    if isCorrect:
                        print('\033[92m ok\033[0m')
                    else:
                        print('\033[91m x\033[0m')
                        isSuccess = False
                    isSure = (isSure_ if isSure else False)

                if isSuccess == False:
                    print('\033[33m--->>>\033[0m: ', end='')
                    for k in words[word].keys():
                        print({words[word][k]})
                    isOneTimeRepeat = True
                else:
                    if isSure and isOneTimeRepeat == False:
                        successList.append(word)
                    isOneTimeRepeat = False

                    if len(successList) >= totalWords:
                        print("")
                        print("======== Congratulation! ========")
                        print("And... Let's repeat it again =)")
                        successList.clear()

        print('This\' the end')

    def input(self, label):
        result = input(label+" ")
        sys.stdout.write("\033[F")
        print(label, result, end=' ...')
        return result

    def check(self, v, correct):
        result = False
        isSure = True
        if len(v) > 1 and v[-1] == '?':
            isSure = False
            v = v[:-1]
        if len(v)>1 and v == correct:
            return True, isSure
        else:
            return False, isSure

Verb = IVerbs()
Verb.guess()
