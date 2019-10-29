import string
def kaisa(s,k):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    before=string.ascii_letters
    after=lower[k:] +lower[:k] +upper[k:] +upper[:k]
    table=''.maketrans(before,after)
    return s.translate(table)
s="Python is a great programming language.I like it ！"
print(kaisa(s,3))
s='If the implementation is easy to explain,it may be a good idea.'
print(kaisa(s,3))
