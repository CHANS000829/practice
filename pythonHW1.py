# 파이썬 기초 과제 

import pandas as pd 
# 1- 

# 1

pd.read_csv(r"C:\Users\baesa\Downloads\1.01.house.price.csv")

# 2 

df_house=pd.read_csv(r"C:\Users\baesa\Downloads\1.01.house.price.csv")

# 3
print(df_house.iloc[0,:], len(df_house))

# 4
print(type(df_house.iloc[0,3]))

# 5, 6

try:
    df_house=pd.read_csv(r"C:\Users\baesa\Downloads\1.01.house.price.csv")
    print(df_house.iloc[0,:], len(df_house))
    print(type(df_house.iloc[0,3]))

except FileNotFoundError:
    print("파일명과 업로드 여부를 확인하세요")


# 실행시

# 정상

#PS C:\Users\baesa\python-study> & 'C:\Users\baesa\AppData\Local\Programs\Python\Python313\python.exe' 'c:/Users/baesa/python-study/pythonHW1.py'
#ID        1.0
#size     34.0
#year      5.0
#price     5.0
#Name: 0, dtype: float64 10
#<class 'numpy.float64'> 


# 실패 

#PS C:\Users\baesa\python-study> & 'C:\Users\baesa\AppData\Local\Programs\Python\Python313\python.exe' 'c:/Users/baesa/python-study/pythonHW1.py'
#파일명과 업로드 여부를 확인하세요




# 1 - 2 

# 1 

houses = []

# 2 

for i in range(len(df_house)):
    df_house.iloc[i,:]


# 3 

for i in range(len(df_house)):
    ch_id = int(df_house['ID'].iloc[i])
    ch_size = int(df_house["size"].iloc[i])
    ch_year = int(df_house['year'].iloc[i])
    ch_price = float(df_house['price'].iloc[i])
    houses.append([ch_id,ch_size,ch_year,ch_price])

print(houses)


# 4, 5

successcount = 0
failcount = 0

for i in range(len(df_house)):
    try:
        if pd.isna(df_house['ID'].iloc[i]):
            print(i, "번째 행 제외 사유: ID값 누락")
            failcount+=1
            continue
        ch_id = int(df_house['ID'].iloc[i])
    

        if pd.isna(df_house["size"].iloc[i]):
            print(i, "번째 행 제외 사유: size값 누락")
            failcount+=1
            continue
        ch_size = int(df_house["size"].iloc[i])
        

        if pd.isna(df_house['year'].iloc[i]):
            print(i, "번째 행 제외 사유: year값 누락")
            failcount+=1
            continue
        ch_year = int(df_house['year'].iloc[i])
        
    
        if pd.isna(df_house['price'].iloc[i]):
            print(i,"번째 행 제외 사유: price값 누락")
            failcount+=1
            continue
        ch_price = float(df_house['price'].iloc[i])
        
        houses.append([ch_id, ch_size, ch_year, ch_price])
        successcount+=1

    
        
    
    except ValueError as e:
        failcount+=1
        print("에러 내용:", i, "행은 숫자로 변환할 수 없는 행")

print(successcount, failcount)






# 1 - 3 

# 1 

houses_test = houses.copy()

houses_test.extend([{"ID": 101, "year": 5, "price": 3},  # size 키 없음
{"ID": 102, "size": 35, "year": 5, "price": None},  # 값 없음
{"ID": 103, "size": "오류", "year": 5, "price": 3},  # 숫자로 변환할 수 없음
{"ID": 104, "size": 35, "year": 5, "price": 3}]) # 정상 데이터)


# 2, 3

for house in houses_test:

  if 'size' not in house:
    print("제외사유: size 키가 없습니다")
    continue

  if 'price' not in house:
    print("제외사유: price 키가 없습니다")
    continue

  if house['price'] is None:
    print("제외사유: 값이 없습니다")
    continue

  if house['size'] is None:
    print("제외사유: 값이 없습니다")
    continue
    
  try:
    int(house['size'])

  except ValueError as e:
    print("제외사유: 숫자로 변환할 수 없습니다")
    continue

  # 4 

for house in houses_test:
    if house['size']<=0 or house['price']<0:
      print(house, "->제외")
      continue


# 5 

selected = []

for house in houses_test:
   if (house['size']>=30) and (house['price']<=4):
      selected.append(house)
      
      
# 6

 
for house in selected:
   print(house['ID'])


# 7 

print(len(selected))





# 1- 4 

# 1, 2, 3
  
try:

    def unit_price(price,size):
        price=float(price)
        size=float(size)
        if (size <= 0) | (price<0):
            return None
        else: 
            return price / size

except:
    print("size가 0이하이거나 가격이 음수입니다.")


# 1- 4 

# 1, 2, 3

def unit_price(price, size):
    price = float(price)
    size = float(size)
    return price / size

# 4  
def unit_price(price, size):
   price = float(price)
   size = float(size)
   if (size<=0):
      print("크기가 0이하입니다.")
      return None
    if (price<0):
      print("가격이 음수입니다.")
      return None 

   return price/size


#5

def unit_price(price, size):
    try:
        price = float(price)
        size = float(size)

    except ValueError:
        print('값 오류: 숫자로 변환할 수 없는 문자열입니다.')
        return None

    if size<=0:
        print("크기가 0이하입니다.")
        return None
    if price<0:
        print("가격이 음수입니다")
        return None

    return price/size


# 6, 7, 9

def unit_price(price, size):
    try:
        price = float(price)
        size = float(size)

    except TypeError:
        print("자료형 오류: 숫자 또는 숫자 형태의 문자열을 입력하세요.")
        return None
    except ValueError:
        print('값 오류: 숫자로 변환할 수 없는 문자열입니다.')
        return None

    if size<=0:
        print("크기가 0이하입니다.")
        return None
    if price<0:
        print("가격이 음수입니다")
        return None

    return price/size



# 8
for house in houses:
   size_house = house[1]
   price_house = house[3]
   id_house = house[0]

   print(id_house, unit_price(price_house,size_house))




# 1-5 


# 1 
   
ID_NUM = []

for i in range(len(houses)):
   ID_NUM.append(houses[i][0])

print(ID_NUM)


# 2 

yeonsik = []

for i in range(len(houses)):
   yeonsik.append(houses[i][2])

yeonsik = list(set(yeonsik))
print(yeonsik)



# 3

ID_PRICE = {}

for i in houses:
    ID = i[0]
    PRICE = i[3]
    ID_PRICE[ID] = PRICE


# 4 

my_tuple = (30,4)

# 튜플을 선택한 이유는 생성 후 값이 바뀌면 안되는 고정된 기준값이기 때문이고, 리스트를 선택하지 않은 이유는 리스트는 생성 후에도 값을 변경/추가/삭제할 수 있어서 '변경 불가'라는 요구에 맞지 않기 때문이다 


# 5 

# 첫 번째 ID 리스트는 리스트를 선택한다. 
# 집이 저장된 원래 순서를 그대로 유지해야하고, ID가 여러번 나올 수 있으니 중복을 허용해야한다. 
# 집합과 차이: 집합은 순서를 보장하지 않고 중복도 자동으로 제거해버려서 원래 순서대로라는 요구와 맞지 않다


#두 번째 year 리스트는 집합을 선택한다
# 중복 없이 저장하는게 목적이고, 순서는 중요하지 않다. 집합은 중복을 자동으로 제거해주는 자료구조라 적합하다
# 리스트와 차이: 리스트는 중복을 그대로 허용하기 때문에, 별도로 중복 제거해야한다

#세 번째 ID_PRICE 조회는 딕셔너리를 선택한다
# ID라는 키를 가지고 price라는 값을 즉시 조회해야한다. 딕셔너리는 키를 통한 조회에 최적화된 자료구조라 적합하다
# 리스트와 차이: 리스트는 값을 가져오려면 인덱스를 알아야하거나 순서대로 찾아야한다

# 최소, 최대 묶음은 튜플을 선택한다
# 한번 정해지면 바뀌면 안되는 고정된 기준값이라, 생성 후 변경이 불가능한 자료구조가 필요하다 
# 리스트와 차이: 리스트는 생성 후에도 원소를 자유롭게 변경/추가/삭제할 수 있다 









    

