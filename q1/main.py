import json 
filepath = "C:/qz2026-xhn789/q1/test.jsonl"
def analyze_log(filepath:str) -> dict:
    with open(filepath,"r",encoding="utf-8") as f:
        total=0
        by_level = {}
        by_user = {}
        back_dict = {}
        last_error = None
        result = {}

        for line in f:
            try :
                line = json.loads(line)
                #读取和获得想要数据
                total += 1 
                level = line["level"]
                user = line["user"]
                by_level[level] = by_level.get(level,0) + 1
                by_user[user] = by_user.get(user,0) + 1
                if line["level"] == "ERROR":
                    last_error = line["message"]

                result["total"] = total
                result["by_level"] = by_level
                result["by_user"] = by_user
                result["last_error"] = last_error
            
               


            except :
                continue
            
        return result    
            


result = analyze_log(filepath)
print(result["total"])        # 5
print(result["by_level"])     # {'INFO': 3, 'ERROR': 2}
print(result["by_user"])      # {'张三': 2, '李四': 2, '王五': 1}
print(result["last_error"])   # 超时


