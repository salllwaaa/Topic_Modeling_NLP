import json
from nltk.corpus import wordnet as wn



stops = {}
with open ("utils/stops.json", "r") as file:
    stops = json.load(file)

  
tagMap = {
        'CD':wn.NOUN, # cardinal number (one, two)             
        'EX':wn.ADV, # existential ‘there’ (there)           
        'FW':wn.NOUN, # foreign word (mea culpa)             
        'IN':wn.ADV, # preposition/sub-conj (of, in, by)   
        'JJ':wn.ADJ, # adjective (yellow)                  
        'JJR':wn.ADJ,  # adj., comparative (bigger)          
        'JJS':wn.ADJ,  # adj., superlative (wildest)           
        'MD':wn.VERB, # modal (can, should)                    
        'NN':wn.NOUN, # noun, sing. or mass (llama)          
        'NNS':wn.NOUN, # noun, plural (llamas)                  
        'NNP':wn.NOUN, # proper noun, sing. (IBM)              
        'NNPS':wn.NOUN, # proper noun, plural (Carolinas)
        'PDT':wn.ADJ, # predeterminer (all, both)            
        'PRP':wn.NOUN, # personal pronoun (I, you, he)     
        'PRP$':wn.NOUN, # possessive pronoun (your, one’s)    
        'RB':wn.ADV, # adverb (quickly, never)            
        'RBR':wn.ADV, # adverb, comparative (faster)        
        'RBS':wn.ADV, # adverb, superlative (fastest)     
        # 'RP':[wn.ADJ, wn.ADJ_SAT], # particle (up, off)
        'RP':wn.ADJ, # particle (up, off)
        'VB':wn.VERB, # verb base form (eat)
        'VBD':wn.VERB, # verb past tense (ate)
        'VBG':wn.VERB, # verb gerund (eating)
        'VBN':wn.VERB, # verb past participle (eaten)
        'VBP':wn.VERB, # verb non-3sg pres (eat)
        'VBZ':wn.VERB, # verb like (comes)
        'WDT':wn.ADJ, # wh-determiner (which, that)
        'CC':wn.NOUN, # coordin. conjunction (and, but, or)  
        'DT':wn.NOUN, # determiner (a, the)                    
        'WP':wn.NOUN, # wh-pronoun (what, who)
        'WP$':wn.NOUN, # possessive (wh- whose)
        'WRB':wn.NOUN, # wh-adverb (how, where)
        'POS':wn.NOUN, # possessive ending (’s )               
        'LS':wn.NOUN, # list item marker (1, 2, One)          
        'TO':wn.NOUN, # “to” (to)
        'UH':wn.NOUN, # interjection (ah, oops)'VBZ':wn.VERB, # verb 3sg pres (eats)
        'SYM':wn.NOUN, # symbol (+,%, &)
        '$':wn.NOUN, #  dollar sign ($)
        '#': wn.NOUN, # pound sign (#)
        '“': wn.NOUN, # left quote (‘ or “)
        '”': wn.NOUN, # right quote (’ or ”)
        '(': wn.NOUN, # left parenthesis ([, (, {, <)
        ')': wn.NOUN, # right parenthesis (], ), }, >)
        ',': wn.NOUN, # comma (,)
        '.': wn.NOUN, # sentence-final punc (. ! ?)
        ':': wn.NOUN, # mid-sentence punc (: ; ... – -)
        "''": wn.NOUN,
        "``": wn.NOUN,
    }
