from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='**/*',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()  # docs = loader.load()

for document in docs:
    print(document.metadata)