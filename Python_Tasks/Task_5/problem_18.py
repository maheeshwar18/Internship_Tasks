# Qno 18
# Minion Game
def minion_game(string):
    vowel_score = 0
    consonant_score = 0
    vowels = "AEIOU"

    for i in range(len(string)):
        if string[i] in vowels:
            vowel_score += len(string) - i
        else:
            consonant_score += len(string) - i

    if vowel_score > consonant_score:
        print("Kevin", vowel_score)
    elif consonant_score > vowel_score:
        print("Stuart", consonant_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
