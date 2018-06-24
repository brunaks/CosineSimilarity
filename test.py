import cosine_similarity

documents = list()

for file_number in range(1, 4):
    filename = "Text" + str(0) + str(file_number) + ".txt";
    document = "";
    document = open(filename,"r").readlines();

    documents.extend(document);

documentsToProcess = tuple(documents)
print documentsToProcess;

#Always compares the first text to the others
print "Cosine similarity:"
cosine_similarity.calculate_cosine_similarity(documentsToProcess);

#print "Jaccard similarity:"
#cosine_similarity.calculate_jaccard_similarity(documentsToProcess)

#print "Euclidean similarity:"
#cosine_similarity.calculate_euclidean_similarity(documentsToProcess);


