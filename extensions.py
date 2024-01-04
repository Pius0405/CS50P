filename = input('File name: ').strip().lower()
suffix = filename.split('.')[-1]
match suffix:
    case 'gif':
        print('image/gif')
    case 'jpg':
        print('image/jpeg')
    case 'jpeg':
        print('image/jpeg')
    case 'png':
        print('image/png')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/zip')
    case _:
        print('application/octet-stream')

