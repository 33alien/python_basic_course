# # # def outer_func(x):
# # #     def inner_func(y):
# # #         return y / x
# # #     return inner_func
# # #
# # #
# # # # output = outer_func(5)
# # # print(outer_func(50)(200))
# #
# #
# m = map(lambda x: f"Mark {x}", [8, 21, 56, 32])
# print(m)
# print(type(m))
# for el in m:
#     print(el)
#     print(list(m))
#
#
# # s = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x), reverse=True)
# # print(s)
#
# d = {}
# l = []
#
# for i in range(5):
#     d["name"] = f"Andrey {i}"
#     l.append(d)
#
# print(l)

d = defaultdict(int)
with open("examples.txt") as f:
    for line in f:
        words = line.split(" ")
        for word in words:
            w = word.strip(",\n ")
            d[w] +=1

print(d)