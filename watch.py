import re

def main():
    print(parse(input("HTML: ")))

#possible URL formats
#http://youtube.com/embed/xvFZjo5PgG0
#https://youtube.com/embed/xvFZjo5PgG0
#https://www.youtube.com/embed/xvFZjo5PgG0

def parse(s):
    match_obj = re.search(r'"https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9]+)"', s)
    if match_obj:
        return 'https://youtu.be/'+match_obj.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
