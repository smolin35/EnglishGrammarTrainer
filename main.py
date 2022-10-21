import json
import random
import sys
import os
import numpy as np
import csv

__PROMOTION_NUM = 4

def __input(label):
    result = input(label+" ")
    sys.stdout.write("\033[F")
    print(label, result, end=' ...')
    return result

def check(v, correct):
    result = False
    isSure = True
    if len(v) > 1 and v[-1] == '?':
        isSure = False
        v = v[:-1]
    if len(v)>1 and v == correct:
        return True, isSure
    else:
        return False, isSure


#with open('dict/verbs_test.json') as json_file:

if len(sys.argv) != 2:
    print('Укажите путь до словаря')
    quit()

dictPath = sys.argv[1]

level = 9999

promotionPath = dictPath[:dictPath.rindex('.')] + '.promotion'

promotion = {}
if os.path.exists(promotionPath):
    with open(promotionPath) as promotion_file:
        promotionReader = csv.reader(promotion_file, delimiter=';')
        for l in promotionReader:
            promotion[l[0]] = l[1]
            if int(l[1]) < level:
                level = int(l[1])
        if promotionReader.line_num == 0:
            level = 0

with open(dictPath) as json_file:
    words = json.load(json_file)

successList = []

totalWords = len(words) - 1
wordsKeys = list(words.keys())
continues = 1
isOneTimeRepeat = False
wordIndex = 0
level_min = 9999

print(f'Level:\033[33m{level_min}\033[0m')
print('-------------')
while(continues):
    word = wordsKeys[wordIndex]
    isSuccess = True
    isSure = True
    #if word != "" and not word in successList:
    if word != "":

        promotion_succes = 0
        if not word in promotion:
            promotion[word] = 0# 0 успешных
        else:
            promotion_succes = int(promotion[word])

        if promotion_succes <= level+1:
            print(f'\n{word} ({promotion_succes}):')
            for k in words[word].keys():
                inputWorld = __input(f'  {k}:')
                isCorrect,isSure_ = check(inputWorld, words[word][k])
                if isCorrect:
                    print('\033[92m ok\033[0m')
                else:
                    print('\033[91m x\033[0m')
                    isSuccess = False
                isSure = (isSure_ if isSure else False)

            if isSuccess == False:
                for k in words[word].keys():
                    print('\033[33m--->>>\033[0m: ', end='')
                    print(words[word][k])
                isOneTimeRepeat = True
                promotion_succes -= 1
                if promotion_succes < 0:
                    promotion_succes = 0
                promotion[word] = promotion_succes
            else:
                if isSure and isOneTimeRepeat == False:
                    successList.append(word)
                    promotion_succes += 1
                    promotion[word] = promotion_succes
                isOneTimeRepeat = False

            if promotion_succes < level_min:
                level_min = promotion_succes

    if isOneTimeRepeat == False:
        wordIndex += 1
        if wordIndex > totalWords:
            with open(promotionPath, 'w') as promotion_file:
                for p in promotion:
                    promotion_file.write(p + ';' + str(promotion[p]) + '\n')
            wordIndex = 0
            print('\n\033[92m======= CONGRATILUTIONS =======\033[0m')
            print(f'Next level:\033[33m{level_min}\033[0m')
            print('-------------')
            level = level_min
            level_min = 9999


        # if len(successList) >= totalWords:
            # print("")
            # print("======== Congratulation! ========")
            # print("And... Let's repeat it again =)")
            # successList.clear()



