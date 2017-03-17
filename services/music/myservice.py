def eval(cmd, input=None):
    s = ""
    if cmd['service'] == 'M': ## Music
        return music.eval(cmd['args'])
    else:
        return "ERROR 42: service not recognized"

def special(incoming):
    body = ''
    if incoming.upper() == "MUSIC" :
        body = music.special
    elif incoming.upper() == "DEMO":
      
        ## welcome/instructions
        body = 'Thanks for using Harvard Now!\n'
        body += 'Text Music to view the Billboard Top 20 songs of the week\n'
    return body
