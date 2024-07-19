import music

def ask(query:str):
    answers = [
        i.split(')')[0].lower()
        for i in query.split('(')
        if ')' in i
    ]
    return answers.index(input(query).lower())

if __name__ == '__main__':
    match ask('(S)potify or (A)pple Music?\n> '):
        case 0:
            provider = music.sfy
        case 1:
            provider = music.apm
    playlist = provider.playlist(input('Playlist link\n> '))
    print('Playlist indexed. Backing playlist via Youtube Music.')
    music.ytm.playlist(playlist)
