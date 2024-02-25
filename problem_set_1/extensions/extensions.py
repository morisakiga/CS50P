"""
See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

In a file called extensions.py, implement a program that prompts the user for the name of a file and 
then outputs that file's media type if the file's name ends, case-insensitively, in any of these 
suffixes:

.gif .jpg .jpeg .png .pdf .txt .zip

If the file's name ends with some other suffix or has no suffix at all, output application/
octet-stream instead, which is a common default.
"""

def get_extension():
    extension = input("File name: ").lower().strip().split(sep=".")
    return extension[-1]


def main():
    extension = get_extension()

    if extension == "gif":
        print("image/gif")
    elif extension == "jpg" or extension == "jpeg":
        print("image/jpeg")
    elif extension == "png":
        print("image/png")
    elif extension == "pdf":
        print("application/pdf")
    elif extension == "txt":
        print("text/plain")
    elif extension == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")


main()