directory = 'C:\\Users\\n219547\\OneDrive - Santander Office 365\\Documenti\\RepositoryGIT\\DWH-SantanderConsumerBank\\80 Python\\0 Formazione\\Corso Linkedin Fondamenti oltre fondamenti\\'

# Directory non necessaria se nelle impostazioni 
# cerco 'python execute'
# e metto il flag su "execute file into the script directory"
infile = open('values.txt','rt')
outfile = open('values_output.txt','wt')

print('Processing file..')
sum = 0
for line in infile:
    sum += 1
    print(line.rstrip(), file=outfile)
print('\nTotal: ' + str(sum), file=outfile)
print('\nTotal: ' + str(sum))

outfile.close()
print('Output complete')