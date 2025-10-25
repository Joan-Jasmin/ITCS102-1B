list = []
print("+ MY ANIME LIST +")
while True:
    anime = input("Give Anime (Type 'thanks' to end): ")
    if anime.lower()== 'thanks':
        print("THANK YOU FOR LISTING!")
        break
    list.append(anime)
num = len(list)
print("My List:")
for J in range(1,num+1,1):
    print(f'- {list[J-1]}')
print("Nice takes buddy.")