import json

class UserManager():
    def __init__(self):
        self.users = {}
        #添加用户
    def add_user(self,name,age):
        id = 0
        id_max = 0
        for id in self.users:
            if id > id_max:
                id_max = id
        id_max += 1
        self.users[id_max] = {"id":id_max,"name":name,"age":age}
        # print(self.users[id_max])
        return self.users[id_max]
        #查询用户
    def get_user(self,user_id):
        if user_id in self.users:
            # print(self.users[user_id])
            return self.users[user_id]
        else:
            #print("None")
           return None
        #修改指定用户年龄
    def update_age(self,id,age):
        if id in self.users:
            self.users[id]["age"] = age
            # print("True")
            return True
        else:
            # print("False")
            return False
        #删除指定用户
    def remove_user(self,id):
        if id in self.users:
            del self.users[id]
            # print("Ture")
            return True
        else:
            # print("False")
            return False
        #列出所有用户
    def list_user(self):
        self.all_users =[]
        for id in self.users:
            self.all_users.append(self.users[id])
        print(self.all_users)    






        
    




um = UserManager()
um.add_user("张三", 18) 
um.add_user("李四", 20)
um.get_user(1)  
um.get_user(99)
um.update_age(1,19)
um.remove_user(2)
um.remove_user(2)
um.list_user()


