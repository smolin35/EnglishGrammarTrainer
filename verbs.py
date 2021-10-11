import json
import random
import sys
class IVerbs:
    def guess(self):
        print('# List irregulars verbs #')
        with open('verbs.json') as json_file:
            verbs = json.load(json_file)

        successList = []

        totalVerbs = len(verbs) - 1
        verbKeys = list(verbs.keys())
        continues = 1
        while(continues):
            verbRandom = random.randint(0, totalVerbs)
            verb = verbKeys[verbRandom]
            isSuccess = True
            print(verbs[verb]['translation'])
            if verb != "" and not verb in successList:
                print("\nTranslation:", verbs[verb]['translation'])
                inputPast = self.input('Infinitive:')
                if (verb == inputPast):
                    print('\033[92m ok\033[0m')
                else:
                    print('\033[91m x\033[0m')
                    isSuccess = False
                pass
                inputPast = self.input('Past Simple:')
                if (verbs[verb]['past'] == inputPast):
                    print('\033[92m ok\033[0m')
                else:
                    print('\033[91m x\033[0m')
                    isSuccess = False
                pass
                inputPastParticiple = self.input('Past Participle:')
                if (verbs[verb]['participle'] == inputPastParticiple):
                    print('\033[92m ok\033[0m')
                else:
                    print('\033[91m x\033[0m')
                    isSuccess = False
                if isSuccess == False:
                    print('--->>>: {} {} {}'.format(verb, verbs[verb]['past'], verbs[verb]['participle']))
                else:
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

Verb = IVerbs()
Verb.guess()
