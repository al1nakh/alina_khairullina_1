#1
def analyze_text(text):
    clean_text = ""
    for i in text.lower():
        if i.isalpha() or i == " ":
            clean_text += i
    vowels = "aeiouy"
    unique_vowels = ""
    for i in clean_text:
        if i in vowels and i not in unique_vowels:
            unique_vowels += i
    vowel_count = len(unique_vowels)
    words = clean_text.split()
    result_words = ""
    seen = ""
    for i in words:
        if len(i) >= 5:
            if i[0] == i[-1]:
                if i not in seen :
                    result_words += i + " "
                    seen += i + " "

    return(vowel_count,result_words.strip())
print(analyze_text("your level is high"))
#-------------------------------------

#2


