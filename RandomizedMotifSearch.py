# import the random package here
import random
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomMotifs(Dna, k, t):
    # place your code here.
    motifs= []
    for i in range(t):
        ind = random.randint(0, len(Dna[0])-k)
        motif = Dna[i][ind:ind +k]
        motifs.append(motif)
    return motifs

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 
        
 
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    profile= {}
    ## divide the number of motif strings to get frequency
    for letter in count.keys():
        profile[letter] = [float(x)/ (t+4) for x in count[letter]]
    return profile

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

def ProfileMostProbablePattern(Text, k, Profile):
    p_dict = {}
    for i in range(len(Text)- k +1):
        p = Pr(Text[i: i+k], Profile)
        p_dict[i] = p
    m = max(p_dict.values())
    keys = [k for k,v in p_dict.items() if v == m]
    ind = keys[0]
    return Text[ind: ind +k]

def Consensus(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    consensus = Consensus(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    score = 0
    for i in range(k):
        FrequentSymbol = consensus[i]
        for j in range(t):
            if Motifs[j][i] != FrequentSymbol:
                score = score + 1
    return score

def Motifs(Profile, Dna):
    motifs = []
    t = len(Dna)
    #k = 4
    for i in range(t):
        motif = ProfileMostProbablePattern(Dna[i], k, Profile)
        motifs.append(motif)
    return motifs


# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
