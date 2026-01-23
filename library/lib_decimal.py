from decimal import Decimal

dec_1 = 0.1 + 0.1 + 0.1 - 0.3
print(dec_1)

dec_2 = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(dec_2)

#! Decimal Context Manager