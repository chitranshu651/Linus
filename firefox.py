import subprocess


def open_url(parameter):
    subprocess.Popen("firefox -new-tab " + (parameter['url']), stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)


def save(parameter):
    import json, lz4.block
    import time
    from credentials import connection
    print("Opened database successfully")

    str = (str(subprocess.check_output(['bash', 'path.sh'])).split("'")[1])[:-2]
    with open(str+"/recovery.jsonlz4", "rb") as read_file:
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
    print(("=" * 20 + "\n") * 2)

    print("Records created successfully")
    connection.close()
    print("done")


def load(parameter):
    import json
    from graphqlclient import GraphQLClient
    client = GraphQLClient('https://asdfghjklasdf.herokuapp.com/v1alpha1/graphql')
    print('client created')
    result = client.execute('{firefox (where: {fileName: {_eq:\"' + parameter['saveFile'] + '\"}}){id windowNumber tabNumber timestamp URI }}')
    print('executed')
    print(result)
    json_obj = json.loads(result)
    print(json_obj)
    res = json_obj['data']
    print(res)
    for i in res['firefox']:
        print(i['id'])
        print(i['windowNumber'])
        print(i['tabNumber'])
        print(i['timestamp'])
        print(i['URI'])
        parameter['url'] = i['URI']
        open_url(parameter)
        print('=' * 40)
