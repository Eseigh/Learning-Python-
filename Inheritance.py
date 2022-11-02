class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def birthday(self):
        print('Happy birthday you were', self.age)
        self.age += 1
        print('You are now', self.age)
    def __str__(self):
        return self.name + ' is ' + str(self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay
    def __str__(self):
        return super().__str__() + ' - id(' + str(self.id) + ')'

class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sales):
        super().__init__(name, age, id)
        self.region = region
        self.sales = sales
    def bonus(self):
        return self.sales * 0.5

print('Person')
p = Person('John', 54)
print(p)
p.birthday()
print(p.name)
print(p.age)
print('-' * 25)

print('Employee')
e = Employee('Denise', 51, 7468)
print(e)
e.birthday()
print(e.name)
print(e.age)
print(e.id)
print('e.calculate_pay(40):', e.calculate_pay(40))
print('-' * 25)

print('SalesPerson')
s = SalesPerson('Phoebe', 21, 4712, 'UK', 30000.0)
s.birthday()
print('s.calculate_pay(40):', s.calculate_pay(40))
print('s.bonus():', s.bonus())
# {"threads":[{"position":0,"start":0,"end":712,"connection":"open"},{"position":1424,"start":713,"end":1424,"connection":"closed"}],"url":"https://att-c.udemycdn.com/2022-06-01_04-37-11-725e0020d0f90d00d83ffb7585a5ed31/original.py?response-content-disposition=attachment%3B+filename%3DInheritance.py&Expires=1654197940&Signature=AIoDpW4OQONLwh2XrDSNZqStATT4xAvt~A5eK2Lk4Nz0iJCD~~A-n-YC8naW4OMC78pb7BFZLljsa2NkPVjjt~pReSLfFEeDP-HlJT2aidE~wZFKO8nXoBLIN3myk2cYzcIIySw0lZ8nf8sNeqpB1v8YlLAbWxPVYwNZsA69JgffwUt8Wfwslx3rL01HwZeCg~EGHuBVs-V9VGWbSiXXI83m21JYpCMaAaIcjAsEqXBSAS-6uFL4gcitWRlHWVK3aYrcrg4FnI8-Tptc1KUzpXUdC55R4fjCgcXvISxp8CYycVUg996-XM0YPWM6R4S6huY7gqWb~zbjv85RDaefVg__&Key-Pair-Id=APKAITJV77WS5ZT7262A","method":"GET","port":443,"downloadSize":1424,"headers":{"content-type":"text/x-python","content-length":"1424","connection":"close","date":"Thu, 02 Jun 2022 14:57:39 GMT","last-modified":"Wed, 01 Jun 2022 04:37:12 GMT","etag":"\"96383ca7f40d2295ef1f14ce11429909\"","x-amz-server-side-encryption":"AES256","x-amz-meta-qqfilename":"Inheritance.py","x-amz-version-id":"c6c3q2GVxXm7Iw8vLZx4WwsiS3CvtJcU","content-disposition":"attachment; filename=Inheritance.py","accept-ranges":"bytes","server":"AmazonS3","x-cache":"Miss from cloudfront","via":"1.1 6d424430e2badcd8859fea1f1185697a.cloudfront.net (CloudFront)","x-amz-cf-pop":"AMS1-C1","x-amz-cf-id":"9Wjs35UcDA_sL2VmsAq7H3n7qT32ESRIeDBtDpew_PBRyfG6muTKPg=="}}