# print(str(1234), end=', ')
# print(str(3.14), end=', ')
# print(str(['seoul', 'osan', 'suwon']), end=', ')
# print(str('korea'))
# # 1234, 3.14, ['seoul', 'osan', 'suwon'], korea
#
# print(repr(1234), end=', ')
# print(repr(3.14), end=', ')
# print(repr(['seoul', 'osan', 'suwon']), end=', ')
# print(repr('korea'))
# # 1234, 3.14, ['seoul', 'osan', 'suwon'], 'korea'
#
#
intexp = repr(1234)
intvalue = eval(intexp)
print(intvalue)

strexp = repr('korea')
strvalue = eval(strexp)
print(strexp)