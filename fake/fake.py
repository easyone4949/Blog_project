from faker import Faker

myfake = Faker()

# Faker의 메소드를 통해 어떤 종류의 가짜데이터를 뽑아낼지 결정 가능
# myfake.seed(Seed번호)
# seed번호 = 각각의 가짜 데이터의 데이터번호

print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())
