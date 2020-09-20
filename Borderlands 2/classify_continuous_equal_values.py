# -*- coding: utf-8 -*-
"""
Created on Thu May 28 03:19:13 2020

@author: ran
"""

import numpy as np
import pandas as pd

"""
어떤 값들 안에 연속하여 동일한 값들을 정수그룹으로 표시하는 방법에 대한 생각

예를 들어 
input : [0, 0, 1, 1, 0, 0, 1, 0] 을
output: [1, 1, 2, 2, 3, 3, 4, 5] 로 표시

여기서 input의 값은 0, 1 만으로 제한되지 않고 어떤 값이든 가능

예를 들어
input : [1, 1, 6, 6, 6, 2, 2, 2, 1, 6, 2, 2] 를
output: [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6] 로 표시

해법:
    동일값이 연속한다는 조건때문에 현재 원소의 연속 여부는 전 원소에 의존한다. 
    따라서 loop를 이용한다면 쉽게 분류가 가능하다. 그러나 여기서는 
    loop를 사용하지 않고 벡터 연산을 통해 해결하고 싶다.
    
    pandas에 이 문제를 쉽게 해결하는 메서드나 함수가 있는지 살펴보았으나 아직
    발견하지 못했다.
"""


# 먼저 loop를 이용하여 함수 구현
# -------------------------------------------------------------------
def grouping_conteq_vals(vals):
    """
    주의: vals는 sequence인데, 원소의 값으로 None은 허용되지 않는다.
    """
    group = []
    prev = None
    igrp = 1
    for curr in vals:
        if curr is None:
            raise ValueError('input sequence 원소값으로 None은 허용되지 않음')
        if (prev is not None) and (prev != curr):
            igrp += 1
        group.append(igrp)
        prev = curr
    return group

cases = [{'inp': [0, 0, 1, 1, 0, 0, 1, 0],
          'sol': [1, 1, 2, 2, 3, 3, 4, 5]},
         {'inp': [1, 1, 6, 6, 6, 2, 2, 2, 1, 6, 2, 2],
          'sol': [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]}
        ]

for case in cases:
    assert  case['sol'] == grouping_conteq_vals(case['inp'])


# 먼저 loop를 이용하여 함수 구현
# -------------------------------------------------------------------
se = pd.Series(cases[0]['inp'], name='inp')
preveq = se.shift().eq(se)
c = preveq.copy()
c[preveq == False] = range(1, sum(~preveq) + 1)
c[preveq] = np.nan
c = c.fillna(method='ffill').astype(int)


pd.concat([se, c], axis=1)


