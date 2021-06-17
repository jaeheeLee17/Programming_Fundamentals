def find_first(filename, key):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    pos = text.find(key)
    if pos == -1:
        outfile.write(key + " is not found.\n")
    else:
        outfile.write("{} is at {}.\n".format(key, str(pos)))
    outfile.close()
    infile.close()
    print("done")

def find_second(filename, key):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    pos = text.find(key)
    pos = text.find(key, pos + 1)
    if pos == -1:
        outfile.write(key + " is not found.\n")
    else:
        outfile.write("{} is at {}.\n".format(key, str(pos)))
    outfile.close()
    infile.close()
    print("done")

def find_last(filename, key):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    pos = text.rfind(key)
    if pos == -1:
        outfile.write(key + " is not found.\n")
    else:
        outfile.write("{} is at {}.\n".format(key, str(pos)))
    outfile.close()
    infile.close()
    print("done")

def find_all(filename, key):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    pos = text.find(key)
    outfile.write("{} is at {}.\n".format(key, str(pos)))
    while True:
        if pos == -1:
            outfile.write(key + " is not found.\n")
            break
        else:
            pos = text.find(key, pos + 1)
            if pos == -1:
                break
            outfile.write("{} is at {}.\n".format(key, str(pos)))
    outfile.close()
    infile.close()
    print("done")

def find_all_count(filename, key):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    count = 0
    pos = text.find(key)
    outfile.write("{} is at {}.\n".format(key, str(pos)))
    while True:
        if pos == -1:
            outfile.write(key + " is not found.\n")
            break
        else:
            count += 1
            pos = text.find(key, pos + 1)
            if pos == -1:
                break
            outfile.write("{} is at {}.\n".format(key, str(pos)))
    outfile.write("\nAppeared {} times in total.\n".format(count))
    outfile.close()
    infile.close()
    print("done")

def one_sentence_per_line(filename):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    count = 0

    while True:
        pos1 = text.find('.')
        pos2 = text.find('?')
        if pos1 == -1 and pos2 == -1:
            break
        elif pos1 == -1:
            text_list = text.partition(text[pos2])
        elif pos2 == -1:
            text_list = text.partition(text[pos1])
        elif pos1 <= pos2:
            text_list = text.partition(text[pos1])
        else:
            text_list = text.partition(text[pos2])
        outfile.write(text_list[0] + text_list[1] + "\n")
        count += 1
        text = text_list[2]

    outfile.write("\n{} sentences in total.\n".format(str(count)))
    outfile.close()
    infile.close()
    print("done")

def find_all_sentence(filename, key):
    infile = open(filename, "r")
    outfile = open("result.txt", "w")
    text = infile.read()
    total_key_cnt, sentence_cnt = 0, 0
    while True:
        pos1 = text.find('.')
        pos2 = text.find('?')
        if pos1 == -1 and pos2 == -1:
            break
        elif pos1 == -1:
            text_list = text.partition(text[pos2])
        elif pos2 == -1:
            text_list = text.partition(text[pos1])
        elif pos1 <= pos2:
            text_list = text.partition(text[pos1])
        else:
            text_list = text.partition(text[pos2])
        sentence = text_list[0] + text_list[1]
        word_cnt = sentence.count(key)
        if word_cnt >= 1:
            outfile.write('{} appeared {} times\n'.format(key, word_cnt))
            outfile.write(sentence + "\n\n")
            total_key_cnt += word_cnt
            sentence_cnt += 1
        text = text_list[2]

    outfile.write('\n{} appears {} times in {} sentences.\n'.format(key, total_key_cnt, sentence_cnt))
    outfile.close()
    infile.close()
    print("done")

# find_first("article.txt", "컴퓨터")
# find_first("article.txt", "세탁기")
# find_second("article.txt", "컴퓨터")
# find_first("article.txt", "데스크탑")
# find_second("article.txt", "데스크탑")
# find_last("article.txt", "컴퓨터")
# find_last("article.txt", "세탁기")
# find_last("article.txt", "데스크탑")
# find_all("article.txt", "컴퓨터")
# find_all("article.txt", "세탁기")
# find_all("article.txt", "데스크탑")
# find_all_count("article.txt", "컴퓨터")
# find_all_count("article.txt", "세탁기")
# find_all_count("article.txt", "데스크탑")
# one_sentence_per_line("article.txt")
# find_all_sentence("article.txt", "컴퓨터")
