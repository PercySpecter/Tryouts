from urllib import request

source_url = "http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv"


def download(url):
    response = request.urlopen(url)
    data = str(response.read())
    lines = data.split("\\n")
    fw = open(r"test.csv" , "w")
    for l in lines:
        fw.write(l + "\n")
    fw.close()


download(source_url)
