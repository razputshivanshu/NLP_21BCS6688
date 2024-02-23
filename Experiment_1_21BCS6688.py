#Experiment 1: Apply Different Tokenization Techniques using NLTK

arr = "You have to apply different Tokenization techniques using1 NLTK Library like WordTokenizer, SentenceTokenizer, RegExpTokenizer and more. And you can choose any one of them according to your requirements.";
print(arr.split(" "));

print('\n')


#Word Tokenization
print('----Word Tokenization------')
import nltk
word_data = "Array and vector is a Linear data structure that stores data in the continuous memory locations."
nltk_tokens = nltk.word_tokenize(word_data);
print(nltk_tokens);


print('\n')

#sentence tokenization
print('----Sentence Tokenization------')
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
tokenize_sen=tokenizer.tokenize(arr)
print(tokenize_sen[0]);
print(tokenize_sen[1]);



#tokenize regular expression
print('\n----Tokenization using regular expressions------')
from nltk.tokenize import RegexpTokenizer 
space_k = RegexpTokenizer('\s+', gaps = True) 
number_k = RegexpTokenizer('\d+', gaps=True)
stop_k= RegexpTokenizer('\.', gaps=True)
print("\nOrignal Array: ",arr)
print("\nTokenization on the basis of space", space_k.tokenize(arr));
print('\n');

print("Tokenization on the basis of numbers: ",number_k.tokenize(arr));
print('\n');

print("Tokenization on the basis of sentence ",stop_k.tokenize(arr));


