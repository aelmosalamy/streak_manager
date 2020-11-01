import json

DATA = {
        'user': {},
        'streaks': []
    }

COMMANDS = {
        "show": lambda args : cmd_show(args),
        "hello": lambda args : cmd_hello(args),
        "create": lambda args : cmd_create(args)
    }

def save_data():
    with open('st_data.json', 'w+') as f:
        data_to_write = json.dumps(DATA, sort_keys=True, indent=4)
        f.write(data_to_write)
    return

def load_data():
    try:
        with open('st_data.json', 'r') as f:
            loaded_data = json.loads(f.read())
            global DATA
            DATA = loaded_data
            print('streak_manger: `st_data.json` loaded.')
    except:
        print("cant find `st_data.json`.")
        
# Tokenizes an input string and does some basic processing on the provided tokens
def parse_input(text):
    tokens = text.lower().split(" ")
    command = tokens[0]
    args = [x for x in tokens[1:] if x != '']
    return {
        "command": command,
        "args": args
        }

####################
# CMDLET FUNCTIONS #
####################
def cmdlet_show_info():
    print("streak_manager (sm) is an API developed by <@aelmosalmy> to track streaks and help you stay focused.")

def cmdlet_show_help():
    print("you communicate with sm through typing commands, some commands are short, some are lengthy. sm understands " + str(len(COMMANDS.keys())) + " commands currently, they are: " + " | ".join(COMMANDS.keys()))

def cmdlet_show_streaks():
    if not len(DATA['streaks']):
        print('you havent created any streaks yet, try `create streak`.')
    elif len(DATA['streaks']) == 1:
        print('you have 1 streak loaded.')
    else:
        print('you have ' + str(len(DATA['streaks'])) + ' streaks loaded.')
    for st in DATA['streaks']:
        print('- ' + st['name'] + '/' + st['type'])
        print('\tDATA HERE')
        
def cmdlet_create_streak():
    st_name = input('new streak name: ').strip()
    st_type = input('new streak type: track | daily | goal? ')
    DATA['streaks'].append({
            'name': st_name,
            'type': st_type,
            'data': {}
        }
    )
    save_data()
    print('`' + st_name + '` streak of type `' + st_type + '` created.')
    
#####################
# COMMAND FUNCTIONS #
#####################
# A non-destructive command that displays stored data to the user based on the first arg
def cmd_show(args):
    if not len(args):
        print("show what exactly: info | help | streaks?")
        return
    t = args[0]
    if t == 'info':
        cmdlet_show_info()
    elif t == 'help':
        cmdlet_show_help()
    elif t == 'streaks':
        cmdlet_show_streaks()
    else:
        print('i cant show you that')

def cmd_create(args):
    if not len(args):
        print("create what exactly: streak?")
        return
    t = args[0]
    if t == 'streak':
        cmdlet_create_streak()
def cmd_hello(args):
    print("hello! stranger")

# Function responsible for executing a command based on a standard {"command": ..., "args": ...} dict provided by `parse_input` function
def execute_command(parsed_input):
    # Encapsulating the everything with try/except to handle `KeyError` errors properly when an invalid command is entered
    try:
        command = parsed_input["command"]
        args = parsed_input["args"]
        # Grab the function that corresponds to the inputted command from the `COMMANDS` dict
        command_function = COMMANDS[command]
        # Execute that function passing `args` as a param
        command_function(args)
    except KeyError:
        print("invalid command, for a list of available commands type 'show help'")

def cli_loop():
    load_data()
    inp = ''
    inp_state = 'normal'
    state_prompt_map = {'normal': ': '}
    while True:
        inp = input(state_prompt_map[inp_state]).strip().lower()
        if inp == '':
            continue
        elif inp == 'exit' or inp == 'quit':
            return
        execute_command(parse_input(inp))
    return
        
if __name__ == '__main__':
    cli_loop()
