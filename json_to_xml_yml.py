import xmltodict,json,yaml
with open('sample.json', 'r') as f_j:
    d_j = json.load(f_j)

with open('sample.yaml', 'w') as f_y:
    d_y = yaml.dump(d_j, f_y)
with open('sample.xml', 'w') as f_x:
    f_x.write(xmltodict.unparse(d_j))