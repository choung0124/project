with open("chang_yong_kang_extracted_text_korean_only.txt", "r") as f1:
    list1 = [str(x.strip()) for x in f1.read().split(',')]
    print(len(list1))

with open("Doctor_JUDY_닥터주디_피부과전문의_extracted_text_korean_only.txt", "r") as f1:
    list2= [str(x.strip()) for x in f1.read().split(',')]
    print(len(list2))

with open("교육하는_의사_extracted_text_korean_only.txt", "r") as f1:
    list3 = [str(x.strip()) for x in f1.read().split(',')]

with open("굿라이프_extracted_text_korean_only.txt", "r") as f1:
    list4 = [str(x.strip()) for x in f1.read().split(',')]

with open("김소형_채널_H_extracted_text_korean_only.txt", "r") as f1:
    list5 = [str(x.strip()) for x in f1.read().split(',')]

with open("다이어트한의사_쏘팟다이어트한의사_쏘팟_extracted_text_korean_only.txt", "r") as f1:
    list6 = [str(x.strip()) for x in f1.read().split(',')]

with open("닥터딩요_extracted_text_korean_only.txt", "r") as f1:
    list7 = [str(x.strip()) for x in f1.read().split(',')]

with open("닥터쓰리_extracted_text_korean_only.txt", "r") as f1:
    list8 = [str(x.strip()) for x in f1.read().split(',')]

with open("닥터프렌즈_extracted_text_korean_only.txt", "r") as f1:
    list9 = [str(x.strip()) for x in f1.read().split(',')]

with open("부산의사_김원장_extracted_text_korean_only.txt", "r") as f1:
    list10 = [str(x.strip()) for x in f1.read().split(',')]

with open("비온뒤_extracted_text_korean_only.txt", "r") as f1:
    list11 = [str(x.strip()) for x in f1.read().split(',')]

with open("산부인과_의사언니_extracted_text_korean_only.txt", "r") as f1:
    list12 = [str(x.strip()) for x in f1.read().split(',')]

with open("우리동네산부인과_extracted_text_korean_only.txt", "r") as f1:
    list13 = [str(x.strip()) for x in f1.read().split(',')]

with open("이재성_박사의_식탁보감_extracted_text_korean_only.txt", "r") as f1:
    list14 = [str(x.strip()) for x in f1.read().split(',')]

with open("장항준_내과_TVextracted_text_korean_only.txt", "r") as f1:
    list15 = [str(x.strip()) for x in f1.read().split(',')]

with open("정라레_Lifestyle Doctor_extracted_text_korean_only.txt", "r") as f1:
    list16 = [str(x.strip()) for x in f1.read().split(',')]

with open("정신과의사_정우열_extracted_text_korean_only.txt", "r") as f1:
    list17 = [str(x.strip()) for x in f1.read().split(',')]

with open("치과의사_매직박_의사_extracted_text_korean_only.txt", "r") as f1:
    list18 = [str(x.strip()) for x in f1.read().split(',')]

with open("치대남_치대나온남자_extracted_text_korean_only.txt", "r") as f1:
    list19 = [str(x.strip()) for x in f1.read().split(',')]

combined_list = list1 + list2 + list3 + list4 + list5 + list6 +list7 + list8 + list9 + list10 + list11 + list12 + list13 + list14+ list15 + list16 + list17 + list18 + list19

#print(combined_list)
print(len(combined_list))

with open("extracted_text_korean_only.txt", "w") as file:
    file.write(','.join(combined_list))
