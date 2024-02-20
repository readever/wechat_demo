import simplestart as ss
import yaml

def testme():
    ss.openpage("main")

ss.md("#### SimpleStart 功能演示")
ss.md("---")


with open('./config.yaml', 'r') as file:
    en_data = yaml.safe_load(file)

def parse(data):
    result = []
    for item in data:
        if isinstance(item, dict):
            title = list(item.keys())[0]
            children = item[title]
            if isinstance(children, list):
                result.append({"type": "subheader", "text": title})
                result.extend(parse(children)) 
            else:
                if title == "tag":
                    result.append({"type":"divider"})
                else:
                    result.append({"type": "page", "text": title, "route": children})
        
    return result

new_data = parse(en_data["pages"])

data = [
    {"type":"subheader", "text":"subheader"},
    {"type":"page", "text":"testme1", "route":"main"},
    {"type":"page", "text":"testme2", "route":"main"},
    {"type":"divider"},
    {"type":"subheader", "text":"subheader"},
    {"type":"page", "text":"testme1", "route":"main"},
    {"type":"page", "text":"testme2", "route":"main"}
]

tmp = '''
<v-list density="compact">
    <div v-for="item in data">
        <v-list-item
        v-if="item.type === 'page'"
        :key="i"
        :title="item.text"
        active-color="primary"
        \@click='onserver("myclick", item.route)'
        >
        </v-list-item>
        <v-list-subheader v-else-if="item.type === 'subheader'">
            {{ item.text }}
        </v-list-subheader>
        <v-divider v-else-if="item.type === 'divider'"></v-divider>
    </div>
</v-list>
'''

def myclick(state, value=None):
    value = value.replace(".py", "")
    if value != None:
        ss.openpage(value)

ss.template(tmp, data = new_data, handlers={"myclick":myclick})