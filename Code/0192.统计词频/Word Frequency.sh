# Read from the file words.txt and output the word frequency list to stdout.

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'

# cat 用于查看word.txt
# tr -s ' ' '\n' 用于将空格替换成换行，每个词占一行
# sort 将分好的词排序
# uniq -c 统计重复次数（此步骤与上一步息息相关，-c原理是字符串相同则加一，如果不进行先排序的话将无法统计数目）
#sort -nr 将数目倒序排列
# awk '{print $2, $1}' 将词频和词语调换位置打印