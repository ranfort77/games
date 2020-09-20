# -*- coding: utf-8 -*-
"""
Created on Tue May 26 01:35:38 2020

@author: ran

성과:

TODO:
    1. 데이터 전처리 단계의 itemid 추가에 대해 method chaining으로 
       더 간단히 처리하는 방법은 없나?
"""

import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)

"""데이터 전처리 단계:
현재 Borderlands2_data.xlsx에 정리된 테이블은 두 가지 정보가 혼합되어 있다.
첫 번째는 파밍 데이터로,
  id_vars가 Date, class, classLevel, RoomNumber이고 value가 Equip인 테이블이고, 두 번째는 Equip가 NA가 아닐 때 
두 번째는 아이템 데이터로,
  Equip가 NA가 아닐 때 획득한 regendary item 테이블이다.   

두 테이블로 분리하기 전에 각각의 Treasure Room에서 얻은 regendary item의 
itemid 열을 추가한다. itemid는 순서대로 1부터 번호가 할당되며, Equip가 NA이면 
0를 할당한다. itemid는 파밍 데이터의 외래키가 된다.
"""
# 데이터 로드 및 itemid 추가
rawdf = pd.read_excel('Borderlands2_data.xlsx').assign(itemid = 0) 
idx = rawdf['Equip'].notna()
rawdf.loc[idx, 'itemid'] = range(1, idx.sum() + 1)
# 파밍 테이블과 아이템 테이블로 분리
farms = rawdf.reindex(columns=['Date', 'Class', 'ClassLevel', 
                               'RoomNumber', 'Equip', 'itemid'])
items = (rawdf.reindex(columns=['itemid', 'Equip', 'ItemLevel', 'Name',
                               'SpecialOption', 'Elemental', 'Manufacturer'])
              .dropna(subset=['Equip']))


"""분석 단계:
정리한 테이블로 부터 알고 싶은 것들은 아래와 같다.
  1. 총 몇 번의 Treasure Room을 털었고, legendary item이 나온 Room은 몇 번인가?
     Room에서 최소 하나의 legendary item이 나올 확률이 얼마인가?
     한 Room에서 2개 이상의 legendary item이 나왔는가?
  2. 연속해서 legendary item이 안나온 Room의 회수를 내림차순으로 출력
"""
# RoomNumber 열은 한 방에서 두 개의 legendary item이 나온 경우 때문에 중복이 있다.
# 따라서 value_counts로 중복을 처리해 준다.
allRoomNums = (farms['RoomNumber'].value_counts().sort_index()
               .rename('allRooms'))
scsRoomNums = (farms[farms['Equip'].notna()]['RoomNumber'].value_counts()
               .sort_index().rename('successRooms'))
# 한 방에 두 개 또는 현재는 없지만 세 개 또는 n 개의 legendary item이 나온적이
# 있는지 카운팅
multiscsRoomNums = (scsRoomNums[scsRoomNums >= 2].value_counts()
      .rename_axis(index='legendItemsInOneRoom').rename('numberOfRooms')
      .reset_index())

# 출력 메세지
print('전체 파밍한 방 수: {} 번'.format(allRoomNums.size))
print('전설템 발견 방 수: {} 번'.format(scsRoomNums.size))
print('최소 하나의 전설템 나올 확률: {:.0f}%'.format(scsRoomNums.size / allRoomNums.size * 100))
templet = lambda row: '한 방에서 {}개 전설템이 나온 방 수: {} 번'.format(*row)
multiscsRoomNums.apply(templet, axis=1).map(print)


# df = farms.assign(nan = farms.Equip.isna()).reindex(columns=['RoomNumber', 'Equip', 'nan'])
# df['section'] = df.nan.sub(df.nan.shift(), fill_value=0)
# df.nan.map()



