import numpy as np
import pandas as pd

class AccountInfo:
    def __init__(self):
        self.database = 'data/people_data.csv'
        self.data = pd.read_csv(self.database)
        
    def create_account(self, ID, name, surname='', birthday='', interests='', wishlist='', friendlist=''):
        id_list = self.data.ID.tolist()
        if ID in id_list:
            print('User ID: ', ID, 'already in the database')
            print(type(self.data['ID']==ID))
            print(self.data[self.data['ID']==ID])
            return -1
        else:
            if name == '':
                print('Name cannot be empty')
                return -1
            else:
                account_dict = {
                    'ID': ID,
                    'Name': name,
                    'Surname': surname,
                    'Birthday': birthday,
                    'Interests': interests,
                    'WishList': wishlist,
                    'FriendList': friendlist
                }
                self.data = self.data.append(account_dict, ignore_index=True)
                self.data.to_csv(self.database, index=False)
                print('Account created successfully!')
        return self.data
    
    def update_account(self, ID, name='', surname='', birthday='', interests='', wishlist='', friendlist=''):
        id_list = self.data.ID.tolist()
        if ID not in id_list:
            print('User ID:', ID, 'is not in the database!!!')
            return -1
        else:
            data = self.data[self.data['ID']==ID]
            if name=='':
                name = data.Name.values[0]
            if surname=='':
                surname = data.Surname.values[0]
            if birthday=='':
                birthday = data.Birthday.values[0]
            if interests=='':
                interests = data.Interests.values[0]
            if wishlist=='':
                wishlist = data.WishList.values[0]
            if friendlist=='':
                friendlist = data.FriendList.values[0]
            account_dict = {
                'ID': ID,
                'Name': name,
                'Surname': surname,
                'Birthday': birthday,
                'Interests': interests,
                'WishList': wishlist,
                'FriendList': friendlist
            }
            index = self.data[self.data['ID']==ID].index[0]
            self.data.at[index, 'WishList'] = account_dict
            self.data.to_csv(self.database, index=False)
            print('Account updated successfully!')
        return self.data
    
    def get_database(self):
        return self.data
    
    def delete_account(self, ID):
        id_list = self.data.ID.tolist()
        if ID not in id_list:
            print('Invalid ID, please enter valid ID.')
            return -1
        else:
            matched_data = self.data[self.data['ID']==ID]
            self.data = self.data.drop(matched_data.index)
            print('Account deleted successfully!')
            self.data.to_csv(self.database, index=False)
        return self.data
    
    def get_info(self, ID):
        id_list = self.data.ID.tolist()
        if ID not in id_list:
            print('Invalid ID, please enter valid ID.')
            return -1
        else:
            return self.data[self.data['ID']==ID]
        
    def search_ID(self, ID):
        if ID == None:
            print("ID cannot be empty!!!")
            return [0], -1
        ID_result = self.data[self.data['ID']==ID]
        if ID_result.values.size == 0:
            print("ID not found! Try ID ranges from 0 to 10.")
            return [0], -1
        return ID_result, True
        
    def get_name(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][1]
    
    def get_surname(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][2]
        
    def get_birthday(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][3]
    
    def get_interests(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][4]
        
    def get_wishlist(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][5]
        
    def add_wishlist(self, ID, items):
        flag = 1
        wl_str = self.get_wishlist(ID)
        if str(wl_str)=='nan':
            wl_str = []
        else:
            wl_str = wl_str.replace('"','')
            wl_str = wl_str.split(', ')
        for _item in items:
            if str(_item) in wl_str:
                print('Item ID:', _item, 'is already in the wishlist!!!')
                flag = 0
            else:
                wl_str.append(str(_item))
                print('Item ID:', _item, 'is added successfully!!!')
        wl_str = ', '.join(i for i in wl_str)
        wl_str = '"' + wl_str + '"'
        index = self.data[self.data['ID']==ID].index[0]
        self.data.at[index, 'WishList'] = wl_str
        self.data.to_csv(self.database, index=False)
        return self.data
    
    def delete_wishlist(self, ID, items):
        flag = 1
        wl_str = self.get_wishlist(ID)
        if str(wl_str)=='nan':
            wl_str = []
        else:
            wl_str = wl_str.replace('"','')
            wl_str = wl_str.split(', ')
        for _item in items:
            if str(_item) in wl_str:
                if len(wl_str):
                    print('There are no items in the wishlist!!!')
                    flag = 0
                else:
                    wl_str.remove(str(_item))
                    print('Item ID:', _item, 'is removed successfully!!!')
            else:
                print('Item ID:', _item, 'is not found in the wishlist!!!')
        wl_str = ', '.join(i for i in wl_str)
        wl_str = '"' + wl_str + '"'
        index = self.data[self.data['ID']==ID].index[0]
        self.data.at[index, 'WishList'] = wl_str
        self.data.to_csv(self.database, index=False)
        return self.data
        
    def get_friendlist(self, ID):
        result, flag = self.search_ID(ID)
        if flag == False:
            return False
        else:
            result_dict = result.values
            return result_dict[0][6]