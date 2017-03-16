def eval(cmd, input=None):
    s = ""
    if cmd['service'] == 'M': ## Music
        return laundry.eval(cmd['args'])
    else:
        return "ERROR 42: service not recognized"

## list of services that need the user's input to work, not a command
def needsInput(cmd):
    return cmd['service'] in ['W']

def special(incoming):
    body = ''
    if incoming.upper() == "Music" :
        body = Music.special
    elif incoming.upper() == "DEMO":
      
        ## welcome/instructions
        body = 'Thanks for using Harvard Now!\n'
        body += 'Text Music to view the Billboard Top 20 songs of the week\n'
    return body