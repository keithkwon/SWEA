#pow()


data_list=[1, 2, 3, 4, 5]

print("pow({0}, 2) => {1}".format(data_list[2],pow(data_list[2],2)))

print("list(map(lambda x:pow(x, 2), {0}))=>{1}".format(data_list, list(map(lambda x:pow(x,2), data_list))))