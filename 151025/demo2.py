class Music:
    def __init__(self, name="", like="", unlike=""):
        self.name = name
        self.like = like
        self.unlike = unlike

    def listen(self, song=""):
        if song.lower() == self.like.lower():
            print(f"{self.name} đang nghe bài hát {song} và rất thích nó.")
        else:
            print(f"{self.name} đang nghe bài hát {song} và không thích nó.")


list_music = []


def init():
    list_music.append(Music("Quân", "Cháu lên bar", "Con cò bé bé"))
    list_music.append(Music("An", "Cơn mưa ngang qua", "Em đi học"))
    list_music.append(Music("Dũng", "Con cò bé bé", "Cháu lên bar"))


def find():
    song = input("Nhap ten bai hat")
    for m in list_music:
        m.listen(song)


def menu():
    while True:
        print("1.Khởi tạo danh sách")
        print("2.Tìm bài hát")
        print("3.Thoát")

        chon = input("Bạn chọn 1/2/3: ")
        if chon == "1":
            init()
        elif chon == "2":
            find()
        elif chon == "3":
            return
        else:
            print("Bạn chọn sai mời chọn lại")


if __name__ == "__main__":
    menu()
