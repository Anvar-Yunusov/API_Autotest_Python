from pages.yandex_disk_page import YandexDiskPage


def test_get_files_and_folders(login_and_get_token, logout):
    token = login_and_get_token
    yandex_disk_page = YandexDiskPage()
    response = yandex_disk_page.get_files_and_folders(token)
    assert response.status_code == 200, "Не удалось получить список папок и файлов в аккаунте Яндекс диска"
    data = response.json()

    list_file_names = []

    for name_file in data["items"]:
        list_file_names.append(name_file["name"])

    list_folder_names = []

    for folder_file in data["items"]:
        string_a = folder_file["path"]
        first_slash_index = string_a.find('/')
        second_slash_index = string_a.find('/', first_slash_index + 1)
        if first_slash_index != -1 and second_slash_index != -1:
            word_between_slashes = string_a[first_slash_index + 1:second_slash_index]
            list_folder_names.append(word_between_slashes)

    print(f"Список папок: {list_folder_names} \nСписок файлов: {list_file_names}")

