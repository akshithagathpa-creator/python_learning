#library management system

books_available = ["python basics", "machine learning", "data science", "AI for begginers"]

borrowed_books = []

print("----books available----")

for i in range(len(books_available)):
    print(books_available[i])
while True:
    book = input("\nenter the books do you wanna borrow(pr type 'done' when over): ").lower()
    if book == "done":
        break
    if book not in books_available:
        print("books not available!")
        continue
    borrowed_books.append(book)


print("\n----final list of books borrowed-----")
count = 1
for book in borrowed_books:
        print(count, '-',book)
        count += 1

