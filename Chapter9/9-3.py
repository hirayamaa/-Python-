import shelve

shelve_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelve_file['cats'] = cats
shelve_file.close()

shelve_file = shelve.open('mydata')
print(shelve_file['cats'])
shelve_file.close()
