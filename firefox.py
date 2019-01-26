import subprocess


def open_url(parameter):
    subprocess.Popen("firefox -new-tab " + (parameter['url']), stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)


def save(parameter):
    import json, lz4.block
    import time
    from credentials import connection
    print("Opened database successfully")

    string = (str(subprocess.check_output(['bash', 'path.sh'])).split("'")[1])[:-2]
    with open(string+"/recovery.jsonlz4", "rb") as read_file:
        magic = read_file.read(8)
        jdata = json.loads(lz4.block.decompress(read_file.read()).decode("utf-8"))
        nwin = 0
        for win in jdata.get("windows"):
            nwin += 1
            ntab = 0
            for tab in win.get("tabs"):
                ntab += 1
                i = tab.get("index") - 1
                urls = tab.get("entries")[i].get("url")
                print(urls)
                cur = connection.cursor()
                strr = 'INSERT INTO firefox (\"fileName\", \"windowNumber\", \"tabNumber\", \"URI\") VALUES (\'' + str(
                    parameter['saveFile']) + '\', ' + str(nwin) + ', ' + str(ntab) + ', \'' + urls + '\');'
                cur.execute(strr)
                connection.commit()
    time.sleep(1)
    print("Records created successfully")
    connection.close()

def load(parameter):
    import json
    from credentials import client
    result = client.execute('{firefox (where: {fileName: {_eq:\"' + parameter['saveFile'] + '\"}}){id windowNumber tabNumber timestamp URI }}')
    json_obj = json.loads(result)
    res = json_obj['data']
    for i in res['firefox']:
        parameter['url'] = i['URI']
        open_url(parameter)


def show(parameter):
    import json
    from credentials import client
    ans = []
    result = client.execute('{firefox {fileName }}')
    json_obj = json.loads(result)
    res = json_obj['data']
    for i in res['firefox']:
        ans.append(i['fileName'])
    new_ans = []
    for d in ans:
        if d not in new_ans:
            new_ans.append(d)
    print(new_ans)
    file = open('/home/iosdev747/Desktop/Linus/Linus/output.txt', 'w')
    data = {}
    order = []
    Image = []
    URI = []
    Text = []

    for a in new_ans:
        order.append(3)
        Text.append({"data": a})
        print(a+'---')
    data['title'] = "Here is your results"
    data['order'] = order
    data['Image'] = Image
    data['URI'] = URI
    data['Text'] = Text
    data['command'] = ""
    json_data = json.dumps(data)
    file.write(json_data)
    file.close()
