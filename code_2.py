
def property():
    evidence = 'Religious particular concern hear somebody arm wall.'
    evidence_length = len(evidence)
    evidence_words = evidence.split()
    evidence_count = len(evidence_words)
    evidence_number = 13

    for word in evidence_words:
        print("Word:", word)

    print("String:", evidence)
    print("String Length:", evidence_length)
    print("Number:", evidence_number)
    print("Word Count:", evidence_count)

if __name__ == "__main__":
    property()
