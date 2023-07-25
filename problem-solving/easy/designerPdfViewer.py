def designerPdfViewer(h, word):
    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z'
    ]

    heights = []
    for ch in word:
        heights.append(h[letters.index(ch)])

    return max(heights)*len(word)
    


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = 'abc'
print(designerPdfViewer(h, word))
