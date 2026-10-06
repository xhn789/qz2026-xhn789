import json 
# filepath = "C:/qz2026-xhn789/q1/test.jsonl"
def analyze_log(filepath:str) -> dict:
    total=0
    by_level = {}
    by_user = {}
    last_error = None
    result = {"total":total,"by_level":by_level,"by_user":by_user,"last_error":last_error}
    try:
        with open(filepath,"r",encoding="utf-8") as f:
            for line in f:
                try:
                    line = json.loads(line)
                except:
                    continue
                else:
                    #读取和获得想要数据
                    try:
                        level = line["level"]
                        user = line["user"]
                       
                        if line["level"] == "ERROR":
                            last_error = line["message"]
                    except:
                        continue
                    else:
                        by_level[level] = by_level.get(level,0) + 1
                        by_user[user] = by_user.get(user,0) + 1
                        total += 1 
    #文件未找到时
    except FileNotFoundError:
        return result
    else:
        result["total"] = total
        result["by_level"] = by_level
        result["by_user"] = by_user
        result["last_error"] = last_error
        return result
            
# result = analyze_log(filepath)
# print(result["total"])        # 5
# print(result["by_level"])     # {'INFO': 3, 'ERROR': 2}
# print(result["by_user"])      # {'张三': 2, '李四': 2, '王五': 1}
# print(result["last_error"])   # 超时

# result = analyze_log("C:/qz2026-xhn789/q1/test_empty.jsonl")
# print(result)

# result = analyze_log("C:\\qz2026-xhn789\\q1\\text_wrong.jsonl")
# print(result)