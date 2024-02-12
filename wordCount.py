from sys import argv
# 在命令提示字元中，利用python去執行可以匯出所有提到檔案或名詞的list
if len(argv) > 2:
    print("請選取文件。。。")
else:
    file = open(argv[1])  # open是python內建的function，用來開啟指定檔案
    lines = file.read()  # 讀取檔案內容，並以string格式輸出
    lines = lines.split("\n")  # 將文件內容以分行分割，並輸出一個新的list
    wordCount = 0
    letterCount = 0
    for line in lines:
        words = line.split(" ")
        wordCount += len(words)
        letterCount += len(line)
    lineCount = len(lines)  # 計算list長度即可得到文件行數
    print(f"總行數是{lineCount}，總單字數是{wordCount}，總字數是{letterCount}")
