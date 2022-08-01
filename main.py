def filter(text):
    replaced_text = text.replace("/", ".\n")
    replaced_text = replaced_text.replace('"', "")
    replaced_text = replaced_text.replace('"', "")
    replaced_text = replaced_text.replace('(', "'")
    replaced_text = replaced_text.replace('+', "*")
    replaced_text = replaced_text.replace('-', ",")
    replaced_text = replaced_text.replace('..', "--")
    return replaced_text

def caesar_cyph(text):
    deciphered = ""
    for i_smb in text:
        if i_smb in letters:
            search = letters.find(i_smb)
            deciphered += letters[search - 1]
        else:
            deciphered += i_smb
    return deciphered

def shift(text, key):
    word_ln = len(text)
    shift = key % word_ln
    text = text[-shift:] + text[:-shift]
    return text
# def find_key(text):   Жалкие попытки выбить ключ
#     word_key = "B"
#     count = 0
#     for i_word in text.split():
#         for j_smb in i_word:
#             if j_smb == word_key:
#                 i_word = i_word[-1:] + i_word[:-1]
#                 count += 1
#                 if i_word.startswith(word_key):
#                     break
#     return count

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/' \
       'dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/' \
       'ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/' \
       'qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/' \
       'hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /' \
       'ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /' \
       'jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()
# Как же я намучался с тем что просто не правильно расположил текст и после 6 строчки все ломалось

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
zen = []
key = 3

for i_word in text:
    text_wtht_csr = caesar_cyph(i_word)
    shift_text = shift(text_wtht_csr, key)
    if shift_text.endswith("/"):
        key += 1
        zen.append(shift_text)
    else:
        zen.append(shift_text)

zen = " ".join(zen)
zen_true = filter(zen)
print(zen_true)