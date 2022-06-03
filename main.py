
##20188022&&20188009&&20188036
########################################

from tkinter import *
import numpy as np
import string
import nltk
from nltk.util import ngrams
import re
import tkinter as tk
root = tk.Tk()
root.geometry("500x300")


def search(data,input):
    file = open(data, "r", encoding="utf8")
    data = file.read()
    file.close()

    # split data in single words
    # words = data.split()
    # print(words)
    ######################################################
    # words = [w.strip(" ") for w in data]
    #print(words)
    #split data in single words by tokens
    words = nltk.word_tokenize(data)
    words_lower=[]
    for i in words:
        words_lower.append(i.lower())


    # ---------------------------------------------------------------------------------------------------

    # calculating probabilities of single word
    probility_word={}
    for i in words_lower:
        probility_word[i]=words_lower.count(i)
    print("probabilty of word:",probility_word)
    ############################
    #Get the count of 2 words(bigrams) and store it in dictionary key is word and value is number of occurance
    bigram=nltk.ngrams(words_lower,2)
    bigramdic={}
    for i in bigram:
        if i not in bigramdic.keys():
            bigramdic[i] = 1
        else:
            bigramdic[i] += 1
    print("probabilty of two words:",bigramdic)
    # print(bigramdic.keys())
    # print(bigramdic.values())

    # for i in range(len(words) - 1):
    #     seq = ' '.join(words[i:i + 2])
    #     if seq not in bigram.keys():
    #         bigram[seq] = 1
    #     else:
    #         bigram[seq] += 1

    #Get probility of second word
    probility_upcomword={}
    for bi in bigramdic:

        seq = ''.join(bi[0])
        probility_upcomword[bi] = bigramdic[bi]/probility_word[seq]
    print("probabilty of filnal:",probility_upcomword)


    # predicted funcion
    output = []
    input=input.lower()
    for i in probility_upcomword.keys():
        if input in i  :
            if (i[0] == input ):

                output.append((i, probility_upcomword[i]))




    output.sort(key=lambda x: x[1], reverse=True)  # descending


    numOfSuggestions = 10 # words that will be suggested
    if numOfSuggestions > len(output):
        numOfSuggestions = len(output)
    list_up_words=[]
    for i in range(numOfSuggestions):
        seq = ' '.join(output[i][0])
        list_up_words.append(seq)
    print("final result:",list_up_words)
    return list_up_words


#---------------------------------------------------------------------------------------------------

def check(event):
    # get text from entry
    input_word = event.widget.get()
    input_word = input_word.strip().lower()
    list_test=search('data1.txt',input_word)

    # get data from test_list
    if input_word == '':
        data_list = list_test
    else:
        data_list = []
        for item in list_test:
            if input_word in item.lower():
                data_list.append(item)

                # update data in listbox
    update(data_list)


def update(data):
    # delete previous data
    listbox.delete(0, 'end')


    # put new data
    for item in data:
        listbox.insert('end', item)


def fillout(event):
    # display element selected on list
    print('previous:', event.widget.get('active'))
    selected=event.widget.get(event.widget.curselection())
    print(selected)
    print('---')





test_list=[]
entry = tk.Entry(root)
entry.pack()
entry.bind('<KeyRelease>', check)
listbox = tk.Listbox(root)
listbox.pack()
listbox.bind('<<ListboxSelect>>', fillout)
update(test_list)
root.mainloop()

######################################################################
# name = tk.StringVar()
#
# def main():
#     out = name_entry.get()
#     result['text']=search("data.txt",out)
#
# name_label = tk.Label(root, text='Enter Word', font=('calibre', 10, 'bold'))
# space = tk.Label(root, text='\n', font=('calibre', 10, 'bold'))
# space1 = tk.Label(root, text='\n', font=('calibre', 10, 'bold'))
# result=tk.Label(root,text='',font=('calibre', 10, 'bold'))
# name_entry = tk.Entry(root, textvariable=name, font=('calibre', 10, 'normal'))
#
#
# sub_btn = tk.Button(root, text='Result', command=main)
#
#
# name_label.grid(row=0, column=0)
# name_entry.grid(row=0, column=1)
# space.grid(row=1,column=1)
# space1.grid(row=2,column=1)
# result.grid(row=1,column=1)
# sub_btn.grid(row=4, column=1)
#
# root.mainloop()