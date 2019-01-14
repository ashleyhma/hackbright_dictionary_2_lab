"""Restaurant rating lister."""


# put your code here

def get_ratings(file_name):

    rating_file = open(file_name)

    rating_dict = {}

    for line in rating_file:
        line = line.strip()
        words = line.split(":")

        rating_dict[words[0]] = words[-1]

    # rating_list = list(rating_dict.items())
    # res_name = rating_list[0]
    # rating_num = rating_list[-1]

    for res_name, res_num in sorted(rating_dict.items()):

        print(res_name, "is rated at", res_num + ".")

get_ratings("scores.txt")



