m_of_2 = {2, 4, 6, 8, 10, 12, 14, 16}
m_of_3 = {3, 6, 9, 12, 15, 18, 21}

print(f'배타적 차집합 : {m_of_2.symmetric_difference(m_of_3)}')
print(f'배타적 차집합 : {m_of_2 ^ m_of_3}')