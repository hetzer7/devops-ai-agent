from search import Search

search = Search()

results = search.search("오늘 김포 날씨")

for r in results:

    print("=" * 50)

    print(r["title"])

    print(r["href"])

    print(r["body"])
