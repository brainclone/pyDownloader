import wget

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
dir = 'files'
bar_type = wget.bar_thermometer

print ('Downloading ' + url +' ...')
filename = wget.download(url, out = dir, bar = bar_type)
print ('\nDownloaded to ' + filename)
