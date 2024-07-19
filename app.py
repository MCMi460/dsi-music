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
            from music.sfy import sfy
            playlist = sfy.playlist(input('Playlist link\n> '))
        case 1:
            from music.apm import apm
            input('Start playing a song in your desired'
            + ' playlist.\nPress enter to continue...')
            playlist = apm.playlist()
            assert input(f'Playlist: {playlist.name}\n'
            + 'Type \'exit\' right now to end the '
            + 'script if this is not desired.\n> '
            ).lower() != 'exit'
    print('Playlist indexed. Backing playlist via Youtube Music.')
    music.ytm.playlist(playlist)
