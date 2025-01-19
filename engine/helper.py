import re

def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None

def remove_words(input_String,words_to_remove):
    words=input_String.split()
    # removes unwanted words
    filtered_words=[word for word in words if word.lower() not in words_to_remove]

    result_string=' '.join(filtered_words)
    return result_string


# example
# input_String="make a phone call to amma"

# words_to_remove=['make','a','to','call','send','message','whatsapp','']
# result=remove_words(input_String,words_to_remove)
# print(result)