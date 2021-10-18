import json
import random
import sys
class IVerbs:
    def guess(self):
        print('# List irregulars verbs #')
        with open('dict/verbs_rus.json') as json_file:
            verbs = json.load(json_file)

        successList = []

        totalVerbs = len(verbs) - 1
        verbKeys = list(verbs.keys())
        continues = 1
        while(continues):
            verbRandom = random.randint(0, totalVerbs)
            verb = verbKeys[verbRandom]
            isSuccess = True
            isSure = True
            if verb != "" and not verb in successList:
                print("\nTranslation:", verbs[verb]['translation'])
                inputVerb = self.input('Infinitive:')
                isCorrect,isSure_ = self.check(inputVerb, verb)
                if isCorrect:
                    print('\033[92m ok\033[0m')
                else:
                    print('\033[91m x\033[0m')
                    isSuccess = False
                isSure = (isSure_ if isSure else False)

                inputVerb = self.input('Past Simple:')
                isCorrect,isSure_ = self.check(inputVerb, verbs[verb]['past'])
                if isCorrect:
                    print('\033[92m ok\033[0m')
                else:
                    print('\033[91m x\033[0m')
                    isSuccess = False
                isSure = (isSure_ if isSure else False)

                inputVerb = self.input('Past Participle:')
                isCorrect,isSure_ = self.check(inputVerb, verbs[verb]['participle'])
                if isCorrect:
                    print('\033[92m ok\033[0m')
                else:
                    print('\033[91m x\033[0m')
                    isSuccess = False
                isSure = (isSure_ if isSure else False)

                if isSuccess == False:
                    print('--->>>: {} {} {}'.format(verb, verbs[verb]['past'], verbs[verb]['participle']))
                else:
                    if isSure:
                        successList.append(verb)
                    if len(successList) >= totalVerbs:
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
