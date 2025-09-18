import random

test_random = random.randint(1,20)

print(" *** เกมทายใจคอมพิวเตอร์ ***")
print(" *** ทายจำนวนเต็มตั้งแต่ 1-20 ***")
print(" *** มีโอกาส 6 ครั้ง ***")

for i in rang(6):

    print(f"ความพยายามครั้งที่{i+1}")
    guess_number = int(input("What is your guess number?:"))

if test_random == guess_number:
    print("เก่งจางเรย เดาถูกได้ไง เก่งอ่า")

elif guess_number < test_random :
    print("ผิดครับพี่ห์ มากกว่านี้")

elif guess_number > test_random:
    print("ผิดครับพีห์ ลดลงอีก")

def test_random():
    random_number = random.radint(1,100)
    print(random_number)

test_random()